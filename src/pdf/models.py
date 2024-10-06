from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime
import uuid

Base = declarative_base()

class Pdf(Base):
    __tablename__ = 'pdfs'

    id = Column(Integer, primary_key=True, index=True)
    unique_value = Column(String, default=lambda: str(uuid.uuid4()))
    
    title = Column(String, index=True)
    page_count = Column(Integer)
    file_size = Column(Integer)
    context_text = Column(String)
    
    is_deleted = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    modified = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
