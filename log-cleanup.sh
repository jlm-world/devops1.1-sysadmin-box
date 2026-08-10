#!/bin/bash

LOG_DIR="/var/log/nginx"
BACKUP_DIR="/var/log/nginx/old_logs"
DAYS=7

echo "Starting log cleanup process..."

# Ensure backup directory exists
mkdir -p "$BACKUP_DIR"

# Find logs older than $DAYS, compress them using gzip, and move them
find "$LOG_DIR" -maxdepth 1 -name "*.log" -mtime +$DAYS | while read -r file; do
    echo "Processing old log: $file"
    # Optional use of grep/awk to filter or inspect log stats before compressing
    ls -lh "$file" | awk '{print "File: " $9 ", Size: " $5}'
    
    # Compress the log file
    gzip "$file"
    
    # Move the gzipped file to the archive directory
    mv "$file.gz" "$BACKUP_DIR/"
done

# Clean up compressed logs older than 30 days from the backup folder
find "$BACKUP_DIR" -name "*.gz" -mtime +30 -exec rm -f {} \;

echo "Log cleanup and compression completed successfully."
