import os
import boto3
import logging
from pathlib import Path

log_filename = '/Users/personal/Desktop/aws-sync/s3_sync.log'
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Replace this with your own value
local_directory = '/Users/personal/Desktop/AWS-DNY'
bucket_name = 'dnydata2023-04-28'
profile = 'macbook'

def upload_to_s3(file_path, bucket, s3_key, session):
    try:
        s3 = session.client('s3')
        s3.upload_file(file_path, bucket, s3_key)
        logging.info(f'Uploaded {file_path} to {bucket}/{s3_key}')
    except Exception as e:
        logging.error(f'Failed to upload {file_path} to {bucket}/{s3_key} - {e}')

def sync_directory(local_directory, bucket_name, profile):
    session = boto3.Session(profile_name=profile)
    local_directory_path = Path(local_directory)
    logging.debug(f'Starting sync for local directory: {local_directory_path}')

    for item in local_directory_path.glob('**/*'):
        if item.is_file() and not item.name.startswith('.DS_Store'):
            logging.debug(f'Processing file: {item}')
            s3_key = str(item.relative_to(local_directory_path))
            upload_to_s3(str(item), bucket_name, s3_key, session)

    logging.debug(f'Finished sync for local directory: {local_directory_path}')

if __name__ == '__main__':
    sync_directory(local_directory, bucket_name, profile)





