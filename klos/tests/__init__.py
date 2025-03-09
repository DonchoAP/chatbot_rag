import os
import unittest
from langchain.schema import Document
from chatbot_rag.textsplit import load_documents, split_documents, load_documents_from_folder

def test_split_large_document(self):
        # Test splitting a large document into chunks
        large_content = "This is a large test document. " * 1000
        documents = [Document(page_content=large_content)]
        chunks = split_documents(documents)
        self.assertGreater(len(chunks), 1)

def test_load_multiple_documents(self):
        # Test loading multiple documents from a folder
        folder_path = "test_folder"
        os.makedirs(folder_path, exist_ok=True)
        pdf_path1 = os.path.join(folder_path, "test1.pdf")
        pdf_path2 = os.path.join(folder_path, "test2.pdf")
        self.create_test_pdf(pdf_path1)
        self.create_test_pdf(pdf_path2)
        
        try:
            documents = load_documents_from_folder(folder_path)
            self.assertGreater(len(documents), 1)
        finally:
            # Clean up the created files and folder
            os.remove(pdf_path1)
            os.remove(pdf_path2)
            os.rmdir(folder_path)
