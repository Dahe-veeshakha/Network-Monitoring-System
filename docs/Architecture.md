# Network Monitoring System Architecture

## Overview

The Network Monitoring System is designed to discover, identify, and monitor devices connected to a local network.

The framework combines passive packet monitoring with active network scanning to maintain an up-to-date inventory of network devices.

---

## Core Components

- Passive Discovery Engine
- Active Discovery Engine
- Device Fingerprinting
- Status Detection
- SQLite Database
- Rich Terminal Dashboard

---

## Discovery Workflow

Passive Monitoring
        ↓
New Device Detected
        ↓
Active Verification
        ↓
Fingerprint Collection
        ↓
SQLite Storage
        ↓
Live Dashboard Update

---

## Technologies

- Python
- Scapy
- SQLite
- Rich
- Requests
- Nmap
- SNMP
