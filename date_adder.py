import os
from datetime import datetime

def add_date_to_filenames(folder_path):
    # Get today's date in YYYY-MM-DD format
    today_date = datetime.now().strftime("%Y-%m-%d")
    
    # Iterate over all files in the specified folder
    for filename in os.listdir(folder_path):
        # Construct the full file path
        old_file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(old_file_path):
            # Create the new filename with the date prefix
            new_filename = f"{today_date}_{filename}"
            new_file_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    test_folder = "test_files"
    if os.path.exists(test_folder):
        add_date_to_filenames(test_folder)
    else:
        print(f"Error: Folder '{test_folder}' not found.")
