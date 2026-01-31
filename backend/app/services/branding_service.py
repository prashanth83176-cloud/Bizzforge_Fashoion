from app.ai.granite import granite_chat
from app.ai.groq_llama import llama_generate
from app.ai.sdxl import generate_logo
from app.models.schemas import BrandResponse

class BrandingService:
    def create_brand(self, idea: str) -> BrandResponse:
        """Generate brand components"""
        try:
            return BrandResponse(
                name=llama_generate(f"Brand name for {idea}"),
                slogan=llama_generate(f"Slogan for {idea}"),
                logo=generate_logo(idea),
                guide=granite_chat(idea)
            )
        except Exception as e:
            raise ValueError(f"Failed to create brand: {str(e)}")