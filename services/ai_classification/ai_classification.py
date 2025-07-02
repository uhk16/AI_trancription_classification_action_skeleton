"""AI Classification service implementation."""
from services.ai_classification.ai_classification_schema import ClassificationRequest, ClassificationResponse
from typing import List, Dict
import random

class AIClassificationService:
    def __init__(self):
        self.default_categories = ["positive", "negative", "neutral", "spam", "ham"]
    
    async def get_categories(self) -> List[str]:
        """Get available classification categories."""
        return self.default_categories
    
    async def classify(self, request: ClassificationRequest) -> ClassificationResponse:
        """Classify the provided text."""
        categories = request.categories or self.default_categories
        
        # Simulate classification with random confidence scores
        predictions = {cat: random.uniform(0, 1) for cat in categories}
        
        # Get the category with highest confidence
        predicted_category = max(predictions, key=predictions.get)
        confidence = predictions[predicted_category]
        
        return ClassificationResponse(
            text=request.text,
            predicted_category=predicted_category,
            confidence=confidence,
            all_predictions=predictions,
            status="completed"
        )

ai_classification_service = AIClassificationService()