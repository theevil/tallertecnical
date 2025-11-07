import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import model
from .service import create_task, get_task_by_id, get_all_tasks, delete_task, update_task
from src.databases.core import DbSession


task_router = APIRouter(prefix="/tasks", tags=["tasks"] )

@task_router.post("/")
def create_new_task(task_data: model.TaskCreate, db: DbSession) -> model.TaskResponse:
    task = create_task(db, task_data)
    return task

@task_router.get("/{task_id}")
def read_task(task_id: str, db: DbSession) -> model.TaskResponse:
    task = get_task_by_id(db, task_id)
    return task

@task_router.get("/")
def read_all_tasks(db: DbSession) -> list[model.TaskResponse]:
    tasks = get_all_tasks(db)
    return tasks

@task_router.delete("/{task_id}")
def delete_existing_task(task_id: uuid.UUID, db: DbSession) -> dict:
    success = delete_task(db, task_id)
    return {"deleted": success}

@task_router.put("/{task_id}")
def update_existing_task(task_id: uuid.UUID, task_data: model.TaskUpdate, db: DbSession) -> model.TaskResponse:
    task = update_task(db, task_id, task_data)
    return task

    