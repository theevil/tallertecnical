from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session

from src.enitites.project import Project
from .model import ProjectCreate, ProjectUpdate, ProjectResponse


def create_project(db_session: Session, project_data: ProjectCreate) -> Project:
    project = Project(
        name=project_data.name,
        description=project_data.description
    )
    db_session.add(project)
    db_session.commit()
    db_session.refresh(project)
    return project

def get_project_by_id(db_session: Session, project_id: UUID) -> Optional[Project]:
    return db_session.get(Project, project_id)

def get_all_projects(db_session: Session) -> List[Project]:
    return db_session.query(Project).all()

def delete_project(db_session: Session, project_id: UUID) -> bool:
    project = get_project_by_id(db_session, project_id)
    if project:
        db_session.delete(project)
        db_session.commit()
        return True
    return False

def update_project(db_session: Session, project_id: UUID, project_data: ProjectUpdate) -> Optional[Project]:
    project = get_project_by_id(db_session, project_id)
    if project:
        update_data = project_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(project, key, value)
        db_session.commit()
        db_session.refresh(project)
        return project
    return None