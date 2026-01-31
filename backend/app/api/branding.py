from fastapi import APIRouter, HTTPException
from app.models.schemas import BrandRequest, BrandResponse
from app.services.branding_service import BrandingService

router = APIRouter()
service = BrandingService()

@router.post("/", response_model=BrandResponse)
def brand(req: BrandRequest):
    """Create a complete brand with name, slogan, logo, and guide"""
    if not req.idea or len(req.idea.strip()) == 0:
        raise HTTPException(status_code=400, detail="Idea cannot be empty")
    
    try:
        return service.create_brand(req.idea)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))