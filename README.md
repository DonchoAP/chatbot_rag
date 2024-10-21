PDF Document Processor with Embeddings Integration
This project focuses on extracting and processing text from PDF documents, splitting the text into manageable chunks, and providing embeddings for further processing, such as natural language processing (NLP) tasks. It includes functionality for loading PDFs, splitting the extracted text, and integrating with embedding models for text representation.

Table of Contents
Installation
Project Structure
Features
PDF Document Loading
Text Splitting
Embeddings Integration
Usage
Loading PDFs from Folder
Text Splitting Example
Embedding Example
Requirements
Contributing
License
Installation
To use this project, follow these steps:

Clone the repository:

bash

git clone <repository-url>
cd <repository-directory>
Install the required dependencies:

bash

pip install -r requirements.txt
(Optional) Install additional packages for embeddings integration, if not included in requirements.txt:

bash

pip install langchain chromadb pypdf pytest
Project Structure
plaintext

.
├── main.py                  # Main Python script for loading, processing, and embedding PDFs
├── README.md                # Project documentation (this file)
├── requirements.txt         # Required packages
└── sample_pdfs/             # Folder containing sample PDF files (for testing purposes)
Features
PDF Document Loading
The project provides functionality to load PDF files from a folder, read the content of each page, and split them into individual documents. This is useful for processing multi-page PDF files and handling large amounts of text data.

Functionality:
load_documents_from_folder(folder_path): Loads PDF files from a specified folder.
load_documents(pdf_path): Extracts text from individual PDF files and returns a list of documents.
Text Splitting
Once the text is extracted from PDF files, it can be split into smaller chunks for easier processing using the RecursiveCharacterTextSplitter from the langchain_text_splitters package.

Functionality:
split_documents(documents): Splits text into smaller chunks with a specified chunk size and overlap for text chunking.
Embeddings Integration
This project integrates text embeddings using the OllamaEmbeddings from langchain_community. These embeddings are useful for a variety of NLP tasks, including text similarity, clustering, and classification.

Functionality:
get_embedding_function(): Returns an embedding function that can be used to obtain vector representations of the text.
The socket server setup allows for interactions with the embeddings module via a network interface.
Usage
Loading PDFs from Folder
To load all PDF files from a folder and process them:

python

folder_path = "path_to_your_pdf_folder"
all_documents = load_documents_from_folder(folder_path)

if all_documents:
    print(f"Number of documents loaded: {len(all_documents)}")
    print("First document content:")
    print(all_documents[0])
else:
    print("No documents loaded.")
Text Splitting Example
To split loaded documents into smaller chunks:

python

pdf_path = "path_to_your_pdf_file.pdf"
documents = load_documents(pdf_path)
chunks = split_documents(documents)

print("First chunk of the document:")
print(chunks[0])
Embedding Example
To generate text embeddings using the Ollama model:

python

from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings

# Example usage
embedding_function = get_embedding_function()
Network Server for Embedding Access
You can set up a socket server to expose the embedding functionality for external access:

python
import socket

HOST = '127.0.0.1'
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Server is listening on port", PORT)
Requirements
The following Python packages are required to run this project:

langchain
chromadb
pypdf
pytest
You can install these dependencies using the following command:

bash

pip install -r requirements.txt
Contributing
Contributions are welcome! Please submit a pull request or open an issue if you have any improvements or bug fixes.

Fork the repository
Create your feature branch (git checkout -b feature/NewFeature)
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature/NewFeature)
Open a Pull Request
License
This project is licensed under the MIT License. See the LICENSE file for details.
