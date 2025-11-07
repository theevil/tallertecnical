from uuid import UUID
from typing import List
from fastapi import APIRouter, HTTPException, status, Depends

from . import model, service
from src.databases.database import get_session as get_db
from sqlalchemy.orm import Session

project_router = APIRouter(prefix="/projects", tags=["projects"])

@project_router.post(
    "/",
    response_model=model.ProjectResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_project(
    project_data: model.ProjectCreate,
    db: Session = Depends(get_db)
) -> model.ProjectResponse:
    try:
        project = service.create_project(db, project_data)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Failed to create project"
            )
        return project
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@project_router.get(
    "/{project_id}",
    response_model=model.ProjectResponse
)
async def get_project(
    project_id: UUID,
    db: Session = Depends(get_db)
) -> model.ProjectResponse:
    project = service.get_project_by_id(db, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with ID {project_id} not found"
        )
    return project

@project_router.get(
    "/",
    response_model=List[model.ProjectResponse]
)
async def get_projects(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> List[model.ProjectResponse]:
    projects = service.get_all_projects(db)
    return projects[skip : skip + limit] if limit else projects

@project_router.put(
    "/{project_id}",
    response_model=model.ProjectResponse
)
async def update_project(
    project_id: UUID,
    project_data: model.ProjectUpdate,
    db: Session = Depends(get_db)
) -> model.ProjectResponse:
    project = service.update_project(db, project_id, project_data)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with ID {project_id} not found"
        )
    return project

@project_router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_project(
    project_id: UUID,
    db: Session = Depends(get_db)
) -> None:
    success = service.delete_project(db, project_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with ID {project_id} not found"
        )
    return None