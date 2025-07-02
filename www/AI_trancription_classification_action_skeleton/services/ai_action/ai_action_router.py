"""AI Action API routes."""
from fastapi import APIRouter, HTTPException
from services.ai_action.ai_action_schema import ActionRequest, ActionResponse
from services.ai_action.ai_action import ai_action_service

router = APIRouter(prefix="/ai-action", tags=["AI Action"])

@router.get("/", response_model=dict)
async def get_actions():
    """Get all available actions."""
    try:
        actions = await ai_action_service.get_all_actions()
        return {"actions": actions, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/", response_model=ActionResponse)
async def create_action(request: ActionRequest):
    """Create and process a new action."""
    try:
        result = await ai_action_service.process_action(request)
        return ActionResponse(result=result, status="completed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))