import os
import sys
import logging
import markdown
import pdfkit

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("conversion.log", mode="w")]
)

def convert_md_to_pdf(input_path, output_path):
    """
    Convert a Markdown file to a PDF.

    :param input_path: Path to the input Markdown file.
    :param output_path: Path to the output PDF file.
    """
    try:
        if not os.path.exists(input_path):
            logging.error(f"Input file does not exist: {input_path}")
            return False

        # Read Markdown file with UTF-8 encoding
        with open(input_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content, output_format="html5")

        # Add inline CSS for font styling
        inline_css = """
        <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 12pt;
            line-height: 1.6;
            color: #000000;
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: Arial, sans-serif;
            color: #333333;
        }
        </style>
        """
        html_content = inline_css + html_content

        # Save HTML content for debugging
        with open("debug.html", "w", encoding="utf-8") as debug_file:
            debug_file.write(html_content)

        # Convert HTML to PDF
        pdfkit_options = {
            "encoding": "UTF-8",
            "quiet": "",
            "dpi": 300,
        }
        pdfkit.from_string(html_content, output_path, options=pdfkit_options)

        logging.info(f"Successfully converted {input_path} to {output_path}")
        return True
    except Exception as e:
        logging.error(f"Error converting {input_path} to PDF: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        logging.error("Usage: python md_to_pdf.py <input_file.md> <output_file.pdf>")
        sys.exit(1)

    # Get input and output paths
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Create the output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logging.info(f"Created directory: {output_dir}")

    # Convert the Markdown file to a PDF
    success = convert_md_to_pdf(input_file, output_file)
    if not success:
        logging.error(f"Failed to convert {input_file} to {output_file}")
        sys.exit(1)
