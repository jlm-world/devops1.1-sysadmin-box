import boto3
import os
from datetime import datetime

SOURCE_DIR = "/var/log/nginx/old_logs"
BUCKET_NAME = "sysadmin-box-541099637062-541099637062-ap-south-1-an"

def upload_logs():
    s3 = boto3.client("s3")

    for filename in os.listdir(SOURCE_DIR):
        file_path = os.path.join(SOURCE_DIR, filename)

        if os.path.isfile(file_path):
            print(f"Uploading {filename}...")

            s3.upload_file(
                file_path,
                BUCKET_NAME,
                f"nginx-logs/{filename}"
            )

            print(f"Uploaded {filename} successfully.")

if __name__ == "__main__":
    upload_logs()
