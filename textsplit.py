import io
from abc import ABC, abstractmethod
from pdfminer.high_level import extract_text_to_fp
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

# Interface for text extraction from documents (can be extended to other document types)
class TextExtractor(ABC):
    @abstractmethod
    def extract_text(self, source) -> str:
        pass

# Concrete implementation of text extraction from a PDF file
class PDFTextExtractor(TextExtractor):
    def extract_text(self, source) -> str:
        output = io.StringIO()
        with open(source, 'rb') as pdf_file:
            extract_text_to_fp(pdf_file, output)
        return output.getvalue()

# Class responsible for loading documents
class DocumentLoader:
    def __init__(self, extractor: TextExtractor):
        self.extractor = extractor

    def load_documents(self, pdf_path: str) -> list[Document]:
        try:
            text = self.extractor.extract_text(pdf_path)
            texts = text.split('\f')  # Split text into documents
            return [Document(page_content=content) for content in texts]
        except Exception as e:
            print(f"Error loading documents from {pdf_path}: {e}")
            return []

# Class responsible for splitting the documents
class DocumentSplitter:
    def __init__(self, chunk_size: int = 800, chunk_overlap: int = 80):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            is_separator_regex=False,
        )

    def split_documents(self, documents: list[Document]) -> list[Document]:
        return self.text_splitter.split_documents(documents)

# Main function to orchestrate the workflow
def main(pdf_path: str):
    # Create an instance of the text extractor for PDFs
    pdf_extractor = PDFTextExtractor()
    document_loader = DocumentLoader(pdf_extractor)
    
    # Load documents
    documents = document_loader.load_documents(pdf_path)
    
    if documents:
        # Create an instance of the document splitter
        splitter = DocumentSplitter()
        # Split the documents into smaller chunks
        chunks = splitter.split_documents(documents)
        
        # Print the content of the first chunk
        print(chunks[0].page_content)
    else:
        print("No documents found.")

# Call the main function with the path to your PDF file
pdf_path = "path/to/your/document.pdf"
main(pdf_path)
