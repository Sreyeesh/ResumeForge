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

        with open(input_path, "r") as f:
            md_content = f.read()
        
        # Convert Markdown to HTML
        html_content = markdown.markdown(md_content)
        
        # Convert HTML to PDF
        pdfkit.from_string(html_content, output_path)
        logging.info(f"Successfully converted {input_path} to {output_path}")
        return True
    except Exception as e:
        logging.error(f"Error converting {input_path} to PDF: {e}")
        return False

if __name__ == "__main__":
    # Ensure correct number of arguments
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
