import os

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Ensure logs and data directories exist
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, 'automation.log')

# --- Default Directories ---
# Customize these to your actual paths
DOWNLOADS_FOLDER = os.path.join(os.path.expanduser('~'), 'Downloads')
SCREENSHOTS_FOLDER = os.path.join(os.path.expanduser('~'), 'Pictures', 'PyWinAutoPilot_Screenshots')
os.makedirs(SCREENSHOTS_FOLDER, exist_ok=True) # Ensure screenshots folder exists

# --- Application Paths (Examples - Customize for your system) ---
APP_PATHS = {
    'notepad': 'notepad.exe',
    'chrome': r'C:\Program Files\Google\Chrome\Application\chrome.exe', # Example path, verify yours
    'calculator': 'calc.exe',
    # Add more frequently used applications here
}

# --- UI Automation Settings ---
DEFAULT_TYPING_DELAY = 0.05 # Delay between characters when typing
DEFAULT_MOUSE_DELAY = 0.1   # Delay after mouse actions

# --- Web Automation Settings (if using Selenium) ---
# CHROMEDRIVER_PATH = r'C:\path\to\your\chromedriver.exe' # Specify path to your browser driver

# --- Web Automation Settings (if using Selenium) ---
# CHROMEDRIVER_PATH = r'C:\path\to\your\chromedriver.exe' # Specify path to your browser driver

# --- Web Automation Settings (if using Selenium) ---
# CHROMEDRIVER_PATH = r'C:\path\to\your\chromedriver.exe' # Specify path to your browser driver