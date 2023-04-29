#!/bin/bash

source /Users/personal/Desktop/aws-s3-sync-script/.venv/bin/activate
# Add a log entry
echo "Cron job started at $(date)" >> /Users/personal/Desktop/aws-s3-sync-script/s3_sync.log

/Users/personal/Desktop/aws-s3-sync-script/.venv/bin/python3 /Users/personal/Desktop/aws-s3-sync-script/script.py

deactivate
