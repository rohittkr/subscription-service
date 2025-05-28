# app/routes/token.py
from fastapi import APIRouter
from pydantic import BaseModel
import jwt
from datetime import datetime, timedelta
from app.config import JWT_SECRET, JWT_ALGORITHM

router = APIRouter()

class TokenRequest(BaseModel):
    user_id: str

@router.post("/token")
def generate_token(data: TokenRequest):
    payload = {
        "user_id": data.user_id,
        "exp": datetime.utcnow() + timedelta(hours=1)  # token valid for 1 hour
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"token": token}
