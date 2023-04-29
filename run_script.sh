#!/bin/bash

source /Users/personal/Desktop/aws-sync/.venv/bin/activate
# Add a log entry
echo "Cron job started at $(date)" >> /Users/personal/Desktop/aws-sync/s3_sync.log

/Users/personal/Desktop/aws-sync/.venv/bin/python3 /Users/personal/Desktop/aws-sync/script.py

deactivate
