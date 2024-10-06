import pdfplumber




def extract_pdf_info(file_path):
    with pdfplumber.open(file_path) as pdf:
        page_count = len(pdf.pages)
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text, page_count


#! Text kayıt işlemlerini daha lean yapmalacak.