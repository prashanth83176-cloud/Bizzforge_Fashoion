from fastapi import APIRouter
from app.models.schemas import TextRequest

router = APIRouter()

@router.post("/")
async def summarize(req: TextRequest):
    words = req.text.split()
    return {"summary": " ".join(words[:30])}        