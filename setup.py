import os

# Define the desired project structure
project_structure = {
    "resumes": ["master-resume.md", "frontend-resume.md", "backend-resume.md", "devops-resume.md", "data-engineer-resume.md"],
    "templates": ["template.html", "resume-template.md", "cover-letter-template.md", "portfolio-template.md"],
    "assets": ["github.css", "example-resume.pdf", "logo.png"],
    "scripts": ["resume-tailor.py", "convert-markdown-to-pdf.py"],
    ".github/workflows": ["convert-markdown-to-pdf.yml"]
}

# Base directory for the project
base_dir = os.getcwd()  # Sets the current working directory as the base

def create_project_structure(base_dir, structure):
    """Create the project folder structure and placeholder files."""
    for folder, files in structure.items():
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)  # Create the folder
        print(f"Created folder: {folder_path}")

        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'w') as file:
                file.write("")  # Create an empty placeholder file
            print(f"Created file: {file_path}")

    print("Project setup completed successfully!")

# Run the setup
create_project_structure(base_dir, project_structure)
