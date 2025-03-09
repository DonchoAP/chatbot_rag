import os
import io
from pdfminer.high_level import extract_text_to_fp
import unittest

def load_documents_from_folder(folder_path):
    # Initialize a list to store all documents
    all_documents = []
    # Iterate over all files in the specified folder
    for filename in os.listdir(folder_path):
        # Check if the file has a .pdf extension
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            print("Loading documents from:", pdf_path)
            # Load documents from the PDF file
            documents = load_documents(pdf_path)
            # Add the loaded documents to the total list
            all_documents.extend(documents)
    return all_documents

def load_documents(pdf_path):
    try:
        output = io.StringIO()
        # Open the PDF file in binary mode
        with open(pdf_path, 'rb') as pdf_file:
            # Extract text from the PDF file
            extract_text_to_fp(pdf_file, output)
        # Split the extracted text into separate documents
        documents = output.getvalue().split('\f')
        return documents
    except Exception as e:
        print("Error loading documents from", pdf_path, ":", e)
        return []

folder_path = "path"
all_documents = load_documents_from_folder(folder_path)

# Add decorator to split the documents into chunks
if all_documents:
    print("Number of documents loaded from all PDF files:", len(all_documents))
    print("First document from the first PDF file:")
    print(all_documents[0])
else:
    print("No documents loaded from any PDF files in the folder.")

# Use Singleton pattern to ensure only one instance of the class is created

class TestDocumentLoader(unittest.TestCase):
    def test_load_documents_from_folder(self):
        folder_path = "test_data"
        os.makedirs(folder_path, exist_ok=True)
        # Create a test PDF file
        with open(os.path.join(folder_path, "test.pdf"), "w") as f:
            f.write("Test PDF content")
        # Load documents from the test folder
        documents = load_documents_from_folder(folder_path)
        self.assertGreater(len(documents), 0)
        # Remove the test file and folder
        os.remove(os.path.join(folder_path, "test.pdf"))
        os.rmdir(folder_path)

    def test_load_documents(self):
        pdf_path = "test.pdf"
        # Create a test PDF file
        with open(pdf_path, "w") as f:
            f.write("Test PDF content")
        # Load documents from the test PDF file
        documents = load_documents(pdf_path)
        self.assertGreater(len(documents), 0)
        # Remove the test file
        os.remove(pdf_path)

if __name__ == "__main__":
    unittest.main()