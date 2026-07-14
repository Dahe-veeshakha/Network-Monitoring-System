# Network Monitoring System

> An intelligent Python-based Network Monitoring and Device Discovery Framework designed for Raspberry Pi and Linux environments.

![Status](https://img.shields.io/badge/Status-Active%20Development-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%20%7C%20Linux-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Overview

Network Monitoring System is a Python-based framework that continuously discovers, identifies, and monitors devices connected to a local network.

The system combines passive packet analysis with active network discovery techniques to maintain an up-to-date inventory of network devices. It records device information such as MAC address, IP address, vendor, status, and discovery confidence while storing monitoring data in an SQLite database for future analysis.

The framework is designed primarily for Raspberry Pi and Linux-based deployments, making it suitable for lightweight network monitoring in home labs, educational environments, and small to medium-sized enterprise networks.

---

## Key Features

- Passive Network Discovery using Scapy
- Active ARP Network Scanning
- Nmap Host Discovery
- Device Fingerprinting
- MAC Address-Based Device Tracking
- Vendor Identification
- Multi-threaded Discovery Engine
- Confidence-Based Device Detection
- Online, Pending, and Offline Status Monitoring
- SQLite Database Logging
- CSV Export Support
- Rich Terminal Dashboard
- Raspberry Pi Compatible

---

## Technology Stack

- Python 3
- Scapy
- Rich
- SQLite
- Requests
- Nmap
- SNMP
- Raspberry Pi OS
- Linux

---

## Project Structure

```text
Network-Monitoring-System/

├── src/
├── docs/
├── database/
├── screenshots/
├── logs/

├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## Current Development Status

The project is currently under active development.

### Completed

- Passive Device Discovery
- Active Network Scanning
- Device Fingerprinting
- Rich Terminal Dashboard
- SQLite Database Integration
- Multi-threaded Device Monitoring

### Planned Features

- Configuration Management
- VLAN Discovery
- Alert & Notification Engine
- Performance Optimization
- Web Dashboard
- Remote Monitoring Support

---

## Installation

```bash
git clone https://github.com/Dahe-veeshakha/Network-Monitoring-System.git

cd Network-Monitoring-System

pip install -r requirements.txt
```

---

## Requirements

- Python 3.10 or later
- Raspberry Pi OS or Linux
- Nmap
- Scapy
- Root/Sudo privileges for packet capture

---

## Future Roadmap

- Web-based Monitoring Dashboard
- Device Classification Improvements
- Configuration File Support
- Email & Telegram Alerts
- Historical Analytics
- Performance Enhancements

---

## Screenshots

Project screenshots will be added after validation on Raspberry Pi hardware.

---

## License

This project is licensed under the MIT License.

---

## Author

**Veeshakha Dahe**

Cybersecurity | Network Security | Python | Linux | Raspberry Pi

---

> **Note:** This project is under continuous development, and new features and improvements are actively being implemented.
