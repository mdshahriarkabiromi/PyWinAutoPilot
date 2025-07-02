# PyWinAutoPilot 🚀

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![OS Compatibility](https://img.shields.io/badge/OS-Windows-success?style=flat-square&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
  - [Configuration](#configuration)
  - [Running with Administrator Privileges (Optional but Recommended)](#running-with-administrator-privileges-optional-but-recommended)
- [Usage](#usage)
  - [Running the Main Script](#running-the-main-script)
  - [Using the Batch File](#using-the-batch-file)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview

`PyWinAutoPilot` is a lightweight, Python-based automation tool designed to streamline various common and repetitive tasks on the Windows operating system. From managing files and applications to simulating user interface interactions, this project aims to boost your productivity by automating mundane digital chores.

Built with modularity in mind, `PyWinAutoPilot` provides a command-line interface that allows users to select and execute automation routines for a range of daily activities.

## Features

`PyWinAutoPilot` currently offers the following core functionalities:

### 📁 File Operations
* **Create Folder:** Quickly create new directories.
* **Delete File:** Remove unwanted files.
* **Move File:** Relocate files from one directory to another.
* **Copy File:** Duplicate files to a specified destination.
* **Empty Folder:** Clear all contents (files and subfolders) from a directory.
* **Organize Downloads:** Automatically sort files in your downloads folder into categorized subfolders (e.g., Images, Documents, Videos, Archives).

### 🖥️ Application Management
* **Open Application:** Launch applications by name or full path.
* **Close Application:** Terminate running applications by their process name.
* **List Running Processes:** View all active processes on your system.

### ⚙️ System Utilities
* **Open Web Page:** Launch any URL in your default web browser.
* **Take Screenshot:** Capture a full-screen screenshot and save it.
* **Lock PC:** Instantly lock your computer screen.
* *(Optional: Shutdown/Restart PC with delay - uncomment in `main.py` and `system_utilities.py` for this functionality)*

### 🖱️⌨️ UI Automation (Mouse & Keyboard)
* **Click at Coordinates:** Simulate mouse clicks at specific screen positions.
* **Type Text:** Automate typing text into active windows.
* **Press Key:** Simulate pressing individual keyboard keys (e.g., `Enter`, `Esc`).
* **Perform Hotkey:** Execute common hotkey combinations (e.g., `Ctrl+C`, `Alt+F4`).
* **Copy to Clipboard:** Place text onto the system clipboard.
* **Paste from Clipboard:** Retrieve and display text from the system clipboard.

*(Future Feature: 🌐 Web Automation - planned integration with Selenium for browser-based tasks)*

## Installation

### Prerequisites

* **Operating System:** Windows 10/11
* **Python:** Version 3.8 or higher.
    * Download from [python.org](https://www.python.org/downloads/windows/).
    * **Crucially, ensure "Add Python to PATH" is checked during installation.**

### Clone the Repository

First, clone the PyWinAutoPilot repository to your local machine using Git:

```bash
git clone [https://github.com/mdshahriarkabiromi/PyWinAutoPilot.git](https://github.com/mdshahriarkabiromi/PyWinAutoPilot.git)
cd PyWinAutoPilot

Install Dependencies
Navigate into the cloned directory and install the required Python libraries. It's highly recommended to use a virtual environment for dependency management.

Bash

# Create a virtual environment (optional, but good practice)
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS (if you ever run on those, though this project is Windows-specific):
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
Configuration
Before running, you must customize the config.py file to match your system's paths and preferences.

Open config.py and update the following variables:

DOWNLOADS_FOLDER: Set this to your actual Downloads directory (e.g., C:\\Users\\YourUser\\Downloads or E:\\YourUser\\Downloads).

SCREENSHOTS_FOLDER: Define where screenshots will be saved.

APP_PATHS: Add or modify paths for frequently used applications on your system (e.g., chrome, notepad).

Python

# config.py example
DOWNLOADS_FOLDER = r'C:\Users\YourUser\Downloads' # Update this!
SCREENSHOTS_FOLDER = r'C:\Users\YourUser\Pictures\PyWinAutoPilot_Screenshots' # Update this!

APP_PATHS = {
    'notepad': 'notepad.exe',
    'chrome': r'C:\Program Files\Google\Chrome\Application\chrome.exe', # Verify this path for your system
    # Add more apps here

Running with Administrator Privileges (Optional but Recommended)
Some tasks (like closing certain applications, moving system-protected files, or advanced system utilities) may require elevated permissions. To avoid PermissionError issues, it's recommended to run PyWinAutoPilot as an administrator:

Via Command Prompt/Terminal: Open cmd.exe or Windows Terminal by right-clicking its icon and selecting "Run as administrator". Then, navigate to your PyWinAutoPilot directory and run the script.

Via Batch File: Create a .bat file (see Usage section below) and right-click it, then select "Run as administrator".

Usage
Running the Main Script
Once configured, you can run the application by executing main.py:

Bash

# Ensure your virtual environment is activated if you created one
python main.py
The application will present an interactive command-line menu. Follow the prompts to select and execute the desired automation tasks.

Using the Batch File
For convenience, you can use the provided run_PyWinAutoPilot.bat file to start the application with a double-click. Ensure this file is located in the root of your PyWinAutoPilot directory.

run_PyWinAutoPilot.bat:

Code snippet

@echo off
rem Change directory to where the script is located
cd /d "%~dp0"

echo Starting PyWinAutoPilot...
rem Use 'python' if it's in your system PATH, otherwise use the full path to python.exe
python main.py
rem "C:\Users\YourUser\AppData\Local\Programs\Python\Python313\python.exe" main.py

echo.
echo PyWinAutoPilot finished. Press any key to exit.
pause > nul
exit /b 0
(Remember to uncomment and update the full path to python.exe if python is not in your system's PATH.)

Project Structure
PyWinAutoPilot/
├── main.py                     # Main application entry point, menu handling
├── config.py                   # Configuration settings (paths, app settings)
├── modules/
│   ├── file_operations.py      # Functions for file and folder management
│   ├── app_management.py       # Functions for managing applications (open, close)
│   ├── system_utilities.py     # Functions for system-level tasks (screenshot, lock PC, web)
│   ├── ui_automation.py        # Functions for simulating mouse and keyboard interactions
│   └── web_automation.py       # (Optional) Functions for browser automation using Selenium
├── logs/
│   └── automation.log          # Application logs for debugging and history
├── data/
│   └── shortcuts.json          # (Example) For storing custom shortcuts or data
├── requirements.txt            # List of required Python packages
├── run_PyWinAutoPilot.bat      # Convenience batch file to run the script
└── README.md                   # Project documentation (this file)
└── .gitignore                  # Specifies intentionally untracked files to ignore by Git
Troubleshooting
PermissionError: [WinError 5] Access is denied / [Errno 13] Permission denied:

This is common for protected files or directories. Try running the script or the .bat file as Administrator.

Ensure the file/folder isn't currently open or in use by another application.

Check your antivirus software; it might be blocking the operation.

python: command not found / Python not running from .bat file:

Ensure Python is correctly installed and its path is added to your system's environment variables.

Alternatively, modify run_PyWinAutoPilot.bat to use the full path to your python.exe (e.g., "C:\Path\To\Python\python.exe" main.py).

AttributeError: module 'modules.file_operations' has no attribute 'create_folder':

This typically means file_operations.py either doesn't have the create_folder function defined or an old .pyc cached version of the module is being loaded.

Solution: Double-check modules/file_operations.py to ensure the function exists. Then, delete the __pycache__ folder within the modules directory and any .pyc files, then restart your terminal/IDE.

Contributing
Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

Fork the repository.

Create a new branch for your feature or bug fix (git checkout -b feature/your-feature-name or git checkout -b bugfix/fix-issue-name).

Make your changes and test them thoroughly.

Commit your changes with clear, concise commit messages.

Push your branch to your forked repository.

Open a Pull Request against the main branch of this repository, describing your changes in detail.

License
This project is licensed under the MIT License - see the LICENSE file

Contact
If you have any questions, feedback, or need assistance, feel free to open an issue on the GitHub repository or contact the project maintainer:

Your Name/Alias: Shahriar

GitHub Profile: https://github.com/mdshahriarkabiromi