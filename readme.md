# Project 1 — SysAdmin Box

My first hands-on DevOps project.

I set up a Linux server on AWS, hosted my portfolio website with Nginx, and added a few small automations for logs and backups.

## What I Built

* AWS EC2 server running Amazon Linux 2023
* Nginx hosting my portfolio
* Bash script for cleaning up old Nginx logs
* Cron job to run the cleanup automatically
* Python backup script using boto3
* S3 bucket for backups
* IAM role for connecting the EC2 server to AWS services
* Git + GitHub for the project

## How It Works

```text
Portfolio Website
       ↓
     Nginx
       ↓
    EC2 Server
     ↙     ↘
   Logs   Backups
    ↓        ↓
 Bash      Python
    ↓        ↓
 Archive    S3
```

## Project Structure

```text
sysadmin-box/
├── scripts/
│   ├── log-cleanup.sh
│   └── s3-backup.py
└── README.md
```

## A Little About The Project

This was mainly a learning project for me to get comfortable with Linux, AWS and basic DevOps tasks.

I started with getting the website running, then gradually added the automation and AWS parts.

There were definitely a few things that didn't work on the first try 😅, but fixing those problems was probably one of the most useful parts of the project.

## What I Learned

* How to work with a Linux server through SSH
* How Nginx serves a website
* Basic Bash scripting
* Cron jobs
* Python automation
* boto3 and AWS
* IAM roles
* S3 backups
* Git and GitHub
status - finished
