import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

from langchain_community.vectorstores import Chroma

from helper import openai_embedding, docs_folder

def load_documents():
    document=[] 
    for file in os.listdir(docs_folder): 
        if file.endswith(".pdf"): 
            pdf_path = f"./{docs_folder}/" + file 
            loader=PyPDFLoader(pdf_path) 
            document.extend(loader.load()) 
        elif file.endswith('.docx') or file.endswith('.doc'): 
            doc_path = f"./{docs_folder}/" + file 
            loader = Docx2txtLoader(doc_path) 
            document.extend(loader.load()) 
        elif file.endswith('.txt'): 
            text_path = f"./{docs_folder}/" + file 
            loader = TextLoader(text_path) 
            document.extend(loader.load())
    
    return document

def get_text_chunks(docs):
    text_splitter = CharacterTextSplitter(
        chunk_size=512, #change chunk size by desired
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(docs)

    return chunks

def create_vector_db_on_disk(docs):
    persist_directory = 'vector_on_disk'

    Chroma.from_documents(
        documents=docs,
        embedding = openai_embedding,
        persist_directory=persist_directory
    )

def handle_query(query, qa):
    if query.lower() == 'exit':
        return "Exiting program..."
    else:
        answer = qa(query)
        if answer:
            return answer.get('result')
        else:
            return "Na túto otázku neviem odpovedať."

if __name__ == "__main__":
    docs = load_documents()
    print(docs)
    chunks = get_text_chunks(docs)
    create_vector_db_on_disk(chunks)

