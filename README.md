
# 📄 RAG-based PDF Question Answering System  
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()  
[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()  
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()

---

## 🔍 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that:
- Loads PDFs from **URLs or local files** (with automatic OCR fallback for scanned PDFs).
- Chunks and stores documents in **Chroma vector store** using **Hugging Face embeddings**.
- Performs **semantic search and question answering** using a **local LLM (Phi3 via Ollama)**.
- Supports refreshing and deleting documents directly from the vector database.

---

## 📂 Project Structure

| Folder/File                | Purpose                                       |
|----------------------------|-----------------------------------------------|
| `rag/document_loader.py`   | Loads PDFs, handles URLs/local paths, OCR fallback |
| `rag/llm.py`               | Connects to Ollama’s Phi3 local LLM            |
| `rag/rag_pipeline.py`      | Handles document ingestion and retrieval logic |
| `rag/vector_db.py`         | Vector DB setup using Chroma + Hugging Face    |
| `main.py`                  | CLI interface for the complete pipeline        |
| `data\DB`                  | Database to store the Chunks of the pdf        |

---

## ✅ Features

- 📥 Load PDFs from **URLs or local paths**.
- 🔄 Automatic fallback to **OCR** for scanned PDFs.
- 📑 Efficient **chunking** using `RecursiveCharacterTextSplitter`.
- 🧠 Vector storage with **Chroma DB** and Hugging Face embeddings.
- 🤖 Semantic search with **local LLM (Phi3 via Ollama)**.
- ♻️ Refresh or delete documents by source ID.
- 🧹 Temporary file cleanup for downloaded PDFs.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Maharshi2708/RAG.git
cd RAG
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Install External Tools
- ✅ **Poppler**: For PDF to image conversion.  
  [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
- ✅ **Tesseract OCR**: For scanned PDF text extraction.  
  [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract)
- ✅ **Ollama**: For local LLMs.  
  [Ollama Official Site](https://ollama.ai/)

> 🔧 **Important:**  
> Make sure to update `poppler_path` in `document_loader.py` to match your local installation.
> Also change the Database directory `DB-DIR` path in `vector_db.py` to store the PDF chunks.

---

## 🚀 How to Run
```bash
python main.py
```

### Menu Options:
- `1`: Load a document from URL or local file.
- `2`: Ask a question based on the loaded documents.
- `3`: Exit the application.
- `4`: Refresh a document by its source ID.
- `5`: Delete a document by its source ID.