
#! FastAPI
from fastapi import FastAPI
from dotenv import load_dotenv
import os
#! Database
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

#? Env variables.
load_dotenv()

# db
DATABASE_URL = "sqlite:///./test.db"
database = Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)


version = "v1"
app = FastAPI(
    title = "Chat With PDF API",
    description = "Chat with GeminiAI about Pdfs",
    version=version
)

#! Routes
from pdf.routes import pdf_router

app.include_router(pdf_router, prefix=f"/api/{version}/pdf", tags = ['Pdf Files'])
