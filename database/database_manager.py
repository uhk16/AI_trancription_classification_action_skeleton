"""Database operations manager."""
from database.database_connection import db_connection

class DatabaseManager:
    def __init__(self):
        self.connection = db_connection
    
    async def create_table(self, table_name: str, schema: str):
        """Create a table with given schema."""
        if self.connection.connection:
            await self.connection.connection.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})")
    
    async def insert_data(self, table: str, data: dict):
        """Insert data into table."""
        if self.connection.connection:
            columns = ", ".join(data.keys())
            values = ", ".join([f"${i+1}" for i in range(len(data))])
            query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
            await self.connection.connection.execute(query, *data.values())
    
    async def query_data(self, query: str):
        """Execute query and return results."""
        if self.connection.connection:
            return await self.connection.connection.fetch(query)
        return []

db_manager = DatabaseManager()