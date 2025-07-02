import webbrowser
import pyautogui
import os
import subprocess
import logging
import platform
from colorama import Fore, Style
from config import SCREENSHOTS_FOLDER

logger = logging.getLogger(__name__)

def open_web_page(url: str):
    """Opens a URL in the default web browser."""
    try:
        webbrowser.open(url)
        print(Fore.GREEN + f"Opened web page: {url}")
        logger.info(f"Opened web page: {url}")
    except Exception as e:
        print(Fore.RED + f"Error opening web page '{url}': {e}")
        logger.error(f"Error opening web page '{url}': {e}")

def take_screenshot(filename: str = 'screenshot.png'):
    """Takes a screenshot of the entire screen and saves it."""
    screenshot_path = os.path.join(SCREENSHOTS_FOLDER, filename)
    try:
        pyautogui.screenshot(screenshot_path)
        print(Fore.GREEN + f"Screenshot saved to: {screenshot_path}")
        logger.info(f"Screenshot saved to: {screenshot_path}")
    except Exception as e:
        print(Fore.RED + f"Error taking screenshot: {e}")
        logger.error(f"Error taking screenshot: {e}")

def lock_pc():
    """Locks the Windows PC."""
    if platform.system() == "Windows":
        try:
            # Equivalent to pressing Win + L
            # For Windows, this is the most reliable way to lock the screen programmatically
            subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"], check=True)
            print(Fore.GREEN + "PC locked successfully.")
            logger.info("PC locked.")
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"Error locking PC: {e}")
            logger.error(f"Error locking PC: {e}")
        except FileNotFoundError:
            print(Fore.RED + "Error: 'rundll32.exe' not found. This is a system utility and should be present.")
            logger.error("rundll32.exe not found during PC lock attempt.")
    else:
        print(Fore.YELLOW + "This function is only supported on Windows.")
        logger.warning("Attempted to lock PC on non-Windows OS.")

def shutdown_pc(delay_minutes: int = 0):
    """Shuts down the PC after a specified delay (in minutes)."""
    if platform.system() == "Windows":
        try:
            # `shutdown /s /t N` where N is seconds
            delay_seconds = delay_minutes * 60
            subprocess.run(f"shutdown /s /t {delay_seconds}", shell=True, check=True)
            if delay_seconds > 0:
                print(Fore.GREEN + f"PC will shut down in {delay_minutes} minute(s).")
                logger.info(f"PC scheduled to shut down in {delay_minutes} minute(s).")
            else:
                print(Fore.GREEN + "PC is shutting down immediately.")
                logger.info("PC shutting down immediately.")
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"Error scheduling shutdown: {e}. You might need administrator privileges.")
            logger.error(f"Error scheduling shutdown: {e}")
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred during shutdown attempt: {e}")
            logger.error(f"Unexpected error during shutdown attempt: {e}")
    else:
        print(Fore.YELLOW + "This function is primarily supported on Windows.")
        logger.warning("Attempted to shutdown PC on non-Windows OS.")

def restart_pc(delay_minutes: int = 0):
    """Restarts the PC after a specified delay (in minutes)."""
    if platform.system() == "Windows":
        try:
            # `shutdown /r /t N` where N is seconds
            delay_seconds = delay_minutes * 60
            subprocess.run(f"shutdown /r /t {delay_seconds}", shell=True, check=True)
            if delay_seconds > 0:
                print(Fore.GREEN + f"PC will restart in {delay_minutes} minute(s).")
                logger.info(f"PC scheduled to restart in {delay_minutes} minute(s).")
            else:
                print(Fore.GREEN + "PC is restarting immediately.")
                logger.info("PC restarting immediately.")
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"Error scheduling restart: {e}. You might need administrator privileges.")
            logger.error(f"Error scheduling restart: {e}")
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred during restart attempt: {e}")
            logger.error(f"Unexpected error during restart attempt: {e}")
    else:
        print(Fore.YELLOW + "This function is primarily supported on Windows.")
        logger.warning("Attempted to restart PC on non-Windows OS.")