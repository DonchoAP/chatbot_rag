import os
import io
from pdfminer.high_level import extract_text_to_fp

#C:\\Users\\49174\\Desktop\\Presentation\\chatbot_rag\\data

def load_documents_from_folder(folder_path):
    all_documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            print("Loading documents from:", pdf_path)
            documents = load_documents(pdf_path)
            all_documents.extend(documents)
    return all_documents

def load_documents(pdf_path):
    try:
        output = io.StringIO()
        with open(pdf_path, 'rb') as pdf_file:
            extract_text_to_fp(pdf_file, output)
        documents = output.getvalue().split('\f')  # Split text into documents
        return documents
    except Exception as e:
        print("Error loading documents from", pdf_path, ":", e)
        return []

folder_path = "C:\\Users\\49174\\Desktop\\Presentation\\chatbot_rag\\data"
all_documents = load_documents_from_folder(folder_path)

if all_documents:
    print("Number of documents loaded from all PDF files:", len(all_documents))
    print("First document from the first PDF file:")
    print(all_documents[0])
else:
    print("No documents loaded from any PDF files in the folder.")