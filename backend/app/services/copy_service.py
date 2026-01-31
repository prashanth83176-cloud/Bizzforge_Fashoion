from app.ai.groq_llama import llama_generate
from app.models.schemas import CopyResponse

class CopyService:
    def generate_copy(self, idea: str) -> CopyResponse:
        """Generate marketing copy for various platforms"""
        try:
            # Generate social media posts
            social_post_1 = llama_generate(f"Write an engaging social media post for {idea}")
            social_post_2 = llama_generate(f"Create a trending social media hook for {idea}")
            social_post_3 = llama_generate(f"Write viral social content about {idea}")
            
            # Generate landing page headline
            landing_headline = llama_generate(f"Create a compelling landing page headline for {idea}")
            
            # Generate product description
            product_desc = llama_generate(f"Write a professional product description for {idea}")
            
            # Generate email subject
            email_subject = llama_generate(f"Create an engaging email subject line for {idea}")
            
            return CopyResponse(
                social_posts=[social_post_1, social_post_2, social_post_3],
                landing_headline=landing_headline,
                product_description=product_desc,
                email_subject=email_subject
            )
        except Exception as e:
            raise ValueError(f"Failed to generate copy: {str(e)}")
