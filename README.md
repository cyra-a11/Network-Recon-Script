# Network Recon (Python)

A simple command-line tool to:
- Resolve domain ↔ IP
- Check host availability (ping)
- Scan common ports



## Features

- Accepts domain or IP input
- Resolves:
  - Domain → IP
  - IP → Domain (reverse lookup)
- Checks if host is alive using ping
- Scans common ports
- Displays open ports and summary


## Technologies

- Python 3
- socket
- subprocess



## How It Works

1. User inputs a domain or IP
2. Tool resolves domain/IP
3. Sends 1 ping request
4. Scans predefined ports
5. Outputs results



## Usage

```bash
python scanner.py
