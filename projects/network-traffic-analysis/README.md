# Network Traffic Analysis Project

## 📄 Project Overview

This project involved capturing and analyzing network traffic to identify potential security threats, anomalies, and vulnerabilities. The goal was to understand common network protocols, detect suspicious patterns, and practice **packet analysis** using Wireshark.

---

## 🎯 Objectives

- Capture live network traffic from a simulated environment.
- Identify and analyze normal vs suspicious traffic.
- Detect evidence of reconnaissance, unauthorized access, or data exfiltration.
- Generate a comprehensive analysis report with findings and recommendations.

---

## 🔧 Tools & Technologies Used

| Tool/Technology | Purpose |
|---|---|
| **Wireshark** | Network traffic capture and analysis |
| **Kali Linux** | Simulated attack traffic (port scans, brute force attempts) |
| **Nmap** | Network scanning to simulate external attacks |
| **Scapy (Python)** | Custom packet crafting (optional) |

---

## 📊 Key Findings

| Observation | Description |
|---|---|
| 🔍 **Port Scanning Detected** | Nmap scans from external IPs indicating reconnaissance activity. |
| 🔓 **Unencrypted HTTP Traffic** | Sensitive data transmitted over plaintext HTTP, vulnerable to interception. |
| 🕵️‍♂️ **Brute Force Attempts** | Repeated failed login attempts on SSH and web login pages. |
| 📡 **Suspicious DNS Queries** | High volume of outbound DNS requests from a single internal IP, possibly indicating data exfiltration. |

---

## 📂 Files in This Project

| File | Description |
|---|---|
| `wireshark-analysis-report.pdf` | Full PDF report detailing traffic analysis, findings, and recommendations. |
| `traffic-sample.pcap` | Captured network traffic in PCAP format (can be opened with Wireshark). |
| `screenshot.png` | Screenshot of captured suspicious packets in Wireshark. |

---

## 📸 Sample Screenshot

![Wireshark Screenshot](screenshot.png)

---

## 📄 Sample Analysis Process

### 1. Capture Traffic
```bash
sudo tcpdump -i eth0 -w traffic-sample.pcap

