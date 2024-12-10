import os
import markdown
import pdfkit

CSS_FILE = "styles/github-markdown.css"  # Path to your GitHub-styled CSS
RESUMES_DIR = "resumes"  # Directory containing Markdown files

def convert_markdown_to_pdf(input_file, output_file):
    """Convert a Markdown file to a PDF using GitHub-styled CSS."""
    # Read and convert Markdown to HTML
    with open(input_file, "r", encoding="utf-8") as md_file:
        raw_markdown_content = md_file.read()
        html_content = markdown.markdown(raw_markdown_content)

    # Wrap HTML in the GitHub-styled template
    styled_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{os.path.basename(input_file)}</title>
        <link rel="stylesheet" href="file://{os.path.abspath(CSS_FILE)}">
    </head>
    <body class="markdown-body">
        {html_content}
    </body>
    </html>
    """

    # Save HTML to debug.html for review
    debug_html_path = "debug.html"
    with open(debug_html_path, "w", encoding="utf-8") as debug_file:
        debug_file.write(styled_html)

    # Convert HTML to PDF
    options = {"enable-local-file-access": None}  # Required for wkhtmltopdf
    pdfkit.from_file(debug_html_path, output_file, options=options)
    print(f"PDF generated: {output_file}")

def main():
    """Iterate over Markdown files in the resumes directory and convert to PDFs."""
    for file_name in os.listdir(RESUMES_DIR):
        if file_name.endswith(".md"):
            input_path = os.path.join(RESUMES_DIR, file_name)
            output_path = input_path.replace(".md", ".pdf")
            print(f"Processing: {input_path}")
            convert_markdown_to_pdf(input_path, output_path)

if __name__ == "__main__":
    main()
