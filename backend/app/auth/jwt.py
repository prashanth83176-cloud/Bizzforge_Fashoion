import jwt
from datetime import datetime, timedelta
from app.config import settings

def create_token(username: str) -> str:
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")