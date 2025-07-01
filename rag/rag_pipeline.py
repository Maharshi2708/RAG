from rag.document_loader import load_document_from_url
from rag.vector_db import store_documents, delete_documents_by_source, search_similar_docs
from rag.llm import generate_answer

def load_and_index_document(url):
    documents, source_id = load_document_from_url(url)

    if documents:
        store_documents(documents, source_id)
    else:
        print("No valid content found to store in the vector database.")

def query_rag(query, k=5):
    retrieved_docs = search_similar_docs(query, k=k)
    if not retrieved_docs:
        return "No Documents available to answer the question."

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    prompt = f"""
You are an expert AI assistant. Provide a detailed and accurate answer based strictly on the provided context only. Do not add additional information or make assumptions beyond the context or from your knowledge. Kindly stick to the context provided.
If the answer is not available in the context, respond with: "The answer is not available in the provided context."

Context:
{context}

Question:
{query}

Answer:
"""
    return generate_answer(prompt, query)

def refresh_document(url):
    print("Refreshing document...")
    delete_documents_by_source(url)
    load_and_index_document(url)
    print("Document refreshed successfully.")

def delete_document(source_id):
    delete_documents_by_source(source_id)
