from sqlmodel import SQLModel, Column, String, DateTime, Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy.dialects.postgresql import UUID as PG_UUID

class Project(SQLModel, table=True):
    __tablename__ = "projects"
    
    id: UUID = Field(
        default_factory=uuid4,
        sa_column=Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    )
    name: str = Field(sa_column=Column(String, nullable=False, unique=True))
    description: Optional[str] = Field(default=None, sa_column=Column(String, nullable=True))
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), nullable=False, server_default="now()")
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(DateTime(timezone=True), nullable=False, server_default="now()", onupdate=datetime.utcnow)
    )
    
    def __repr__(self):
        return f"<Project id={self.id} name={self.name}>"
        
    