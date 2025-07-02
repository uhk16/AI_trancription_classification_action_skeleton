"""Database connection management."""
import asyncpg
from config.config import config

class DatabaseConnection:
    def __init__(self):
        self.connection = None
    
    async def connect(self):
        """Establish database connection."""
        try:
            self.connection = await asyncpg.connect(config.database_url)
            print("Database connected successfully")
        except Exception as e:
            print(f"Database connection failed: {e}")
    
    async def disconnect(self):
        """Close database connection."""
        if self.connection:
            await self.connection.close()
            print("Database disconnected")

db_connection = DatabaseConnection()