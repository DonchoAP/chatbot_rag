import io
from pdfminer.high_level import extract_text_to_fp
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

def load_documents(pdf_path):
    try:
        output = io.StringIO()
        with open(pdf_path, 'rb') as pdf_file:
            extract_text_to_fp(pdf_file, output)
        texts = output.getvalue().split('\f')  # Split text into documents
        documents = [Document(page_content=text) for text in texts]
        return documents
    except Exception as e:
        print("Error loading documents from", pdf_path, ":", e)
        return []

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)



# Specify the path to the PDF file
pdf_path = "C:\\Users\\49174\\Desktop\\Presentation\\chatbot_rag\\data"

# Load documents from the PDF file
documents = load_documents(pdf_path)

# Split the documents into chunks
chunks = split_documents(documents)

# Print the first chunk
#print(chunks[0])

def load_documents():
    # Create a Document object with the provided page content
    document = Document(page_content='Jo B. Das Joblexikon')
    # Return a list containing the Document object
    return [document] 
