"""AI Classification API routes."""
from fastapi import APIRouter, HTTPException
from services.ai_classification.ai_classification_schema import ClassificationRequest, ClassificationResponse
from services.ai_classification.ai_classification import ai_classification_service

router = APIRouter(prefix="/ai-classification", tags=["AI Classification"])

@router.get("/", response_model=dict)
async def get_classifications():
    """Get available classification categories."""
    try:
        categories = await ai_classification_service.get_categories()
        return {"categories": categories, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/classify", response_model=ClassificationResponse)
async def classify_data(request: ClassificationRequest):
    """Classify the provided data."""
    try:
        result = await ai_classification_service.classify(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))