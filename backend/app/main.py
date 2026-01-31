from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.api import branding, content, sentiment, summarize, style
from app.config import settings

app = FastAPI(
    title="BizForge API",
    description="AI-powered branding and content generation",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Redirect to API documentation"""
    return RedirectResponse(url="/docs")

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "api_keys_configured": bool(settings.GROQ_API_KEY and settings.HF_API_KEY)
    }

app.include_router(branding.router, prefix="/branding", tags=["Branding"])
app.include_router(content.router, prefix="/content", tags=["Content"])
app.include_router(sentiment.router, prefix="/sentiment", tags=["Sentiment"])
app.include_router(summarize.router, prefix="/summarize", tags=["Summarize"])
app.include_router(style.router, prefix="/style", tags=["Style System"])