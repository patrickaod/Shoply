from django.core.management.base import BaseCommand
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi
from django.conf import settings
import os
import logging

# Get the logger instance
logger = logging.getLogger('shoply')


class Command(BaseCommand):
    help = 'Download and organise dataset from Kaggle'

    def add_arguments(self, parser):
        # Add a custom argument for the dataset URL
        parser.add_argument(
            '--dataset-url',
            type=str,
            help=(
                'Use the LAST PART of the Kaggle dataset URL to download '
                '(e.g., username/dataset-name)'
            )
        )

    def handle(self, *args, **kwargs):
        # Step 1: Get the dataset URL from the command arguments
        dataset_url = kwargs['dataset_url']

        if not dataset_url:
            logger.error(
                "You must provide a dataset URL using the --dataset-url option"
            )
            return

        logger.info(
            f'Downloading dataset from: '
            f'https://www.kaggle.com/datasets/{dataset_url}'
        )

        # Step 2: Ensure Kaggle credentials are available
        kaggle_username = os.getenv("KAGGLE_USERNAME")
        kaggle_key = os.getenv("KAGGLE_KEY")
        if not all([kaggle_username, kaggle_key]):
            logger.error("KAGGLE_USERNAME or KAGGLE_KEY is not set")
            return  # Exit early if credentials are missing

        # Step 3: Authenticate with Kaggle API
        api = KaggleApi()
        try:
            api.authenticate()
            logger.info('Authenticated with Kaggle API successfully.')
        except Exception as e:
            logger.error(f'Failed to authenticate with Kaggle API: {e}')
            return

        # Step 4: Ensure the 'data/raw/' folder exists
        data_raw_dir = Path(settings.BASE_DIR) / 'data/raw'
        data_raw_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f'Data will be saved to: {data_raw_dir}')

        # Step 5: Download the dataset using the Kaggle API
        logger.info(f'Downloading dataset...')
        try:
            api.dataset_download_files(
                dataset_url, path=str(data_raw_dir), unzip=True
            )
            logger.info("Dataset downloaded successfully")
        except Exception as e:
            logger.error(f"Error downloading the dataset: {e}")
            return
