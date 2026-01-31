from fastapi import APIRouter
from app.models.schemas import TextRequest

router = APIRouter()

@router.post("/")
async def sentiment(req: TextRequest):
    text = req.text.lower()
    if any(word in text for word in ["good", "great", "excellent"]):
        return {"sentiment": "positive"}
    if any(word in text for word in ["bad", "poor", "terrible"]):
        return {"sentiment": "negative"}
    return {"sentiment": "neutral"}
