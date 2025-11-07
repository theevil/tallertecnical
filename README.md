# Taller Técnico - Task Management API

A FastAPI-based Jira Like Task Management API

## 🏗️ Project Structure

```
tallertecnical/
├── src/
│   ├── __init__.py
│   ├── main.py                    # FastAPI application entry point
│   ├── api.py                     # Router configuration
│   │
│   ├── databases/                 # Database configuration
│   │   ├── __init__.py
│   │   ├── core.py
│   │   └── database.py           # SQLModel engine and session management
│   │
│   ├── enitites/                  # Database entities (SQLModel tables)
│   │   ├── __init__.py
│   │   ├── project.py            # Project entity
│   │   └── task.py               # Task entity with Priority enum
│   │
│   └── models/                    # API models and business logic
│       ├── __init__.py
│       │
│       ├── project/
│       │   ├── __init__.py
│       │   ├── controller.py     # Project API endpoints
│       │   ├── model.py          # Pydantic models (Request/Response)
│       │   └── service.py        # Business logic layer
│       │
│       └── task/
│           ├── __init__.py
│           ├── controller.py     # Task API endpoints
│           ├── model.py          # Pydantic models (Request/Response)
│           └── service.py        # Business logic layer
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py               # Pytest configuration and fixtures
│   │
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_api.py           # API integration tests
│   │
│   └── unit/
│       ├── __init__.py
│       └── test_models.py        # Unit tests for models
│
├── .env                          # Environment variables (local)
├── .env.docker                   # Environment variables (Docker)
├── .dockerignore                 # Docker ignore patterns
├── Dockerfile                    # Docker image definition
├── docker-compose.yml            # Multi-container Docker setup
├── requirements.txt              # Python dependencies
├── Pipfile                       # Pipenv configuration
├── Pipfile.lock                  # Locked dependencies
├── pytest.ini                    # Pytest configuration
└── README.md                     # This file
```

## 🚀 Features

- **Projects Management**: Create, read, update, and delete projects
- **Tasks Management**: Manage tasks with priority levels and completion status
- **Priority System**: 5 priority levels (Normal, Low, Medium, High, Top)
- **Relationships**: Tasks are linked to projects with cascade deletion
- **Timestamps**: Automatic created_at and updated_at tracking
- **UUID Primary Keys**: Using UUIDs for all entities
- **API Documentation**: Auto-generated Swagger UI and ReDoc

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.121.0
- **Database**: PostgreSQL 15
- **ORM**: SQLModel (SQLAlchemy + Pydantic)
- **Async DB Driver**: asyncpg
- **Validation**: Pydantic v2
- **Testing**: pytest, pytest-asyncio, pytest-cov
- **Containerization**: Docker & Docker Compose

## 📦 Installation

### Using Docker (Recommended)

1. **Start the services**:
   ```bash
   docker-compose up -d
   ```

2. **View logs**:
   ```bash
   docker-compose logs -f
   ```

3. **Stop the services**:
   ```bash
   docker-compose down
   ```

### Local Development

1. **Install dependencies**:
   ```bash
   pipenv install --dev
   ```

2. **Activate virtual environment**:
   ```bash
   pipenv shell
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

4. **Run the application**:
   ```bash
   uvicorn src.main:app --reload
   ```

## 🔌 API Endpoints

### Projects

- `POST /projects/` - Create a new project
- `GET /projects/` - List all projects
- `GET /projects/{project_id}` - Get a specific project
- `PUT /projects/{project_id}` - Update a project
- `DELETE /projects/{project_id}` - Delete a project

### Tasks

- `POST /tasks/` - Create a new task
- `GET /tasks/` - List all tasks
- `GET /tasks/{task_id}` - Get a specific task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

## 📊 Database Schema

### Projects Table
- `id` (UUID, Primary Key)
- `name` (String, Unique, Required)
- `description` (String, Optional)
- `created_at` (Timestamp with timezone)
- `updated_at` (Timestamp with timezone)

### Tasks Table
- `id` (UUID, Primary Key)
- `title` (String, Required)
- `description` (String, Optional)
- `priority` (Enum: Normal, Low, Medium, High, Top)
- `is_completed` (Boolean, Default: false)
- `due_date` (Timestamp with timezone, Optional)
- `project_id` (UUID, Foreign Key → projects.id, CASCADE)
- `created_at` (Timestamp with timezone)
- `updated_at` (Timestamp with timezone)

## 🧪 Testing

Run tests with coverage:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/unit/test_models.py

# Run integration tests only
pytest tests/integration/
```

## 🌐 Access Points

- **API**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **PostgreSQL**: localhost:5432
  - Database: `jiradb`
  - User: `postgres`
  - Password: `postgres`

## 🔧 Environment Variables

```bash
# Database connection string
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/jiradb

# For Docker (uses service name as host)
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/jiradb
```

## 📝 Architecture Patterns

### Layered Architecture

1. **Controller Layer** (`controller.py`): Handles HTTP requests/responses and routing
2. **Service Layer** (`service.py`): Contains business logic and data validation
3. **Entity Layer** (`enitites/`): Database models using SQLModel
4. **Model Layer** (`models/`): Pydantic schemas for API request/response validation

### Design Principles

- **Separation of Concerns**: Clear separation between API, business logic, and data layers
- **Dependency Injection**: Database sessions injected via FastAPI dependencies
- **Type Safety**: Full type hints throughout the codebase
- **Async/Await**: Asynchronous database operations for better performance

## 🐳 Docker Configuration

### Services

- **postgres**: PostgreSQL 15 Alpine with health checks
- **fastapi**: Python 3.10 application with hot reload

