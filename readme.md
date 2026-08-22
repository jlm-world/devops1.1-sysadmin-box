

```markdown
# Project 1 — SysAdmin Box

My first hands-on DevOps project. 

I set up a Linux server on AWS, hosted my website with Nginx, and added automated scripts for logs and cloud backups.

## What I Built

* **AWS EC2:** Deployed and configured a server running Amazon Linux 2023.
* **Nginx:** Installed and configured the web server to host the project status page.
* **Log Management:** Built a Bash script (`log-cleanup.sh`) to rotate, compress, and purge old Nginx logs.
* **Cloud Backups:** Developed a Python script (`s3-backup.py`) utilizing `boto3` to securely upload log archives to an AWS S3 bucket.
* **Automation:** Configured automated cron jobs to run log maintenance and backups on a schedule.
* **Security & IAM:** Configured roles and access for secure communication between EC2 and AWS services.
* **Version Control:** Managed source code and documentation using Git and GitHub.

## How It Works

```text
Website Request
       ↓
     Nginx
       ↓
   EC2 Server
    ↙      ↘
  Logs    Backups
   ↓         ↓
 Bash      Python
   ↓         ↓
Archive     S3 Bucket

```

## Project Structure

```text
sysadmin-box/
├── scripts/
│   ├── log-cleanup.sh
│   └── s3-backup.py
└── README.md

```

## Project Reflections

This was a hands-on learning project to build comfort with Linux environments, core AWS services, and basic DevOps workflows.

Working through real-time debugging—from configuring file permissions to troubleshooting script paths and AWS credentials—made the learning experience practical and rewarding.

## What I Learned

* Managing a remote Linux server via SSH
* Web server deployment and configuration with Nginx
* Writing automated maintenance scripts in Bash
* Scheduling routine tasks with Cron
* Building cloud automation scripts in Python using `boto3`
* Interfacing EC2 securely with AWS S3 using IAM
* Maintaining clean version control with Git and GitHub

---

**Status:** Completed ✅

```

```
