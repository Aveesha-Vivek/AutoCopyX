//Aveesha Vivek 2024

import os
import time
import shutil

# Define the path to the .md file with user info
SOURCE_FILE = r"C:\Users\Vivek Bandara\PycharmProjects\pythonProject\.venv\Scripts\dist\user_info.md"
  # Path to your .md file
DESTINATION_DRIVE = 'F:\\'  # Define the destination drive as F:


# Function to check if the F: drive is available and copy the file once
def copy_to_flash_drive():
    file_copied = False  # Flag to track if the file has been copied

    while True:
        if os.path.exists(DESTINATION_DRIVE):  # Check if F: drive is available
            if not file_copied:  # Only copy if the file has not been copied yet
                try:
                    # Construct destination path
                    dest_path = os.path.join(DESTINATION_DRIVE, os.path.basename(SOURCE_FILE))

                    # Copy the .md file
                    shutil.copy(SOURCE_FILE, dest_path)
                    print(f"File copied to {dest_path}")
                    file_copied = True  # Set the flag to True after copying
                except Exception as e:
                    print(f"Error copying file: {e}")

        else:
            print("Waiting for F: drive to be available...")

        time.sleep(2)  # Check every 2 seconds


# Run the function
if __name__ == "__main__":
    copy_to_flash_drive()
