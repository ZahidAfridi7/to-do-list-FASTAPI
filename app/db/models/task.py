from sqlalchemy import Column,String,ForeignKey,Integer,DateTime,Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.sql import func
from app.db.models.base import Base

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    title = Column(String,nullable=False)
    description = Column(String,nullable=False)
    status = Column(Boolean)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    