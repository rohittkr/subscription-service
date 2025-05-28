from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_plans():
    return [{"id": 1, "name": "Basic", "price": 100, "duration": 30}]
