# FastAPI
from fastapi import APIRouter, status,UploadFile,File, Depends
from sqlalchemy.orm import Session
# Src/files
from pdf.schemas import (PfdUuidResponse,)
from pdf.validations import validate_pdf
from pdf import models
from pdf.utils import extract_pdf_info
# Python
import uuid
import os
#Depend
from database import get_db

pdf_router = APIRouter()



@pdf_router.post('/',status_code = status.HTTP_201_CREATED) 
async def create_a_pdf(file:UploadFile = File(...), db: Session = Depends(get_db)) -> dict:
    print("Triggered Upload API")
    
    validate_pdf(file)
    
    pdf_id = str(uuid.uuid4())
    print(pdf_id)
    upload_dir = "../uploads/pdf"
    os.makedirs(upload_dir, exist_ok=True)
    file_location = f"{upload_dir}/{pdf_id}.pdf"
    
    with open(file_location, "wb") as f:
        f.write(await file.read())

    text, page_count = extract_pdf_info(file_location)
    
    new_pdf = models.Pdf(
        title = file.filename,
        file_size = file.size,
        
        page_count=page_count,
        context_text = text,
        unique_value=pdf_id
    )
    db.add(new_pdf)
    db.commit()
    db.refresh(new_pdf)
    
    return {"unique_value":new_pdf.unique_value}



#curl -X POST "http://localhost:8000/api/v1/pdf/" -F "file=@/home/serhat//project/gemini/gemini/sample.pdf"
#! Test route
@pdf_router.get('/all',status_code = status.HTTP_200_OK) 
async def get_all_pdfs(db: Session = Depends(get_db)):
    pdfs = db.query(models.Pdf).all() 
    return pdfs

