import pytest
from fastapi import status

def test_create_project(client, test_project_data):
    response = client.post("/projects/", json=test_project_data)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["name"] == test_project_data["name"]
    assert "id" in data
    return data

def test_get_project(client, test_project_data):
    create_response = client.post("/projects/", json=test_project_data)
    project_id = create_response.json()["id"]
    
    response = client.get(f"/projects/{project_id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == project_id
    assert data["name"] == test_project_data["name"]

def test_create_task(client, test_project_data, test_task_data):
    project = client.post("/projects/", json=test_project_data).json()
    
    test_task_data["project_id"] = project["id"]
    response = client.post("/tasks/", json=test_task_data)
    
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == test_task_data["title"]
    assert data["project_id"] == str(project["id"])