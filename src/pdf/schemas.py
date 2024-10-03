from pydantic import BaseModel, Field
from datetime import datetime
import uuid

class Pdf(BaseModel):
    id:int
    title:str
    page_count : int
    file_size : int
    
    unique_value : str = Field(default_factory=lambda : str(uuid.uuid4())) 
    
    is_deleted : bool
    created: datetime
    modified: datetime
    