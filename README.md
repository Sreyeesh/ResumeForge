

---

# ResumeForge

**ResumeForge** is a Python-based solution for managing and converting Markdown files into polished PDF resumes and cover letters. It’s designed for developers, professionals, and students who want a customizable, version-controlled workflow for creating and maintaining job application documents.

---

## Features

- **Markdown to PDF Conversion**:  
  Easily generate beautifully styled PDFs from Markdown files.
- **Customizable Styling**:  
  Use inline CSS or external stylesheets to control the appearance of your PDFs.
- **GitHub Actions Integration**:  
  Automate the PDF generation process whenever a Markdown file is updated.
- **Template Management**:  
  Organize and version-control multiple resumes and cover letters using Git.
- **Dynamic Directory Structure**:  
  Keep your resumes, cover letters, and scripts well-organized.

---

## Directory Structure

```plaintext
ResumeForge/
├── .github/                     # GitHub workflows for automation
│   └── workflows/
│       └── convert-markdown-to-pdf.yml
├── assets/                      # Fonts, images, or other resources
├── generated_pdfs/              # Auto-generated PDF files (ignored in Git)
├── resumes/                     # Markdown files for resumes and cover letters
│   ├── cover-letters/           # Subdirectory for cover letters
│   │   ├── epam-cover-letter.md
│   │   └── master_cover_letter.md
│   ├── master-resume.md
├── scripts/                     # Python scripts for functionality
│   ├── convert_markdown_to_pdf.py  # Main conversion script
│   └── setup.py                 # Setup script for packaging (if needed)
├── styles/                      # CSS styles for PDF formatting
│   └── custom-style.css         # Default CSS for styling the PDFs
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── .gitignore                   # Ignore unnecessary files and directories
```

---

## Getting Started

Follow these steps to set up and use ResumeForge:

### Prerequisites

- **Python 3.9+**
- **wkhtmltopdf**: For converting HTML to PDF.
- **pip**: Python package manager.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sreyeesh/ResumeForge.git
   cd ResumeForge
   ```

2. Install Python dependencies from `requirements.txt`:
   ```bash
   python3 -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

   The following libraries are required for the project:
   - **Jinja2==3.1.4**: Templating engine for HTML generation.
   - **Markdown==3.7**: Converts Markdown files to HTML.
   - **MarkupSafe==3.0.2**: Supports safe handling of strings in Jinja2.
   - **pdfkit==1.0.0**: Generates PDF files from HTML using `wkhtmltopdf`.

3. Install `wkhtmltopdf`:
   ```bash
   sudo apt-get update
   sudo apt-get install -y wkhtmltopdf fonts-liberation ttf-mscorefonts-installer
   ```

---

## Usage

### Convert Markdown to PDF Locally

1. Place your Markdown files in the `resumes/` directory or its subdirectories.
2. Run the `convert_markdown_to_pdf.py` script:
   ```bash
   python3 scripts/convert_markdown_to_pdf.py resumes/master-resume.md generated_pdfs/master-resume.pdf
   ```
3. Your PDF will be saved in the `generated_pdfs/` directory.

### Automate with GitHub Actions

1. Push changes to the `resumes/` or `resumes/cover-letters/` directories.
2. GitHub Actions will automatically run the conversion workflow (`convert-markdown-to-pdf.yml`).
3. Download the generated PDFs from the workflow artifacts.

---

## Templates

Start with the provided Markdown templates for resumes and cover letters:
- **Master Resume**: [master-resume.md](resumes/master-resume.md)
- **Master Cover Letter**: [master_cover_letter.md](resumes/cover-letters/master_cover_letter.md)

Feel free to customize these templates to suit your needs.

---

## Customization

### CSS Styling

Modify the `styles/custom-style.css` file to change the appearance of the generated PDFs. You can customize:
- Fonts
- Margins
- Colors
- Line spacing

### Add New Templates

1. Create a new Markdown file in the `resumes/` or `resumes/cover-letters/` directory.
2. Follow the Markdown syntax to structure your resume or cover letter.
3. Run the script to generate a PDF.

---

## Contribution Guidelines

Contributions are welcome! Here’s how you can help:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "feat: add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a pull request.

---

## Troubleshooting

### Common Issues

1. **wkhtmltopdf Not Found**:
   - Ensure it is installed and available in your `PATH`.
   - Test the installation:
     ```bash
     wkhtmltopdf --version
     ```

2. **Formatting Issues**:
   - Verify that the Markdown files use proper UTF-8 encoding.
   - Adjust the CSS in `styles/custom-style.css` if needed.

3. **No PDFs Generated**:
   - Check for errors in the logs (`conversion.log`).
   - Ensure the input and output file paths are correct.

---

## Acknowledgments

Special thanks to the open-source tools and libraries used in this project:
- [wkhtmltopdf](https://wkhtmltopdf.org/)
- [Python-Markdown](https://python-markdown.github.io/)

---

