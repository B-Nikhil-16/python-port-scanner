# Python Port Scanner

A simple TCP port scanner built using Python and the socket module.

## Features
- Scan a single port
- Scan multiple ports using a range
- Resolve domain names to IP addresses
- Detect open TCP ports
- Simple command-line interface

## Technologies Used
- Python 3
- Socket Programming

## How It Works
The program:
1. Accepts an IP address or domain name
2. Accepts a single port or a range of ports
3. Attempts TCP connections to the target ports
4. Displays open ports

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-port-scanner.git
```

Move into the project folder:

```bash
cd python-port-scanner
```

## Usage

Run the script:

```bash
python scanner.py
```

## Example

```text
enter 1. for ip address
2. for domain name
2

enter the website name: google.com

enter
1. for single port
2. for multiple port
2

enter the range(example:1-10): 75-85

Target: 142.250.183.14
ports to scan are 75 , 85

port 80 is open
```

## Project Structure

```text
python-port-scanner/
│
├── scanner.py
└── README.md
```

## Disclaimer

This project is intended for educational purposes and authorized security testing only. Do not scan systems or networks without permission.
