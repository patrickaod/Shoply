from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime
import os
import pandas as pd
import logging

# Use the custom 'shoply' logger for application-specific logging
logger = logging.getLogger('shoply')


class Command(BaseCommand):
    help = 'Download and organize dataset from Kaggle'

    def handle(self, *args, **kwargs):
        # Step 1: Prompt user for required inputs
        file_name = input(
                "What file would you like to process? "
                "(Example: data/raw/your_dataset.csv): "
            ).strip()

        file_path = Path(settings.BASE_DIR) / file_name

        # Check if file exists
        if not file_path.exists():
            logger.error(f"File not found at {file_path}")
            return

        header = input(
            "What header would you like to sample by? "
            "(e.g., category): "
        ).strip()

        selected_elements = input(
            "Which elements should be selected from this header "
            "(leave blank for all)? (e.g., electronics, clothing): "
        ).strip()

        sample_size = input(
            "How many samples should be taken per category? "
            "(Default: 50): "
        ).strip()

        sample_random = input(
            "Would you like the sample to be random? "
            "(yes/no, Default: yes): "
        ).strip().lower()

        # Set defaults if necessary
        sample_size = int(sample_size) if sample_size else 50
        sample_random = sample_random != "no"  # Defaults to True if left blank

        # Convert selected elements to list
        elements_list = [
                elem.strip() for elem in selected_elements.split(',')
            ] if selected_elements else []

        # Step 2: Load the dataset
        try:
            df = pd.read_csv(file_path)
            logger.info(f"Loaded dataset from {file_path}")
        except pd.errors.ParserError:
            logger.error(
                f"Error parsing the file: {file_path}. "
                "The file may not be a valid CSV."
            )
            return
        except Exception as e:
            logger.error(f"Error loading file: {e}")
            return

        # Step 3: Filter by the specified header and elements
        if header not in df.columns:
            logger.error(
                f"Header '{header}' not found in the dataset columns."
            )
            return

        # If no elements are provided, sample all unique values from the header
        if not elements_list:
            logger.info(
                f"No specific elements selected for '{header}'. "
                "Using all unique values from this header."
            )
            elements_list = df[header].unique()

        # Filter the dataset based on the elements provided
        df_filtered = df[df[header].isin(elements_list)]
        logger.info(
            f"Filtered dataset by elements in '{header}': {elements_list}"
        )

        # Step 4: Sample data from each category in the header
        sampled_data = []

        for element in elements_list:
            # Filter the rows where the header matches the current element
            group = df_filtered[df_filtered[header] == element]

            if group.empty:
                logger.warning(
                    f"No data for element '{element}' in header '{header}'"
                )
                continue

            # Randomly sample data, or take all if fewer than sample_size
            if sample_random:
                group_sampled = group.sample(
                    n=min(sample_size, len(group)),
                    random_state=None
                )

            else:
                # If no random sampling, take the first `sample_size` rows
                group_sampled = group.head(sample_size)

            # Add the sampled group to the list of sampled data
            sampled_data.append(group_sampled)

            logger.info(
                        f"Sampled {len(group_sampled)} from '{element}' "
                        f"({len(group)})"
                    )

        # Check the length of sampled_data before concatenation
            if not sampled_data:
                logger.error(
                    "No samples selected or sampled_data is empty."
                )
                return  # Exit the function

        # Combine all sampled data into a single DataFrame
            try:
                final_sampled_data = pd.concat(sampled_data, ignore_index=True)
                logger.info(
                    f"Total sampled data: {len(final_sampled_data)} "
                    "rows"
                )

            except ValueError as e:
                logger.error(f"Error while concatenating data: {e}")
                return  # Exit or handle the error

        # Step 5: Save the processed data to the 'data/processed' directory
        processed_dir = Path(settings.BASE_DIR) / 'data/processed'
        processed_dir.mkdir(parents=True, exist_ok=True)

        # Generating a new file name based on the original
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        processed_file_path = processed_dir / f"{timestamp}_processed_"
        processed_file_path += f"{file_path.stem}.csv"

        try:
            final_sampled_data.to_csv(processed_file_path, index=False)
            logger.info(
                f"Processed data successfully saved to: {processed_file_path}"
            )

        except Exception as e:
            logger.error(f"Error saving processed data: {e}")
            return

        # Step 6: Confirm deletion of the original file
        delete_original = input(
                "Would you like to delete the original"
                "dataset file? (yes/no): "
            ).strip().lower()

        if delete_original == "yes":
            try:
                os.remove(file_path)
                logger.info(
                    f"Original dataset file {file_path} deleted successfully."
                )
            except Exception as e:
                logger.error(f"Error deleting file: {e}")
        else:
            logger.info(f"Original dataset file retained: {file_path}")
