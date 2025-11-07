from pydantic import Field
from sqlmodel import SQLModel, Column, String, DateTime
from typing import Optional
from datetime import datetime
from uuid import UUID

class Project(SQLModel, table=True):
    id: UUID = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column("name", String, nullable=False, unique=True))
    description: Optional[str] = Field(default=None, sa_column=Column("description", String, nullable=True))
    created_at: datetime = Field(default_factory=datetime.utcnow, sa_column=Column("created_at", DateTime, nullable=False))
    
    