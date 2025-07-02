import os
import logging
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# Import modules
from config import LOG_FILE, APP_PATHS
from modules import file_operations, app_management, system_utilities, ui_automation
# from modules import web_automation # Uncomment if you include web_automation

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename=LOG_FILE,
                    filemode='a') # 'a' for append, so it doesn't overwrite
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

# --- Main Menu Functions ---

def display_main_menu():
    """Displays the main menu options to the user."""
    print(Fore.CYAN + Style.BRIGHT + "\n--- PyWinAutoPilot Main Menu ---")
    print(Fore.YELLOW + "1. File Operations")
    print(Fore.YELLOW + "2. Application Management")
    print(Fore.YELLOW + "3. System Utilities")
    print(Fore.YELLOW + "4. UI Automation (Mouse & Keyboard)")
    # print(Fore.YELLOW + "5. Web Automation (Requires Selenium)") # Uncomment if included
    print(Fore.RED + "0. Exit")
    print(Fore.CYAN + "--------------------------------")

def handle_file_operations():
    """Handles the file operations sub-menu."""
    while True:
        print(Fore.GREEN + "\n--- File Operations ---")
        print(Fore.YELLOW + "1. Create Folder")
        print(Fore.YELLOW + "2. Delete File")
        print(Fore.YELLOW + "3. Move File")
        print(Fore.YELLOW + "4. Copy File")
        print(Fore.YELLOW + "5. Empty Folder")
        print(Fore.YELLOW + "6. Organize Downloads Folder (Basic)")
        print(Fore.BLUE + "0. Back to Main Menu")
        choice = input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL)

        if choice == '1':
            path = input("Enter path where to create folder: ")
            name = input("Enter new folder name: ")
            file_operations.create_folder(path, name)
        elif choice == '2':
            path = input("Enter full path of file to delete: ")
            file_operations.delete_file(path)
        elif choice == '3':
            source = input("Enter source file path: ")
            destination = input("Enter destination folder path: ")
            file_operations.move_file(source, destination)
        elif choice == '4':
            source = input("Enter source file path: ")
            destination = input("Enter destination folder path: ")
            file_operations.copy_file(source, destination)
        elif choice == '5':
            path = input("Enter path of folder to empty: ")
            file_operations.empty_folder(path)
        elif choice == '6':
            download_path = input("Enter your downloads folder path (e.g., C:\\Users\\YourUser\\Downloads): ")
            file_operations.organize_downloads(download_path)
        elif choice == '0':
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
        input(Fore.BLUE + "Press Enter to continue...")


def handle_app_management():
    """Handles the application management sub-menu."""
    while True:
        print(Fore.GREEN + "\n--- Application Management ---")
        print(Fore.YELLOW + "1. Open Application")
        print(Fore.YELLOW + "2. Close Application (by name)")
        print(Fore.YELLOW + "3. List Running Processes")
        print(Fore.BLUE + "0. Back to Main Menu")
        choice = input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL)

        if choice == '1':
            app_name = input("Enter application name (e.g., 'notepad', 'chrome') or full path: ")
            app_management.open_application(app_name)
        elif choice == '2':
            app_name = input("Enter application name to close (e.g., 'notepad.exe'): ")
            app_management.close_application(app_name)
        elif choice == '3':
            app_management.list_running_processes()
        elif choice == '0':
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
        input(Fore.BLUE + "Press Enter to continue...")

def handle_system_utilities():
    """Handles the system utilities sub-menu."""
    while True:
        print(Fore.GREEN + "\n--- System Utilities ---")
        print(Fore.YELLOW + "1. Open Web Page")
        print(Fore.YELLOW + "2. Take Screenshot")
        print(Fore.YELLOW + "3. Lock PC")
        # print(Fore.YELLOW + "4. Shutdown PC (Warning: Immediate!)") # Use with caution
        # print(Fore.YELLOW + "5. Restart PC (Warning: Immediate!)") # Use with caution
        print(Fore.BLUE + "0. Back to Main Menu")
        choice = input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL)

        if choice == '1':
            url = input("Enter URL to open: ")
            system_utilities.open_web_page(url)
        elif choice == '2':
            filename = input("Enter filename for screenshot (e.g., 'desktop_capture.png'): ")
            system_utilities.take_screenshot(filename)
        elif choice == '3':
            system_utilities.lock_pc()
        # elif choice == '4':
        #     confirm = input(Fore.RED + "WARNING: This will immediately shutdown your PC. Type 'yes' to confirm: " + Style.RESET_ALL)
        #     if confirm.lower() == 'yes':
        #         system_utilities.shutdown_pc(delay_minutes=0) # Immediate shutdown
        #     else:
        #         print("Shutdown cancelled.")
        # elif choice == '5':
        #     confirm = input(Fore.RED + "WARNING: This will immediately restart your PC. Type 'yes' to confirm: " + Style.RESET_ALL)
        #     if confirm.lower() == 'yes':
        #         system_utilities.restart_pc(delay_minutes=0) # Immediate restart
        #     else:
        #         print("Restart cancelled.")
        elif choice == '0':
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
        input(Fore.BLUE + "Press Enter to continue...")

