from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class TaskCreate(BaseModel):
    id : int
    title : str
    description:str
    status:bool
    created_at:datetime=None
    
    class Config:
        from_attributes = True 
    
class TaskResponse(BaseModel):
    id:int
    title:str
    description:str
    status:bool
    created_at:datetime
    
    class Config:
        orm_mode=True

class TaskUpdate(BaseModel):
    title:Optional[str]=None
    description:Optional[str]=None
    status:Optional[bool]=None
    created_at:Optional[datetime]=None
    
    
    
            
            