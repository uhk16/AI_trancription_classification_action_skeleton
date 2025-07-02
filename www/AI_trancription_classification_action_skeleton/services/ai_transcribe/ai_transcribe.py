"""AI Transcribe service implementation."""
from fastapi import UploadFile
from services.ai_transcribe.ai_transcribe_schema import TranscribeResponse
from typing import List
import random

class AITranscribeService:
    def __init__(self):
        self.supported_formats = ["wav", "mp3", "flac", "ogg", "m4a"]
    
    async def get_supported_formats(self) -> List[str]:
        """Get list of supported audio formats."""
        return self.supported_formats
    
    async def transcribe(self, file: UploadFile) -> TranscribeResponse:
        """Transcribe audio file to text."""
        # Read file content
        content = await file.read()
        
        # Simulate transcription (in real implementation, you'd use a speech-to-text service)
        mock_transcript = f"This is a mock transcription of the uploaded file: {file.filename}. The actual transcription would be processed by a speech-to-text service."
        
        return TranscribeResponse(
            transcript=mock_transcript,
            confidence=random.uniform(0.8, 0.99),
            language="en",
            duration=random.uniform(10, 120),  # Mock duration in seconds
            status="completed",
            word_count=len(mock_transcript.split())
        )

ai_transcribe_service = AITranscribeService()