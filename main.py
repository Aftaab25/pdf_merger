import os
from PyPDF2 import PdfMerger
from tkinter import Tk, filedialog, simpledialog

def combine_pdfs():
    # Hide the root Tkinter window
    root = Tk()
    root.withdraw()

    # Allow user to select multiple PDF files (multiselect enabled)
    pdf_files = filedialog.askopenfilenames(
        title="Select PDF Files to Combine",
        filetypes=[("PDF Files", "*.pdf")],
        # Ensure multi-selection is enabled
        multiple=True  
    )

    if not pdf_files:
        print("No files selected.")
        return

    # Ask the user for the destination directory and file name
    destination_dir = filedialog.askdirectory(title="Select Destination Folder")
    if not destination_dir:
        print("No destination folder selected.")
        return

    output_filename = simpledialog.askstring("Output File", "Enter the name for the combined PDF (without .pdf):")
    if not output_filename:
        print("No output file name provided.")
        return

    output_filepath = os.path.join(destination_dir, f"{output_filename}.pdf")

    # Combine the selected PDFs
    merger = PdfMerger()

    for pdf in pdf_files:
        merger.append(pdf)

    # Save the combined PDF
    merger.write(output_filepath)
    merger.close()

    print(f"Combined PDF saved as: {output_filepath}")

if __name__ == "__main__":
    combine_pdfs()

