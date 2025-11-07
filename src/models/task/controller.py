from uuid import UUID
from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from . import model, service
from src.databases.database import get_session


task_router = APIRouter(prefix="/tasks", tags=["tasks"])

@task_router.post(
    "/",
    response_model=model.TaskResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_task(
    task_data: model.TaskCreate,
    db: Session = Depends(get_session)
) -> model.TaskResponse:
    try:
        task = service.create_task(db, task_data)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create task"
            )
        return task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@task_router.get(
    "/{task_id}",
    response_model=model.TaskResponse
)
async def get_task(
    task_id: UUID,
    db: Session = Depends(get_session)
) -> model.TaskResponse:
    task = service.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return task

@task_router.get(
    "/",
    response_model=List[model.TaskResponse]
)
async def get_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_session)
) -> List[model.TaskResponse]:
    tasks = service.get_all_tasks(db)
    return tasks[skip : skip + limit] if limit else tasks

@task_router.put(
    "/{task_id}",
    response_model=model.TaskResponse
)
async def update_task(
    task_id: UUID,
    task_data: model.TaskUpdate,
    db: Session = Depends(get_session)
) -> model.TaskResponse:
    task = service.update_task(db, task_id, task_data)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return task

@task_router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_task(
    task_id: UUID,
    db: Session = Depends(get_session)
) -> None:
    success = service.delete_task(db, task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return None