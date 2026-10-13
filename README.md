# Fire TV Web Remote

A custom, web-based remote control for an Amazon Fire TV Stick, built using Python, Flask, and Android Debug Bridge (ADB).

## Project Overview

This project allows me to control my Fire TV Stick through a web browser using a remote interface hosted on a Linux Mint laptop.

I started this project as a way to gain hands-on experience with Python, Linux, networking, and troubleshooting while building something useful for everyday use.

## Technologies Used

- **Python** — Application logic
- **Flask** — Web interface and HTTP requests
- **ADB (Android Debug Bridge)** — Communication with the Fire TV Stick
- **Linux Mint** — Host operating system
- **HTML/CSS** — Remote interface
- **Local networking** — Communication between devices

## How It Works

1. A Python Flask application runs on the Linux laptop.
2. A device on the same local network opens the remote's web interface.
3. The application sends commands to the Fire TV Stick through ADB.
4. The Fire TV Stick responds to those commands.

## Running the Project

The application requires Python, Flask, ADB, and a compatible Fire TV device with ADB debugging enabled.

The Fire TV's network address must be configured in the application before use.

The Flask application can then be started with:

```bash
python3 app.py
```

The web interface is accessed through the host computer's IP address and the application's configured port.

## Project Status

**Work in progress**

The remote is functional, but I am continuing to test, troubleshoot, and improve its features and interface.

## What I'm Learning

- Python application development
- Linux terminal commands
- Network connectivity and IP addressing
- Device communication using ADB
- Web-based user interfaces
- Troubleshooting and iterative development

## Future Improvements

- Improve the remote interface
- Add additional controls and functionality
- Improve connection handling
- Continue testing across devices

## Disclaimer

This is a personal educational project and is not affiliated with or endorsed by Amazon.
