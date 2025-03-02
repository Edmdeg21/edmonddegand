# AWS Security Audit Project

## 📄 Project Overview

This project involved conducting a comprehensive **security audit** of an AWS environment, focusing on identifying **misconfigurations**, **overly permissive policies**, and **potential security risks** across AWS services like IAM, S3, CloudTrail, and more.

The goal was to assess the environment against **AWS security best practices**, including the **AWS Well-Architected Framework** and **CIS AWS Foundations Benchmark**.

---

## 🎯 Objectives

- Review **IAM policies, roles, and permissions**.
- Check **S3 bucket permissions, encryption status, and public access policies**.
- Review **CloudTrail configuration and coverage across all regions**.
- Identify unused or excessively permissive **IAM users, roles, and policies**.
- Check for active findings in **AWS Security Hub**.

---

## 🔧 Tools & Technologies Used

| Tool | Purpose |
|---|---|
| **AWS CLI** | Direct configuration review and evidence gathering |
| **AWS Security Hub** | Consolidated view of security and compliance findings |
| **AWS Config** | Continuous monitoring and rule-based compliance checking |
| **CloudTrail** | Review of logged API calls and user activity |
| **IAM Access Analyzer** | Detect overly permissive policies and external access |
| **ScoutSuite** | Automated AWS security scanning tool |
| **Python (Boto3)** | Scripted review of bucket permissions (sample script included) |

---

## 🔬 Key Findings

| Finding | Description | Severity |
|---|---|---|
| Public S3 Buckets | Multiple S3 buckets allowed **public read access** | 🔴 High |
| Overly Permissive IAM Policies | Some IAM users had **AdministratorAccess** attached directly | 🔴 High |
| Missing S3 Encryption | Several buckets were not encrypted at rest | 🟠 Medium |
| Incomplete CloudTrail Coverage | Not all regions had active trails | 🟠 Medium |
| Root User Without MFA | Root account did not enforce MFA | 🔴 High |
| Stale IAM Keys | Multiple IAM users had access keys older than 90 days | 🟡 Low |

---

## 📂 Files in This Project

| File | Description |
|---|---|
| `aws-audit-report.pdf` | Full security audit report with detailed findings and evidence |
| `aws-cli-commands.txt` | Complete list of AWS CLI commands used to gather evidence |
| `boto3-public-bucket-checker.py` | Python script to programmatically check for public S3 buckets |
| `screenshot-securityhub.png` | Screenshot showing findings in AWS Security Hub dashboard |

---

## 📝 Sample AWS CLI Commands Used

### Review IAM Users and Policies
```bash
aws iam list-users
aws iam list-policies --scope Local
aws iam list-attached-user-policies --user-name ExampleUser

