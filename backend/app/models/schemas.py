from pydantic import BaseModel
from typing import List

class BrandRequest(BaseModel):
    idea: str

class TextRequest(BaseModel):
    text: str

class BrandResponse(BaseModel):
    name: str
    slogan: str
    logo: str
    guide: str

class CopyRequest(BaseModel):
    idea: str
    platform: str = "general"  # social, landing, product, email

class CopyResponse(BaseModel):
    social_posts: List[str]
    landing_headline: str
    product_description: str
    email_subject: str

class StyleSystemRequest(BaseModel):
    idea: str
    industry: str = "technology"

class StyleSystemResponse(BaseModel):
    primary_color: str
    secondary_color: str
    accent_color: str
    typography: dict
    design_principles: List[str]