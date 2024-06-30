import os
import shutil

# Define the source directory and the destination directories
source_dir = "path/to/your/downloads"  # Change this to your downloads folder path
dest_dirs = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh"],
}

def create_directories(base_dir, directories):
    """Create directories if they don't exist."""
    for directory in directories:
        dir_path = os.path.join(base_dir, directory)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

def move_files_to_directories(source, dest_dirs):
    """Move files to their respective directories based on file extensions."""
    for file_name in os.listdir(source):
        file_path = os.path.join(source, file_name)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file_name)[1].lower()
            moved = False
            for dir_name, extensions in dest_dirs.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(source, dir_name, file_name))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(source, "Others", file_name))

def main():
    create_directories(source_dir, list(dest_dirs.keys()) + ["Others"])
    move_files_to_directories(source_dir, dest_dirs)
    print("Files have been organized successfully.")

if __name__ == "__main__":
    main()
