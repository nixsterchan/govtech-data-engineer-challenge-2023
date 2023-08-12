import pandas as pd
import re
import argparse
import logging
import os
import hashlib
from datetime import datetime

logging.basicConfig(
    filename='logger.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Initiate logger
logger = logging.getLogger(__name__)

# Data ingest and output points
INGESTION_DATA_FOLDER = '../ingestion-data/'
SUCCESSFUL_APPS_FOLDER = 'successful-applications/'
FAILED_APPS_FOLDER = 'failed-applications/'

# Validation variables
DOB_REQUIRED_FORMAT = '%Y%m%d'
EXPECTED_MOBILE_NO_LEN = 8
EMAIL_PATTERN = r'@.*\.(com|net)'

# 1st Jan 2022 reference point for age comparison
DATE_REFERENCE_POINT = datetime(2022, 1, 1)

def create_folder(file_path):
    """
    Helper function to create folder if non existing.

    Args:
        file_path (string): Path for the folder to be created.

    Returns:
        None
    """
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        logger.info(f'Created folder: {file_path}.')
    return None


def main():
    logger.info('Beginning file processing.')

    # Create output folders if non-existent
    for f_path in [SUCCESSFUL_APPS_FOLDER, FAILED_APPS_FOLDER]:
        create_folder(f_path)

    # Retrieve list of csv files to be processed 
    csv_file_names = [file for file in os.listdir(INGESTION_DATA_FOLDER) if file.endswith('.csv')]

    for f_name in csv_file_names:
        f_path = os.path.join(INGESTION_DATA_FOLDER, f_name)
        logger.info(f'Working on file: {f_path}')
        # Output file paths
        success_out_path = os.path.join(SUCCESSFUL_APPS_FOLDER, f_name)
        failed_out_path = os.path.join(FAILED_APPS_FOLDER, f_name)

        try:
            df = pd.read_csv(f_path, header=0, index_col=False)
            logger.info(f'Dataframe shape: {df.shape}.')
        except Exception as e:
            logger.error(f'Ran into an issue while attempting to read dataframe. Moving to next file.')

        if df.shape[0] == 0: continue

        # Perform preprocessing tasks
        try:
            # Convert date_of_birth to preferred format
            df['conv_date'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
            df['date_of_birth'] = df['conv_date'].dt.strftime(DOB_REQUIRED_FORMAT)

            # Check age for validation
            df['age'] = (DATE_REFERENCE_POINT - df['conv_date']).astype('<m8[Y]')
            df['above_18'] = df['age'] >= 18

            # Check if email is valid
            df['is_valid_email'] = df['email'].str.contains(EMAIL_PATTERN, regex=True)

            # Mark out rows that failed the requirements (i.e. not above 18, non valid email, number!=8, null name)
            df['is_failed_application'] = (~df['above_18']) | (~df['is_valid_email']) | (df['name'].isnull()) | (df['mobile_no'].str.len() != EXPECTED_MOBILE_NO_LEN)
            df = df.drop(columns=['age', 'is_valid_email', 'conv_date'])

            # Split into successful and failed dfs
            df_success = df[df['is_failed_application'] != True].drop(columns='is_failed_application')
            df_failed = df[df['is_failed_application']].drop(columns='is_failed_application')

            logger.info(f'Dataframe split into successful and failed applications.')

            # Split name into first_name and last_name
            df_success[['first_name', 'last_name']] = df['name'].str.split(n=1, expand=True)

            # Create 'membership_id' column that follows the formula <last_name>_<SHA256hash(bdate)[-5:] 
            df_success['membership_id'] = df_success.apply(lambda row: f"{row['last_name']}_{hashlib.sha256(row['date_of_birth'].encode()).hexdigest()[-5:]}", axis=1)
            df_success = df_success.drop(columns=['name'])
            
            logger.info(f'Successful applications sucessfully processed.')

        except Exception as e:
            logger.error(f'Ran into an issue while processing present dataframe. Moving to next file.')
        
        try:
            df_success.to_csv(success_out_path, header=True, index=False)
            df_failed.to_csv(failed_out_path, header=True, index=False)

            logger.info(f'Success and failed application dataframes were successfully written out.')
        except Exception as e:
            logger.error(f'Ran into an issue while writing out success and failed dataframes. Moving to next file.')
        
    return None


if __name__ == "__main__":
    main()