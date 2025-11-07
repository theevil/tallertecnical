import pytest
from sqlmodel import Session
from src.enitites.project import Project
from src.enitites.task import Task, Priority

def test_create_project(db_session: Session):
    project = Project(name="Test Project", description="Test Description")
    db_session.add(project)
    db_session.commit()
    db_session.refresh(project)
    
    assert project.id is not None
    assert project.name == "Test Project"
    assert project.description == "Test Description"

def test_create_task_with_project(db_session: Session):
    project = Project(name="Test Project")
    db_session.add(project)
    db_session.commit()
    db_session.refresh(project)
    
    task = Task(
        title="Test Task",
        description="Test Description",
        priority=Priority.High,
        project_id=project.id
    )
    db_session.add(task)
    db_session.commit()
    db_session.refresh(task)
    
    assert task.id is not None
    assert task.title == "Test Task"
    assert task.project_id == project.id