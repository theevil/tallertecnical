from fastapi import FastAPI
from databases.core import DatabaseConnection

from routes.api import include_routers

app = FastAPI()

@app.on_event("startup")
async def startup():
    await DatabaseConnection.connect()

@app.on_event("shutdown")
async def shutdown():
    await DatabaseConnection.disconnect()

include_routers(app)
