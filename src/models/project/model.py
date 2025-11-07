from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class ProjectBase(BaseModel):
    """Base model for Project with common fields."""
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class ProjectCreate(ProjectBase):
    """Model for creating a new project."""
    pass

class ProjectUpdate(ProjectBase):
    """Model for updating an existing project."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)

class ProjectResponse(ProjectBase):
    """Response model for project data."""
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        
    def __repr__(self):
        return f"<Project id={self.id} name={self.name}>"