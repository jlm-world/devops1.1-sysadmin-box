import boto3
import os

SOURCE_DIR = "/var/log/nginx/old_logs"
BUCKET_NAME = "sysadmin-box-541099637062-541099637062-ap-south-1-an"
REGION = "ap-south-1"

def upload_logs():
    if not os.path.exists(SOURCE_DIR):
        print(f"Folder not found: {SOURCE_DIR}")
        return

    s3 = boto3.client("s3", region_name=REGION)

    files = os.listdir(SOURCE_DIR)
    if not files:
        print("No files to upload.")
        return

    for filename in files:
        file_path = os.path.join(SOURCE_DIR, filename)

        # Only upload files, only .gz files
        if not os.path.isfile(file_path):
            continue
        if not filename.endswith(".gz"):
            continue

        print(f"Uploading {filename}...")

        try:
            s3.upload_file(
                file_path,
                BUCKET_NAME,
                f"backups/{filename}"
            )
            print(f"Uploaded {filename} successfully.")
        except Exception as e:
            print(f"Failed to upload {filename}: {e}")

if __name__ == "__main__":
    upload_logs()
