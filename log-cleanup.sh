#!/bin/bash

# Log Cleanup Script for Nginx
LOG_DIR="/var/log/nginx"
DAYS=7

echo "Starting log cleanup in $LOG_DIR..."

# Find and delete logs older than specified days
find "$LOG_DIR" -type f -name "*.log" -mtime +$DAYS -exec rm -f {} \;

echo "Cleanup completed successfully."
