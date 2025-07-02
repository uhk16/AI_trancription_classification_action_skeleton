"""AI Transcribe data schemas."""
from pydantic import BaseModel
from typing import Optional, List

class TranscribeRequest(BaseModel):
    audio_url: Optional[str] = None
    language: Optional[str] = "en"
    format: Optional[str] = "wav"

class TranscribeResponse(BaseModel):
    transcript: str
    confidence: float
    language: str
    duration: float
    status: str
    word_count: int