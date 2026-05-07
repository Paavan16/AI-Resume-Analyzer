import pdfplumber
from docx import Document

def extract_pdf_text(path):

    text = ""

    with pdfplumber.open(path) as pdf:

        for page in pdf.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + " "

    return text

def extract_docx_text(path):

    doc = Document(path)

    return " ".join(
        [paragraph.text for paragraph in doc.paragraphs]
    )

def extract_text(path):

    if path.endswith('.pdf'):
        return extract_pdf_text(path)

    elif path.endswith('.docx'):
        return extract_docx_text(path)

    elif path.endswith('.txt'):

        with open(path, 'r') as f:
            return f.read()

    return ""