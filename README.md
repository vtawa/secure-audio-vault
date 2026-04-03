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
