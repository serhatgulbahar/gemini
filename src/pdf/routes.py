# FastAPI
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
# Src/files
from pdf.schemas import Pdf
# Python
from typing import List

pdf_router = APIRouter()



@pdf_router.post('/',status_code = status.HTTP_201_CREATED) #!, response_model = List[Pdf]
async def create_a_pdf(pdf_data:Pdf) -> dict:
    return {"unique_value":""}



