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
        success_out_path = os.path.join(SUCCESSFUL_APPS_FOLDER, f_name)
        failed_out_path = os.path.join(FAILED_APPS_FOLDER, f_name)

        df = pd.read_csv(f_path, header=0, index_col=False)
        print(df.shape)

        # Convert date of birth to preferred format
        df['conv_date'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
        df['date_of_birth'] = df['conv_date'].dt.strftime(DOB_REQUIRED_FORMAT)

        # Get the age for comparison
        df['age'] = (DATE_REFERENCE_POINT - df['conv_date']).astype('<m8[Y]')
        df['is_valid_email'] = df['email'].str.contains(EMAIL_PATTERN, regex=True)
        df['above_18'] = df['age'] >= 18

        df['is_failed_application'] = (~df['above_18']) | (~df['is_valid_email']) | (df['name'].isnull()) | (df['mobile_no'].str.len() != EXPECTED_MOBILE_NO_LEN)
        
        df = df.drop(columns=['age', 'is_valid_email', 'conv_date'])

        df_success = df[df['is_failed_application'] != True].drop(columns='is_failed_application')
        df_failed = df[df['is_failed_application']].drop(columns='is_failed_application')



        df_success[['first_name', 'last_name']] = df['name'].str.split(n=1, expand=True)
        df_success['membership_id'] = df_success.apply(lambda row: f"{row['last_name']}_{hashlib.sha256(row['date_of_birth'].encode()).hexdigest()[-5:]}", axis=1)

        df_success = df_success.drop(columns=['name'])
        # Split up dataframe into successful and unsuccessful applications based on the name
        # df = df.apply(lambda row: row[''])
        # Filter by mobile number

        # Filter by age

        # Filter by valid email

        # Output
        df_success.to_csv(success_out_path, header=True, index=False)
        df_failed.to_csv(failed_out_path, header=True, index=False)
        

        
    return None


if __name__ == "__main__":
    main()