def handle_ui_automation():
    """Handles the UI automation sub-menu."""
    while True:
        print(Fore.GREEN + "\n--- UI Automation (Mouse & Keyboard) ---")
        print(Fore.YELLOW + "1. Click at Coordinates")
        print(Fore.YELLOW + "2. Type Text")
        print(Fore.YELLOW + "3. Press Key")
        print(Fore.YELLOW + "4. Perform Hotkey (e.g., Ctrl+C)")
        print(Fore.YELLOW + "5. Copy to Clipboard")
        print(Fore.YELLOW + "6. Paste from Clipboard")
        print(Fore.BLUE + "0. Back to Main Menu")
        choice = input(Fore.MAGENTA + "Enter your choice: " + Style.RESET_ALL)

        if choice == '1':
            try:
                x = int(input("Enter X coordinate: "))
                y = int(input("Enter Y coordinate: "))
                ui_automation.click_at_coordinates(x, y)
                print(Fore.GREEN + "Click performed.")
            except ValueError:
                print(Fore.RED + "Invalid coordinates. Please enter numbers.")
        elif choice == '2':
            text = input("Enter text to type: ")
            delay = float(input("Enter delay between characters (e.g., 0.1): ") or 0.1)
            ui_automation.type_text(text, delay)
            print(Fore.GREEN + "Text typed.")
        elif choice == '3':
            key = input("Enter key to press (e.g., 'enter', 'esc', 'space'): ")
            ui_automation.press_key(key)
            print(Fore.GREEN + f"Key '{key}' pressed.")
        elif choice == '4':
            keys_str = input("Enter hotkeys separated by comma (e.g., 'ctrl,c', 'alt,f4'): ")
            keys = [k.strip() for k in keys_str.split(',')]
            ui_automation.hotkey(keys)
            print(Fore.GREEN + f"Hotkey '{keys_str}' performed.")
        elif choice == '5':
            text = input("Enter text to copy to clipboard: ")
            ui_automation.copy_to_clipboard(text)
            print(Fore.GREEN + "Text copied to clipboard.")
        elif choice == '6':
            pasted_text = ui_automation.paste_from_clipboard()
            if pasted_text:
                print(Fore.GREEN + f"Text pasted from clipboard: {pasted_text}")
            else:
                print(Fore.YELLOW + "Clipboard is empty or text could not be retrieved.")
        elif choice == '0':
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
        input(Fore.BLUE + "Press Enter to continue...")

# def handle_web_automation():
#     """Handles the web automation sub-menu."""
#     print(Fore.YELLOW + "\nWeb Automation functionalities will go here.")
#     print(Fore.YELLOW + "Remember to download a browser driver (e.g., ChromeDriver) and place it in your system's PATH.")
#     # Example:
#     # driver_path = input("Enter path to your browser driver (e.g., C:\\WebDriver\\chromedriver.exe): ")
#     # url = input("Enter URL to open: ")
#     # web_automation.open_browser(url, driver_path)
#     input(Fore.BLUE + "Press Enter to continue...")

# --- Main Program Loop ---

def main():
    """Main function to run the PyWinAutoPilot application."""
    logging.info("PyWinAutoPilot started.")
    while True:
        display_main_menu()
        choice = input(Fore.MAGENTA + "Enter your main menu choice: " + Style.RESET_ALL)

        if choice == '1':
            handle_file_operations()
        elif choice == '2':
            handle_app_management()
        elif choice == '3':
            handle_system_utilities()
        elif choice == '4':
            handle_ui_automation()
        # elif choice == '5': # Uncomment if you include web_automation
        #     handle_web_automation()
        elif choice == '0':
            print(Fore.GREEN + "Exiting PyWinAutoPilot. Goodbye!")
            logging.info("PyWinAutoPilot exited.")
            break
        else:
            print(Fore.RED + "Invalid main menu choice. Please try again.")
            logging.warning(f"Invalid main menu choice: {choice}")
        input(Fore.BLUE + "Press Enter to return to main menu...")


if __name__ == "__main__":
    main()