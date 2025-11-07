from fastapi import FastAPI
from src.api import include_routers
from src.databases.database import create_db_and_tables

app = FastAPI()

include_routers(app)

# Create database tables on startup
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
