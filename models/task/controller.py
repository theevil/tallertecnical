import uuid

from fastapi import APIRouter
from .models import models
from .service import create_task, get_task_by_id, get_all_tasks, delete_task, update_task
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends


task_router = APIRouter(prefix="/tasks", tags=["tasks"] )

@task_router.post("/")
def create_new_task(task_data: models.TaskCreate, db: Session = Depends(get_db)):
    task = create_task(db, task_data)
    return task

@task_router.get("/{task_id}")
def read_task(task_id: str, db: Session = Depends(get_db)):
    task = get_task_by_id(db, task_id)
    return task

@task_router.get("/")
def read_all_tasks(db: Session = Depends(get_db)):
    tasks = get_all_tasks(db)
    return tasks

@task_router.delete("/{task_id}")
def delete_existing_task(task_id: uuid.UUID, db: Session = Depends(get_db)):
    success = delete_task(db, task_id)
    return {"deleted": success}

@task_router.put("/{task_id}")
def update_existing_task(task_id: uuid.UUID, task_data: models.TaskUpdate, db: Session = Depends(get_db)):
    task = update_task(db, task_id, task_data)
    return task

    