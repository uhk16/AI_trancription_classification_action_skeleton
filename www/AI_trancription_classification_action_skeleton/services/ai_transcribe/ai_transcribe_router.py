"""AI Transcribe API routes."""
from fastapi import APIRouter, HTTPException, UploadFile, File
from services.ai_transcribe.ai_transcribe_schema import TranscribeResponse
from services.ai_transcribe.ai_transcribe import ai_transcribe_service

router = APIRouter(prefix="/ai-transcribe", tags=["AI Transcribe"])

@router.post("/transcribe", response_model=TranscribeResponse)
async def transcribe_audio(file: UploadFile = File(...)):
    """Transcribe audio file to text."""
    try:
        # Check if file is audio
        if not file.content_type.startswith('audio/'):
            raise HTTPException(status_code=400, detail="File must be an audio file")
        
        result = await ai_transcribe_service.transcribe(file)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/supported-formats", response_model=dict)
async def get_supported_formats():
    """Get list of supported audio formats."""
    formats = await ai_transcribe_service.get_supported_formats()
    return {"supported_formats": formats}