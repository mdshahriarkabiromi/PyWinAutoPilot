import os
import shutil
import logging
from pathlib import Path
from collections import defaultdict
from colorama import Fore, Style

logger = logging.getLogger(__name__)

def create_folder(path: str, name: str):
    """Creates a new folder at the specified path."""
    full_path = os.path.join(path, name)
    try:
        os.makedirs(full_path, exist_ok=True)
        print(Fore.GREEN + f"Folder '{name}' created successfully at '{path}'.")
        logger.info(f"Folder '{name}' created at '{path}'.")
    except OSError as e:
        print(Fore.RED + f"Error creating folder '{name}': {e}")
        logger.error(f"Error creating folder '{name}' at '{path}': {e}")

def delete_file(file_path: str):
    """Deletes a file at the specified path."""
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(Fore.GREEN + f"File '{file_path}' deleted successfully.")
            logger.info(f"File '{file_path}' deleted.")
        else:
            print(Fore.YELLOW + f"File '{file_path}' not found.")
            logger.warning(f"Attempted to delete non-existent file: {file_path}")
    except OSError as e:
        print(Fore.RED + f"Error deleting file '{file_path}': {e}")
        logger.error(f"Error deleting file '{file_path}': {e}")

def move_file(source_path: str, destination_folder: str):
    """Moves a file from source to destination folder."""
    try:
        if os.path.isfile(source_path):
            shutil.move(source_path, destination_folder)
            print(Fore.GREEN + f"File '{source_path}' moved to '{destination_folder}'.")
            logger.info(f"File '{source_path}' moved to '{destination_folder}'.")
        else:
            print(Fore.YELLOW + f"Source file '{source_path}' not found.")
            logger.warning(f"Attempted to move non-existent source file: {source_path}")
    except FileNotFoundError:
        print(Fore.RED + f"Error: Source file '{source_path}' or destination folder '{destination_folder}' not found.")
        logger.error(f"File not found during move operation: Source={source_path}, Dest={destination_folder}")
    except shutil.Error as e:
        print(Fore.RED + f"Error moving file '{source_path}': {e}")
        logger.error(f"Error moving file '{source_path}' to '{destination_folder}': {e}")

def copy_file(source_path: str, destination_folder: str):
    """Copies a file from source to destination folder."""
    try:
        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_folder) # copy2 preserves metadata
            print(Fore.GREEN + f"File '{source_path}' copied to '{destination_folder}'.")
            logger.info(f"File '{source_path}' copied to '{destination_folder}'.")
        else:
            print(Fore.YELLOW + f"Source file '{source_path}' not found.")
            logger.warning(f"Attempted to copy non-existent source file: {source_path}")
    except FileNotFoundError:
        print(Fore.RED + f"Error: Source file '{source_path}' or destination folder '{destination_folder}' not found.")
        logger.error(f"File not found during copy operation: Source={source_path}, Dest={destination_folder}")
    except shutil.Error as e:
        print(Fore.RED + f"Error copying file '{source_path}': {e}")
        logger.error(f"Error copying file '{source_path}' to '{destination_folder}': {e}")

def empty_folder(folder_path: str):
    """Deletes all contents (files and subfolders) within a given folder."""
    try:
        if not os.path.isdir(folder_path):
            print(Fore.YELLOW + f"Folder '{folder_path}' does not exist.")
            logger.warning(f"Attempted to empty non-existent folder: {folder_path}")
            return

        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.remove(item_path)
                    print(Fore.GREEN + f"Deleted file: {item_path}")
                    logger.info(f"Deleted file: {item_path}")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(Fore.GREEN + f"Deleted folder: {item_path}")
                    logger.info(f"Deleted folder: {item_path}")
            except OSError as e:
                print(Fore.RED + f"Error deleting '{item_path}': {e}")
                logger.error(f"Error deleting '{item_path}' while emptying '{folder_path}': {e}")
        print(Fore.GREEN + f"Folder '{folder_path}' contents emptied successfully.")
        logger.info(f"Contents of folder '{folder_path}' emptied.")

    except OSError as e:
        print(Fore.RED + f"Error accessing folder '{folder_path}': {e}")
        logger.error(f"Error accessing folder '{folder_path}' for emptying: {e}")

