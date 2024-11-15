import csv
import json
from django.core.management.base import BaseCommand
from pathlib import Path
import logging
from datetime import datetime
import re
from django.conf import settings

# Initialize logger
logger = logging.getLogger('shoply')


class Command(BaseCommand):
    help = 'Convert a CSV file to JSON with an updated timestamped filename and save it in the data/json folder'

    def handle(self, *args, **kwargs):
        # Step 1: Prompt for the CSV file path
        csv_file_path = input("Enter the path of the CSV file (e.g., data/processed/your_file.csv): ").strip()

        # Validate CSV file path
        csv_file = Path(settings.BASE_DIR) / csv_file_path
        if not csv_file.exists() or not csv_file.is_file():
            logger.error(f"File not found: {csv_file_path}")
            return

        # Step 2: Check the filename and add/replace timestamp
        new_file_name = self.add_or_replace_timestamp(csv_file.name)
        json_folder = Path(settings.BASE_DIR) / "data/json"
        json_folder.mkdir(parents=True, exist_ok=True)  # Ensure folder exists
        json_file_path = json_folder / (new_file_name + ".json")

        logger.info(f"Processing file '{csv_file.name}' -> New JSON file: {json_file_path}")

        # Step 3: Read CSV and convert to JSON
        try:
            with csv_file.open(mode='r', encoding='utf-8') as csv_file_obj:
                csv_reader = csv.DictReader(csv_file_obj)
                data = self.convert_csv_to_fixture_format(csv_reader)

            # Step 4: Save to JSON
            with json_file_path.open(mode='w', encoding='utf-8') as json_file_obj:
                json.dump(data, json_file_obj, indent=4)

            logger.info(f"Successfully converted CSV to JSON: {json_file_path}")
        except Exception as e:
            logger.error(f"Error processing file: {e}")
            return

    @staticmethod
    def add_or_replace_timestamp(file_name):
            """
            Checks if the filename starts with a timestamp and replaces it with the current timestamp.
            If no timestamp is present, it adds one.
            """
            current_timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            file_stem = Path(file_name).stem

            # Regex to validate timestamp (DD-MM-YY_HH-MM-SS)
            timestamp_pattern = r'^\d{2}-\d{2}-\d{4}_\d{2}-\d{2}-\d{2}_'

            if re.match(timestamp_pattern, file_stem):
                # Remove the existing timestamp
                file_stem = re.sub(timestamp_pattern, "", file_stem)

            # Add the new timestamp
            new_file_name = f"{current_timestamp}_{file_stem}"
            return new_file_name

    def convert_csv_to_fixture_format(self, csv_reader):
        """
        Converts CSV rows into Django fixture format
        Adds the model reference and transforms each row into 'fields' format.
        """
        data = []
        for row in csv_reader:
            # Create the fixture entry for each row
            product_entry = {
                "model": "products.Product",
                "fields": {
                    "asin": row['asin'],
                    "title": row['title'],
                    "imgUrl": row['imgUrl'],
                    "productURL": row['productURL'],
                    "stars": float(row['stars']) if row['stars'] else None,  # Convert to float
                    "reviews": int(row['reviews']) if row['reviews'] else None,  # Convert to int
                    "price": float(row['price']) if row['price'] else None,  # Convert to float
                    "isBestSeller": row['isBestSeller'].lower() == 'true',  # Convert string to boolean
                    "boughtInLastMonth": row['boughtInLastMonth'].lower() == 'true',  # Convert string to boolean
                    "categoryName": row['categoryName']
                }
            }
            data.append(product_entry)
        return data