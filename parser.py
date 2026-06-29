#convert pdf and docx to text, making it easier to process and analyze the content of these files. This module provides functions to extract text from PDF and DOCX files using the PyPDF2 and python-docx libraries, respectively.
from PyPDF2 import PdfReader
from docx import Document

#for pdf files, the extract_text_from_pdf function takes a file object as input, reads the PDF using PdfReader, and iterates through each page to extract the text. The extracted text is concatenated and returned as a single string.
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text

#for docx files, the extract_text_from_docx function takes a file object as input, reads the DOCX using Document, and iterates through each paragraph to extract the text. The extracted text is concatenated and returned as a single string.
def extract_text_from_docx(file):
    document = Document(file)
    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text