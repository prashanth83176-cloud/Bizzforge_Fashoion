from app.models.schemas import StyleSystemResponse
import hashlib

class StyleService:
    def generate_style_system(self, idea: str, industry: str = "technology") -> StyleSystemResponse:
        """Generate complete style system including colors and typography"""
        try:
            # Hash-based deterministic color generation
            hash_digest = hashlib.md5(f"{idea}{industry}".encode()).hexdigest()
            hash_int = int(hash_digest[:8], 16)
            
            # Define color palettes by industry
            color_palettes = {
                "technology": {
                    "primary": "#1e3a8a",
                    "secondary": "#0f172a",
                    "accent": "#ff6b35"
                },
                "healthcare": {
                    "primary": "#065f46",
                    "secondary": "#ecfdf5",
                    "accent": "#f97316"
                },
                "finance": {
                    "primary": "#1e40af",
                    "secondary": "#eff6ff",
                    "accent": "#dc2626"
                },
                "creative": {
                    "primary": "#7c3aed",
                    "secondary": "#ede9fe",
                    "accent": "#f97316"
                },
                "ecommerce": {
                    "primary": "#be123c",
                    "secondary": "#ffe4e6",
                    "accent": "#06b6d4"
                }
            }
            
            # Get palette based on industry
            palette = color_palettes.get(industry.lower(), color_palettes["technology"])
            
            # Typography recommendations
            typography = {
                "heading_font": "Inter, sans-serif",
                "body_font": "Inter, sans-serif",
                "heading_weight": "700",
                "body_weight": "400",
                "line_height": "1.6"
            }
            
            # Design principles
            design_principles = [
                "Consistency across all touchpoints",
                "Accessibility first - WCAG AA compliant",
                "Mobile-responsive design",
                "Clear visual hierarchy",
                "Minimalist approach - no visual clutter",
                "Emotional resonance with target audience",
                "Scalable from 16px to billboard size"
            ]
            
            return StyleSystemResponse(
                primary_color=palette["primary"],
                secondary_color=palette["secondary"],
                accent_color=palette["accent"],
                typography=typography,
                design_principles=design_principles
            )
        except Exception as e:
            raise ValueError(f"Failed to generate style system: {str(e)}")
