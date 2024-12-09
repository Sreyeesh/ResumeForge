import os
import pdfkit
from markdown import markdown
from jinja2 import Template

def convert_markdown_to_pdf(input_path, output_path, css_path):
    """Convert Markdown file to PDF using the specified CSS."""
    # Read the Markdown file
    with open(input_path, 'r') as f:
        md_content = f.read()
    
    # Convert Markdown to HTML
    html_content = markdown(md_content)
    
    # Apply CSS for styling
    with open(css_path, 'r') as css_file:
        css = css_file.read()

    # Create the final HTML template with applied CSS
    html_template = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Resume</title>
        <style>{css}</style>
    </head>
    <body>
        <div class="markdown-body">
            {html_content}
        </div>
    </body>
    </html>
    """
    
    # Generate PDF from HTML
    pdfkit.from_string(html_template, output_path)

def find_md_files_in_directory(directory):
    """Find all .md files in a directory."""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def main():
    # Path to the directory where Markdown files are stored
    resumes_dir = './resumes'
    
    # Path to the CSS file for styling
    css_file_path = './styles/github-markdown.css'
    
    # Find all Markdown files in the resumes directory
    md_files = find_md_files_in_directory(resumes_dir)

    # Process each Markdown file
    for md_file in md_files:
        # Set output PDF file path
        output_pdf = md_file.replace('.md', '.pdf')

        # Convert Markdown to PDF
        print(f"Processing: {md_file}")
        convert_markdown_to_pdf(md_file, output_pdf, css_file_path)
        print(f"PDF generated: {output_pdf}")

if __name__ == "__main__":
    main()
