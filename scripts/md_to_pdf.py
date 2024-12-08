import os
import subprocess

def convert_md_to_pdf(md_file, output_dir=None):
    """
    Converts a Markdown file to PDF using pandoc and keeps the Markdown file intact.

    Args:
        md_file (str): Path to the Markdown file.
        output_dir (str, optional): Directory to save the PDF. Defaults to the same directory as the Markdown file.

    Returns:
        str: Path to the generated PDF file.
    """
    if not os.path.exists(md_file):
        raise FileNotFoundError(f"The file '{md_file}' does not exist.")

    if not md_file.endswith(".md"):
        raise ValueError("The input file must be a Markdown file (.md).")

    # Set output directory
    output_dir = output_dir or os.path.dirname(md_file)
    os.makedirs(output_dir, exist_ok=True)

    # Generate output PDF file name
    pdf_file = os.path.join(output_dir, os.path.splitext(os.path.basename(md_file))[0] + ".pdf")

    # Run pandoc to convert Markdown to PDF
    try:
        subprocess.run(
            ["pandoc", md_file, "-o", pdf_file],
            check=True
        )
        print(f"Converted '{md_file}' to '{pdf_file}'.")
        return pdf_file
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
        raise RuntimeError("Pandoc failed to convert the Markdown file to PDF.")

if __name__ == "__main__":
    # Path to the Markdown file
    md_file = "../resumes/Sreyeesh_Garimella_Engineer_Manager_EMPA.md"

    # Convert to PDF
    try:
        convert_md_to_pdf(md_file)
    except Exception as e:
        print(str(e))
