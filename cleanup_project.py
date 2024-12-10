import os
import shutil

# Define the project structure
project_structure = {
    "assets": [],
    "generated_pdfs": [],
    "node_modules": [],
    "resumes": [
        "cover-letters"  # Subfolder for cover letters
    ],
    "scripts": [],
    "styles": [],
}

# Files to move to specific folders
files_to_move = {
    "scripts": ["convert_markdown_to_pdf.py", "setup.py"],
    "styles": ["custom-style.css"],  # Add your CSS files here
    "resumes": ["master-resume.md", "master_cover_letter.md"],
}

# Temporary/debug files to delete
files_to_delete = ["debug.html", "test.pdf", "conversion.log"]

# Function to create directories
def create_directories(base_path, structure):
    for folder, subfolders in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)

# Function to move files
def move_files(base_path, files_mapping):
    for target_folder, files in files_mapping.items():
        target_path = os.path.join(base_path, target_folder)
        os.makedirs(target_path, exist_ok=True)
        for file_name in files:
            source_path = os.path.join(base_path, file_name)
            if os.path.exists(source_path):
                shutil.move(source_path, os.path.join(target_path, file_name))
                print(f"Moved {file_name} to {target_folder}/")
            else:
                print(f"File {file_name} not found, skipping...")

# Function to delete files
def delete_files(base_path, files):
    for file_name in files:
        file_path = os.path.join(base_path, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted {file_name}")
        else:
            print(f"File {file_name} not found, skipping...")

# Function to clean up node_modules
def cleanup_node_modules(base_path):
    node_modules_path = os.path.join(base_path, "node_modules")
    if os.path.exists(node_modules_path):
        shutil.rmtree(node_modules_path)
        print("Removed node_modules/ directory")

# Main function
def cleanup_project(base_path):
    print("Starting cleanup process...")
    create_directories(base_path, project_structure)
    move_files(base_path, files_to_move)
    delete_files(base_path, files_to_delete)
    cleanup_node_modules(base_path)
    print("Cleanup completed successfully!")

# Run the script
if __name__ == "__main__":
    base_directory = os.getcwd()  # Current directory
    cleanup_project(base_directory)
