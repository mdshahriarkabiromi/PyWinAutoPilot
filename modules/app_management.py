import subprocess
import os
import psutil
import logging
from colorama import Fore, Style
from config import APP_PATHS

logger = logging.getLogger(__name__)

def open_application(app_name_or_path: str):
    """
    Opens an application. Tries predefined paths first, then as a system command.
    """
    if app_name_or_path.lower() in APP_PATHS:
        full_path = APP_PATHS[app_name_or_path.lower()]
    elif os.path.isfile(app_name_or_path) and app_name_or_path.endswith('.exe'):
        full_path = app_name_or_path
    else:
        full_path = app_name_or_path # Assume it's a command like 'notepad', 'calc'

    try:
        if os.path.exists(full_path) and full_path.endswith('.exe'):
            subprocess.Popen([full_path])
            print(Fore.GREEN + f"Opened application: {full_path}")
            logger.info(f"Opened application: {full_path}")
        else:
            # Try to open as a shell command (e.g., 'notepad', 'calc')
            subprocess.Popen(full_path, shell=True)
            print(Fore.GREEN + f"Attempted to open application/command: {full_path}")
            logger.info(f"Attempted to open application/command: {full_path}")
    except FileNotFoundError:
        print(Fore.RED + f"Error: Application '{app_name_or_path}' not found at '{full_path}'.")
        logger.error(f"Application not found: {app_name_or_path} (resolved to {full_path})")
    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred while opening '{app_name_or_path}': {e}")
        logger.error(f"Error opening application '{app_name_or_path}': {e}")

def close_application(app_name: str):
    """
    Closes an application by its process name (e.g., 'notepad.exe', 'chrome.exe').
    """
    found = False
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == app_name.lower():
            try:
                proc.terminate()
                print(Fore.GREEN + f"Terminated process: {app_name} (PID: {proc.info['pid']})")
                logger.info(f"Terminated process: {app_name} (PID: {proc.info['pid']})")
                found = True
            except psutil.AccessDenied:
                print(Fore.YELLOW + f"Access denied to terminate {app_name} (PID: {proc.info['pid']}). Try running as administrator.")
                logger.warning(f"Access denied to terminate {app_name} (PID: {proc.info['pid']}).")
            except Exception as e:
                print(Fore.RED + f"Error terminating {app_name} (PID: {proc.info['pid']}): {e}")
                logger.error(f"Error terminating {app_name} (PID: {proc.info['pid']}): {e}")
    if not found:
        print(Fore.YELLOW + f"No running process found with name: {app_name}")
        logger.info(f"No process found with name: {app_name}")

def list_running_processes():
    """Lists all currently running processes."""
    print(Fore.CYAN + "\n--- Running Processes ---")
    logger.info("Listing running processes.")
    try:
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                pinfo = proc.info
                print(Fore.WHITE + f"PID: {pinfo['pid']}, Name: {pinfo['name']}, Status: {pinfo['status']}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        print(Fore.CYAN + "-------------------------\n")
    except Exception as e:
        print(Fore.RED + f"Error listing processes: {e}")
        logger.error(f"Error listing processes: {e}")