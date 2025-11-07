import uuid

from fastapi import APIRouter
from .models import models
from ..database import get_db
from sqlalchemy.orm import Session
from ..models.project.service import create_project, get_project_by_id, get_all_projects, delete_project
from fastapi import Depends



project_router = APIRouter(prefix="/project", tags=["project"] )

@project_router.post("/")
def create_new_project(project_data: models.ProjectCreate, db: Session = Depends(get_db)):
    project = create_project(db, project_data)
    return project

@project_router.get("/{project_id}")
def read_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
    project = get_project_by_id(db, project_id)
    return project

@project_router.get("/")
def read_all_projects(db: Session = Depends(get_db)):
    projects = get_all_projects(db)
    return projects

@project_router.delete("/{project_id}")
def delete_existing_project(project_id: uuid.UUID, db: Session = Depends(get_db)):
    success = delete_project(db, project_id)
    return {"deleted": success}
