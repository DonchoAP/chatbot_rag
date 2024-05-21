#import embeddings
from langchain_community.embeddings.ollama import OllamaEmbeddings
import socket


def get_embedding_function():
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings 



HOST = '127.0.0.1'
PORT = 5001  # Change this to the new port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