def organize_downloads(download_folder: str):
    """
    Organizes files in the downloads folder into subfolders based on file extension.
    Recognized categories: Images, Documents, Videos, Audio, Archives, Executables, Others.
    """
    if not os.path.isdir(download_folder):
        print(Fore.RED + f"Error: Downloads folder '{download_folder}' not found.")
        logger.error(f"Downloads folder not found for organization: {download_folder}")
        return

    print(Fore.CYAN + f"\nOrganizing downloads in: {download_folder}")
    logger.info(f"Starting download organization for: {download_folder}")

    categories = {
        'Images': ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.ico'), # Added .ico
        'Documents': ('.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.txt', '.rtf', '.odt', '.csv', '.xml'), # Added .csv, .xml
        'Videos': ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv'),
        'Audio': ('.mp3', '.wav', '.flac', '.aac'),
        'Archives': ('.zip', '.rar', '.7z', '.tar', '.gz'),
        'Executables': ('.exe', '.msi', '.bat', '.cmd'), # Added .bat, .cmd
        'Others': () # Catch-all for files that don't fit
    }

    files_moved = defaultdict(int)
    files_skipped_permission = 0
    files_skipped_other_error = 0
    files_skipped_non_file = 0 # For directories

    for item in os.listdir(download_folder):
        item_path = os.path.join(download_folder, item)
        
        if os.path.isfile(item_path):
            file_extension = Path(item).suffix.lower()
            moved = False
            
            target_category = 'Others' # Default category if no specific match

            for category, extensions in categories.items():
                if file_extension in extensions:
                    target_category = category
                    break # Found a category, no need to check others

            dest_dir = os.path.join(download_folder, target_category)
            os.makedirs(dest_dir, exist_ok=True) # Ensure destination category folder exists

            try:
                shutil.move(item_path, dest_dir)
                print(Fore.GREEN + f"Moved '{item}' to '{target_category}' folder.")
                logger.info(f"Moved '{item}' to '{target_category}'.")
                files_moved[target_category] += 1
                moved = True
            except PermissionError:
                print(Fore.YELLOW + f"Permission denied for '{item}'. Skipping.")
                logger.warning(f"Permission denied while moving '{item}'.")
                files_skipped_permission += 1
                moved = True # Mark as handled/skipped, don't try 'Others' again
            except FileNotFoundError:
                print(Fore.YELLOW + f"File '{item}' not found (might have been moved/deleted). Skipping.")
                logger.warning(f"File '{item}' not found during organization, possibly already handled.")
                files_skipped_other_error += 1
                moved = True
            except shutil.Error as e: # Catch other shutil specific errors
                print(Fore.RED + f"Shutil error moving '{item}': {e}. Skipping.")
                logger.error(f"Shutil error moving '{item}' to '{target_category}': {e}")
                files_skipped_other_error += 1
                moved = True
            except Exception as e: # Catch any other unexpected errors
                print(Fore.RED + f"Unexpected error moving '{item}': {e}. Skipping.")
                logger.error(f"Unexpected error moving '{item}' to '{target_category}': {e}")
                files_skipped_other_error += 1
                moved = True
        elif os.path.isdir(item_path):
            print(Fore.BLUE + f"Skipping directory: {item}")
            logger.info(f"Skipping directory during organization: {item}")
            files_skipped_non_file += 1
        else: # For symlinks, device files etc.
            print(Fore.BLUE + f"Skipping non-file system entry: {item}")
            logger.info(f"Skipping non-file system entry during organization: {item}")
            files_skipped_non_file += 1

    print(Fore.CYAN + "\n--- Organization Summary ---")
    total_moved = sum(files_moved.values())
    if total_moved > 0:
        for category, count in files_moved.items():
            print(Fore.GREEN + f"  {category}: {count} files moved.")
    else:
        print(Fore.YELLOW + "No files were moved.")

    if files_skipped_permission > 0:
        print(Fore.YELLOW + f"{files_skipped_permission} files were skipped due to permission errors.")
    if files_skipped_other_error > 0:
        print(Fore.YELLOW + f"{files_skipped_other_error} files were skipped due to other errors.")
    if files_skipped_non_file > 0:
        print(Fore.BLUE + f"{files_skipped_non_file} non-file items (directories, etc.) were skipped.")
        
    print(Fore.CYAN + "--------------------------")
    logger.info("Download organization complete.")