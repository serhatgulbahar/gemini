from fastapi import HTTPException,UploadFile
import os

def validate_pdf(file: UploadFile):
    # Maksimum dosya boyutu (örneğin, 10 MB)
    MAX_FILE_SIZE = 10 * 1024 * 1024

    # Sadece PDF dosyalarını kabul edelim
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    
    # Dosya boyutunu kontrol et
    file_size = file.file._file.seek(0, os.SEEK_END)
    file.file._file.seek(0)  # Dosya konumunu başa al
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size exceeds the maximum allowed limit of 10MB.")

