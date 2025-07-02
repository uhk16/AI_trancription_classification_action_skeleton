"""Application configuration settings."""
import os
from typing import Optional

class Config:
    def __init__(self):
        self.database_url: str = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/mydb")
        self.api_key: str = os.getenv("API_KEY", "your_api_key_here")
        self.debug: bool = os.getenv("DEBUG", "True").lower() == "true"
        self.host: str = os.getenv("HOST", "0.0.0.0")
        self.port: int = int(os.getenv("PORT", "5021"))

config = Config()