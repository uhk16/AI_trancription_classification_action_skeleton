"""Application entry point."""
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from config.config import config
from database.database_connection import db_connection
from services.ai_action.ai_action_router import router as ai_action_router
from services.ai_classification.ai_classification_router import router as ai_classification_router
from services.ai_transcribe.ai_transcribe_router import router as ai_transcribe_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up...")
    await db_connection.connect()
    yield
    # Shutdown
    print("Shutting down...")
    await db_connection.disconnect()

app = FastAPI(
    title="AI Services API",
    description="A comprehensive API for AI services including actions, classification, and transcription",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ai_action_router)
app.include_router(ai_classification_router)
app.include_router(ai_transcribe_router)

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "AI Services API",
        "version": "1.0.0",
        "services": ["ai-action", "ai-classification", "ai-transcribe"],
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "port": config.port}

def main():
    """Run the FastAPI application."""
    uvicorn.run(
        "main:app",
        host=config.host,
        port=config.port,
        reload=config.debug,
        log_level="info"
    )

if __name__ == "__main__":
    main()