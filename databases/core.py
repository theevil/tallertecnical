from databases import Database
import os
from dotenv import load_dotenv
load_dotenv()

# Database Connection core
database = Database(os.getenv("DATABASE_URL"))

class DatabaseConnection:
    @staticmethod
    async def connect():
        await database.connect()

    @staticmethod
    async def disconnect():
        await database.disconnect()
        
        
        