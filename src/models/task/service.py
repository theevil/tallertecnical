from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID

from src.enitites.task import Task, Priority
from .model import TaskCreate, TaskResponse, TaskUpdate


def create_task(db_session: Session, task_data: TaskCreate) -> Task:
    task = Task(
        title=task_data.title,
        description=task_data.description,
        priority=task_data.priority,
        is_completed=task_data.is_completed if hasattr(task_data, 'is_completed') else False,
        project_id=task_data.project_id
    )
    db_session.add(task)
    db_session.commit()
    db_session.refresh(task)
    return task

def get_task_by_id(db_session: Session, task_id: UUID) -> Optional[Task]:
    return db_session.query(Task).filter(Task.id == task_id).first()

def get_all_tasks(db_session: Session) -> List[Task]:
    return db_session.query(Task).all()

def delete_task(db_session: Session, task_id: UUID) -> bool:
    task = get_task_by_id(db_session, task_id)
    if task:
        db_session.delete(task)
        db_session.commit()
        return True
    return False

def update_task(db_session: Session, task_id: UUID, task_data: TaskUpdate) -> Optional[Task]:
    task = get_task_by_id(db_session, task_id)
    if task:
        update_data = task_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(task, key, value)
        db_session.commit()
        db_session.refresh(task)
        return task
    return None