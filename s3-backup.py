import tarfile
import os
from datetime import datetime

# Configuration for a local backup archive
SOURCE_DIR = '/home/ec2-user'
BACKUP_DIR = '/home/ec2-user/backups'

# Ensure backup directory exists
os.makedirs(BACKUP_DIR, exist_ok=True)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_filename = f"backup_{timestamp}.tar.gz"
backup_path = os.path.join(BACKUP_DIR, backup_filename)

def create_backup():
    try:
        print(f"Creating backup of {SOURCE_DIR}...")
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))
        print(f"Backup created successfully at {backup_path}")
    except Exception as e:
        print(f"Backup failed: {e}")

if __name__ == '__main__':
    create_backup()
