# FastAPI
from fastapi import APIRouter, status,UploadFile,File, Depends, HTTPException
from sqlalchemy.orm import Session
#Depend
from database import get_db
# Src
from pdf import models


chat_router = APIRouter()


@chat_router.post('/{pdf_id}',status_code = status.HTTP_200_OK) 
async def chat_with_pdf(pdf_id:str , db: Session = Depends(get_db)):
    pdf_record = db.get(models.Pdf, pdf_id)
    if not pdf_record:
        raise HTTPException(status_code=404, detail="PDF not found")
    
    
    return {"Test":"pdf_id"}