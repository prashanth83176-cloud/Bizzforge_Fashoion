from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "BizForge"
    GROQ_API_KEY: Optional[str] = None
    HF_API_KEY: Optional[str] = None
    JWT_SECRET: str = "dev-secret-key-change-in-production"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
