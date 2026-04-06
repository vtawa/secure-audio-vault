# Secure Audio Vault (S3 + Terraform + Python)

A cloud-native secure storage solution designed for artists and digital creators to share private audio assets using time-limited, encrypted access links.

## Overview
This project automates the creation of a hardened AWS S3 environment and provides a backend utility to share private files without ever making them public. It eliminates the "Public S3 Bucket" vulnerability by using IAM-based presigned URLs.

## Tech Stack
* **Infrastructure:** Terraform (Infrastructure-as-Code)
* **Cloud Provider:** AWS (S3, IAM)
* **Backend:** Python 3.x (Boto3 SDK)
* **Security:** AES-256 Encryption, S3 Public Access Block (PAB)

## Security Features
* **Public Access Block:** Hardcoded Terraform policy to reject all public ACLs and policies.
* **Encryption at Rest:** Automated AES-256 server-side encryption for all uploaded assets.
* **Presigned URLs:** Temporary access links (default 30 min) that expire automatically, ensuring assets cannot be "scraped" or hot-linked.
* **Least Privilege:** Designed to run via dedicated IAM service accounts with scoped permissions.

## Project Structure
```text
.
├── terraform/          # IaC files to build the AWS environment
│   └── main.tf         # S3 Bucket, Security Block, & Encryption config
├── src/                # Python backend logic
│   └── handler.py      # Presigned URL generation logic
└── README.md           # Documentation
```
# Setup & Deployment Instructions
## 1. Prerequisites
Terraform installed.
Python 3.x installed.
AWS CLI configured or Access Keys ready.

# 2. Infrastructure Build
## Navigate to terraform directory
cd terraform

## Initialize and deploy
terraform init
terraform apply -auto-approve
# 3. Upload Test Asset
Log into the AWS S3 Console.

Find your bucket (e.g., secure-audio-vault).

Upload a file named test.mp3.
# 4. Run the Access Link Generator
## Navigate to the source directory
cd ../src

## Install dependencies
pip install boto3

## Set your temporary session credentials (if not using AWS CLI)
$env:AWS_ACCESS_KEY_ID="your_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret"
$env:AWS_DEFAULT_REGION="us-east-1"

## Run the script
python handler.py
# 5. Cleanup
## To avoid AWS charges after testing, run:
terraform destroy -auto-approve
# Results & Verification
<img width="1117" height="52" alt="image" src="https://github.com/user-attachments/assets/0714647f-3acc-436b-8278-8c127792f3cb" />

Infrastructure Validation: Successfully deployed the S3 environment via Terraform, confirming that all Public Access Block settings were active upon creation.

Security Testing: Attempted to access the test.mp3 file directly via its public S3 URL; confirmed that AWS returned a 403 Access Denied error as expected.

Functional Testing: Verified that the Python Boto3 script generated a valid Presigned URL.

Lifecycle Management: Used the temporary link to successfully stream the audio file, and verified that the link expired automatically after the set duration (30 minutes), restoring the "Private" state of the asset.
