from fastapi import APIRouter
from app.models.schemas import BrandRequest, CopyResponse
from app.services.copy_service import CopyService

router = APIRouter()
service = CopyService()

@router.post("/generate", response_model=CopyResponse)
async def generate_content(req: BrandRequest):
    """Generate marketing copy for all platforms"""
    return service.generate_copy(req.idea)