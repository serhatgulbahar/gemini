
#! FastAPI
from fastapi import FastAPI
from dotenv import load_dotenv
import os
#! Database
from database import init_db

version = "v1"
app = FastAPI(
    title = "Chat With PDF API",
    description = "Chat with GeminiAI about Pdfs",
    version=version
)

#! Routes
from pdf.routes import pdf_router
from chat.routes import chat_router

app.include_router(pdf_router, prefix=f"/api/{version}/pdf", tags = ['Pdf Files'])
app.include_router(chat_router, prefix=f"/api/{version}/chat", tags = ['Chat with Pdf'])


if __name__ == "main":
    init_db()