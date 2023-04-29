## AWS S3 Sync Script
This is a Python script that syncs local files and directories to an Amazon S3 bucket using the AWS CLI. The script is designed to be run as a cron job on macOS.

### Prerequisites

- Python 3
- AWS CLI configured with credentials and a default region
- An Amazon S3 bucket to sync files to
- macOS with the cron daemon running

### Installation
Follow these steps to install and configure the script:
1. Clone this repository to your local machine:
    git clone https://github.com/Yasharora2020/AWS-S3-Sync-Script.git

2. Navigate to the project directory:
    cd aws-s3-sync


3. Install the required Python packages:
    pip install -r requirements.txt


4. Edit the s3_sync.py file to set the local_directory and bucket_name variables to the appropriate values for your project.
    
    #!/bin/bash

    source /path/to/your/virtualenv/bin/activate

    python /path/to/your/s3_sync.py

    deactivate


5. Create a new shell script called run_script.sh:

    Replace /path/to/your/virtualenv and /path/to/your/s3_sync.py with the correct paths for your project. This script activates the virtual environment and then runs the s3_sync.py script.

6. Make the shell script executable:
    chmod +x run_script.sh


7. Add a new cron job by running the following command:
    crontab -e


8. Add the following line to the crontab file:
    * * * * * /path/to/your/run_script.sh >> /path/to/your/s3_sync.log 2>&1

    Replace /path/to/your/run_script.sh and /path/to/your/s3_sync.log with the correct paths for your project.

9. Save the crontab file and exit the editor.

### Usage
The script will run every minute as specified in the crontab file. When the script runs, it will sync the files in the local_directory to the specified S3 bucket.

You can view the log file at /path/to/your/s3_sync.log to see the output of the script and any error messages.

### Troubleshooting
If the script is not syncing files as expected, check the following:

- Check the contents of the log file for any error messages.
- Make sure that the AWS CLI is configured correctly and that you have the necessary permissions to access the S3 bucket.
- Check that the cron daemon is running and that the cron job is set up correctly.
- Check that the file permissions are set correctly for the shell script and the Python script.
- Test the script manually to make sure it works as expected.

### License
This project is licensed under the MIT License - see the LICENSE file for details.




