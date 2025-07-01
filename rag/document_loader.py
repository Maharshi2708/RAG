import os
import requests
import pytesseract
from langchain_community.document_loaders import PyPDFLoader
from langchain.schema.document import Document
from pdf2image import convert_from_path
from urllib.parse import urlparse

def is_url(string):
    try:
        result = urlparse(string)
        return result.scheme in ('http', 'https')
    except:
        return False

def download_pdf(url, filename='temp_file.pdf'):
    print("Downloading PDF from the internet...")
    response = requests.get(url, verify=False)  
    with open(filename, 'wb') as f:
        f.write(response.content)
    return filename

def ocr_extract(pdf_path):
    try:
        images = convert_from_path(pdf_path, poppler_path=r'C:\poppler\poppler-24.08.0\Library\bin')
        text = ""
        for img in images:
            text += pytesseract.image_to_string(img)
        return text
    except Exception as e:
        print(f"OCR extraction failed: {e}")

def load_document_from_url(path_or_url):
    is_temp_file = False
    if is_url(path_or_url):
        source_id = path_or_url
        pdf_path = download_pdf(path_or_url)
        is_temp_file = True
    else:
        if not os.path.exists(path_or_url):
            raise Exception("File not found. Please check the path.")
        source_id = path_or_url
        pdf_path = path_or_url

    try:
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        
        full_text = "".join([doc.page_content.strip() for doc in documents])
        if not full_text or len(full_text) < 50:  
            raise Exception("Loaded content is empty or insufficient, possibly a scanned PDF.")
        print("Document loaded successfully using PyPDFLoader.")
        if is_temp_file:
            os.remove(pdf_path)
        return documents, source_id

    except Exception as e:
        print(f"Error loading with PyPDFLoader: {e}")
        print("Falling back to OCR...")
        text = ocr_extract(pdf_path)
        if is_temp_file:
            os.remove(pdf_path)
        if text.strip():
            doc = Document(page_content=text, metadata={"source": source_id})
            print("Document loaded successfully using OCR.")
            return [doc], source_id
        else:
            print("OCR failed to extract text from the document.")
            return [], source_id