# Penetration Testing Project - Vulnerable Web Application

## 📄 Project Overview

This project simulates a **penetration test** on a deliberately vulnerable web application. The goal was to identify, exploit, and document security vulnerabilities using a combination of automated and manual techniques.

---

## 🔧 Tools Used

- **Nmap** - Initial port scanning
- **Dirbuster** - Directory brute force
- **SQLmap** - SQL Injection testing
- **Burp Suite** - Manual web app analysis
- **Metasploit** - Exploitation framework

---

## 🔬 Key Findings

- ✅ SQL Injection Vulnerability - Authentication Bypass
- ✅ Exposed Directories - `/admin`, `/backup`, `/uploads`
- ✅ Outdated CMS Plugin - Remote Code Execution

---

## 📂 Files

| File | Description |
|---|---|
| `webapp-pentest-report.pdf` | Detailed penetration testing report |
| `metasploit-scan.sh` | Automated Metasploit scanning script |
| `sql_injection_test.py` | Custom SQL injection testing script |
| `dirbuster_scan.txt` | Sample output from directory enumeration |

---

## 📸 Sample Screenshot

![Burp Suite Screenshot](../screenshots/burp-sql-injection.png)

---

## 📄 Sample Commands

### Nmap Scan
```bash
nmap -sC -sV -oN initial_scan.txt 192.168.1.100

