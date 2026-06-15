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

Run the tool from your terminal:

```bash
python scanner.py
```
Then Type:
```
example.com
```



## Example Output

--- Scan Result ---
Target: example.com
Domain: example.com
IP: 93.184.216.34
Ping: host is alive
Ports scanned: 12
Open ports: 2
Open port list: [80, 443]

## Limitations

No threading (slow scanning)
Fixed port list
Minimal error handling
Future Improvements
Custom port range
Multi-threaded scanning
Better input validation
Service detection (banner grabbing)
Disclaimer

This tool is for educational purposes only.
Do not scan systems without permission.
