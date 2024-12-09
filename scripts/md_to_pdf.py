import sys
import markdown
import pdfkit

def convert_markdown_to_pdf(input_path, output_path):
    with open(input_path, 'r') as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content, extensions=['tables'])
    # Add CSS styling
    css_path = 'styles/github-markdown.css'
    styled_html = f"""
    <html>
    <head>
      <link rel="stylesheet" href="{css_path}">
    </head>
    <body class="markdown-body">
      {html_content}
    </body>
    </html>
    """
    pdfkit.from_string(styled_html, output_path, options={"enable-local-file-access": ""})

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    convert_markdown_to_pdf(input_path, output_path)
