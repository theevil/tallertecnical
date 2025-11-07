from pydantic import BaseModel

class Task(BaseModel):
    id: int
    project_id: int
    title: str
    priority: int | None = None
    completed: bool
    due_date: str | None = None

    class Config:
        orm_mode = True
        
    def __repr__(self):
        return f"<Task id={self.id} title={self.title} completed={self.completed}>"

class TaskCreate(BaseModel):
    project_id: int
    title: str
    priority: int | None = None
    due_date: str | None = None

    class Config:
        orm_mode = True