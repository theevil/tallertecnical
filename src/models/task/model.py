from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field

from src.enitites.task import Priority

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Priority = Priority.Normal
    is_completed: bool = False
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    project_id: UUID

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=500)
    priority: Optional[Priority] = None
    is_completed: Optional[bool] = None
    due_date: Optional[datetime] = None

class TaskResponse(TaskBase):
    id: UUID
    project_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        
    def __repr__(self):
        return f"<Task id={self.id} title={self.title} completed={self.is_completed}>"
