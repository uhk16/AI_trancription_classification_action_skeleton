"""AI Classification data schemas."""
from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class ClassificationRequest(BaseModel):
    text: str
    categories: Optional[List[str]] = None
    confidence_threshold: Optional[float] = 0.5

class ClassificationResponse(BaseModel):
    text: str
    predicted_category: str
    confidence: float
    all_predictions: Dict[str, float]
    status: str