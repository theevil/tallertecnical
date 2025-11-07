from typing import Optional
from pydantic import Field
from sqlalchemy import Boolean
from sqlmodel import SQLModel, Column, String, DateTime
from datetime import datetime
from uuid import UUID
from .models import models


class Task(SQLModel, table=True):
    id: UUID = Field(default=None, primary_key=True)
    project_id: UUID = models.ForeignKey('project.id', related_name='tasks', on_delete=models.CASCADE)
    title: str = Field(sa_column=Column("title", String, nullable=False))
    priority: Optional[int] = Field(default=None, sa_column=Column("priority", String, nullable=True))
    completed: bool = Field(default=False, sa_column=Column("completed", Boolean, nullable=False))
    due_date: Optional[datetime] = Field(default=None, sa_column=Column("due_date", DateTime, nullable=True))
    
    