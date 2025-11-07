import enum
from typing import Optional
from sqlalchemy import Boolean, Enum, ForeignKey
from sqlmodel import SQLModel, Column, String, DateTime, Field
from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class Priority(enum.Enum):
    Normal = 0
    Low = 1
    Medium = 2
    High = 3
    Top = 4


class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    
    id: UUID = Field(
        default_factory=uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    )
    title: str = Field(sa_column=Column(String, nullable=False))
    description: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))
    priority: Priority = Field(
        sa_column=Column(Enum(Priority), nullable=False), 
        default=Priority.Normal
    )
    is_completed: bool = Field(
        sa_column=Column(Boolean, nullable=False, server_default="false"),
        default=False
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), nullable=False, server_default="now()")
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), nullable=False, server_default="now()", onupdate=datetime.utcnow)
    )
    due_date: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), nullable=True)
    )
    project_id: UUID = Field(
        sa_column=Column(
            PG_UUID(as_uuid=True),
            ForeignKey("projects.id", ondelete="CASCADE"),
            nullable=False
        )
    )
    
    def __repr__(self):
        return f"<Task id={self.id} title={self.title} completed={self.is_completed}>"