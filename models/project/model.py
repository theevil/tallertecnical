from pydantic import BaseModel

class Project(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True
        
    def __repr__(self):
        return f"<Project id={self.id} name={self.name}>"

class ProjectCreate(BaseModel):
    name: str
    description: str | None = None

    class Config:
        orm_mode = True