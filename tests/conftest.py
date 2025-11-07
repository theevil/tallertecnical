import os
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker
from typing import Generator, Any, Callable

from src.main import app
from src.databases.database import get_session

TEST_DATABASE_URL = "sqlite:///:memory:"
test_engine = create_engine(
    TEST_DATABASE_URL, 
    connect_args={"check_same_thread": False}, 
    echo=True
)

# Crear una sesión de prueba
TestingSessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=test_engine
)

@pytest.fixture(scope="function")
def db_session() -> Generator[Session, None, None]:
    SQLModel.metadata.create_all(test_engine)
    
    connection = test_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def client(db_session: Session) -> TestClient:
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    
    app.dependency_overrides[get_session] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()

@pytest.fixture(scope="function")
def test_project_data() -> dict[str, Any]:
    return {
        "name": "Test Project",
        "description": "Test Description"
    }

@pytest.fixture(scope="function")
def test_task_data() -> dict[str, Any]:
    return {
        "title": "Test Task",
        "description": "Test Task Description",
        "priority": "High",
        "project_id": None  
    }