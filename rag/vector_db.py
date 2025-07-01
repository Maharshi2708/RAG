import os
from langchain_chroma import Chroma
from langchain_community.vectorstores import Chroma as VectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

DB_DIR = "data/rag_db"
_vectordb = None

def get_vector_db():
    global _vectordb
    os.makedirs(DB_DIR, exist_ok=True)

    if _vectordb is None:
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        if os.listdir(DB_DIR):
            print(f"Loading existing Chroma DB from {DB_DIR}")
        else:
            print(f"Creating new Chroma DB in {DB_DIR}")
        _vectordb = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)

    return _vectordb

def store_documents(raw_documents, source_id):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(raw_documents)

    valid_chunks = []
    for chunk in chunks:
        if chunk.page_content.strip():  
            if chunk.metadata is None:
                chunk.metadata = {}
            chunk.metadata['source_id'] = source_id
            valid_chunks.append(chunk)

    if not valid_chunks:
        print("No valid content found to store in the vector database.")
        return

    db = get_vector_db()
    db.add_documents(valid_chunks)
    print(f"Document loaded and indexed successfully.")

def search_similar_docs(query, k=3):
    db = get_vector_db()
    return db.similarity_search(query, k=k)

def delete_documents_by_source(source_id):
    global _vectordb
    db = get_vector_db()
    db.delete(where={"source_id": source_id})
    print(f"Documents from source '{source_id}' deleted successfully.")
    _vectordb = None
