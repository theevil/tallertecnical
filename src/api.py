
from .models.project.controller import project_router
from .models.task.controller import task_router

def include_routers(app):
    app.include_router(project_router)
    app.include_router(task_router)