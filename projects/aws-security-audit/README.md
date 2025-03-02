# AWS Security Audit Project

## 📄 Project Overview

This project involved conducting a comprehensive **security audit** of an AWS environment to assess configurations, access controls, and overall cloud security posture. The goal was to identify misconfigurations, excessive permissions, and potential exposure risks.

---

## 🎯 Objectives

- Review **IAM policies**, roles, and permissions.
- Analyze **S3 bucket policies** for public exposure.
- Review **CloudTrail logs** for suspicious or unauthorized activity.
- Assess compliance with **AWS Well-Architected Framework** and **CIS AWS Foundations Benchmark**.

---

## 🔧 Tools Used

| Tool/Service | Purpose |
|---|---|
| **AWS CLI** | Manual configuration and policy review |
| **AWS Security Hub** | Consolidated view of security findings |
| **AWS Config** | Continuous monitoring of resource configurations |
| **CloudTrail** | Monitoring and analysis of user and service activity |
| **Python (Boto3)** | Automated audits for public S3 buckets (sample script included) |

---

## 📂 Files in This Project

| File | Description |
|---|---|
| `aws-audit-report.pdf` | Full audit report summarizing findings and recommendations |
| `aws-cli-commands.txt` | All AWS CLI commands used during the audit |
| `boto3-public-bucket-checker.py` | Python script to check for public S3 buckets |
| `screenshot-securityhub.png` | Screenshot showing findings in AWS Security Hub |

---

## 📝 Key AWS CLI Commands Used

### Check S3 Bucket Policies
```bash
aws s3api get-bucket-acl --bucket example-bucket
