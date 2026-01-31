from fastapi import APIRouter
from app.models.schemas import StyleSystemRequest, StyleSystemResponse
from app.services.style_service import StyleService

router = APIRouter()
service = StyleService()

@router.post("/generate", response_model=StyleSystemResponse)
async def generate_style(req: StyleSystemRequest):
    """Generate complete style system with colors and typography"""
    return service.generate_style_system(req.idea, req.industry)
