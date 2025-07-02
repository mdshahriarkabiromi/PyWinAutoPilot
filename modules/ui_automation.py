import pyautogui
import pyperclip
import time
import logging
from colorama import Fore, Style
from config import DEFAULT_TYPING_DELAY, DEFAULT_MOUSE_DELAY

logger = logging.getLogger(__name__)

# Configure PyAutoGUI fail-safe and pause
pyautogui.FAILSAFE = True  # Move mouse to top-left corner to abort script
pyautogui.PAUSE = 0.5      # Pause after each PyAutoGUI call by default

def click_at_coordinates(x: int, y: int, button: str = 'left'):
    """Clicks the mouse at specified (x, y) coordinates."""
    try:
        pyautogui.click(x=x, y=y, button=button)
        print(Fore.GREEN + f"Clicked {button} mouse button at ({x}, {y}).")
        logger.info(f"Clicked {button} mouse button at ({x}, {y}).")
        time.sleep(DEFAULT_MOUSE_DELAY)
    except Exception as e:
        print(Fore.RED + f"Error clicking at ({x}, {y}): {e}")
        logger.error(f"Error clicking at ({x}, {y}): {e}")

def type_text(text: str, delay: float = DEFAULT_TYPING_DELAY):
    """Types the given text using keyboard simulation."""
    try:
        pyautogui.write(text, interval=delay)
        print(Fore.GREEN + f"Typed text: '{text[:20]}...' (truncated for display)")
        logger.info(f"Typed text: '{text}' with delay {delay}.")
    except Exception as e:
        print(Fore.RED + f"Error typing text: {e}")
        logger.error(f"Error typing text: {e}")

def press_key(key: str):
    """Presses a single keyboard key (e.g., 'enter', 'esc', 'tab')."""
    try:
        pyautogui.press(key)
        print(Fore.GREEN + f"Pressed key: '{key}'.")
        logger.info(f"Pressed key: '{key}'.")
        time.sleep(DEFAULT_MOUSE_DELAY) # Small pause after key press
    except Exception as e:
        print(Fore.RED + f"Error pressing key '{key}': {e}")
        logger.error(f"Error pressing key '{key}': {e}")

def hotkey(keys: list):
    """Performs a hotkey combination (e.g., ['ctrl', 'c'], ['alt', 'f4'])."""
    try:
        pyautogui.hotkey(*keys)
        print(Fore.GREEN + f"Performed hotkey: {', '.join(keys)}.")
        logger.info(f"Performed hotkey: {', '.join(keys)}.")
        time.sleep(DEFAULT_MOUSE_DELAY) # Small pause after hotkey
    except Exception as e:
        print(Fore.RED + f"Error performing hotkey {keys}: {e}")
        logger.error(f"Error performing hotkey {keys}: {e}")

def copy_to_clipboard(text: str):
    """Copies text to the system clipboard."""
    try:
        pyperclip.copy(text)
        print(Fore.GREEN + f"Copied to clipboard: '{text[:20]}...'")
        logger.info(f"Copied to clipboard: '{text}'.")
    except Exception as e:
        print(Fore.RED + f"Error copying to clipboard: {e}")
        logger.error(f"Error copying to clipboard: {e}")

def paste_from_clipboard() -> str:
    """Pastes text from the system clipboard and returns it."""
    try:
        text = pyperclip.paste()
        if text:
            print(Fore.GREEN + f"Pasted from clipboard: '{text[:20]}...'")
            logger.info(f"Pasted from clipboard: '{text}'.")
            return text
        else:
            print(Fore.YELLOW + "Clipboard is empty.")
            logger.warning("Attempted to paste from an empty clipboard.")
            return ""
    except Exception as e:
        print(Fore.RED + f"Error pasting from clipboard: {e}")
        logger.error(f"Error pasting from clipboard: {e}")
        return ""

# You can add more advanced UI automation functions here, like:
# - find_image_on_screen(image_path, confidence=0.9)
# - drag_and_drop(start_x, start_y, end_x, end_y)
# - scroll(clicks)