"""AI Action data schemas."""
from pydantic import BaseModel
from typing import Dict, Any, Optional

class ActionRequest(BaseModel):
    action_type: str
    parameters: Dict[str, Any]
    user_id: Optional[str] = None

class ActionResponse(BaseModel):
    result: Dict[str, Any]
    status: str
    message: Optional[str] = None