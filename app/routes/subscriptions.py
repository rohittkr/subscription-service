from fastapi import APIRouter, Depends, HTTPException
from app.utils.auth import verify_jwt

router = APIRouter()

@router.post("/")
def create_subscription(user_id: str = Depends(verify_jwt)):
    return {"message": "Subscription created", "user_id": user_id}

@router.get("/{user_id}")
def get_subscription(user_id: str, current_user: str = Depends(verify_jwt)):
    # Optionally, check if user_id == current_user or allow admins, etc.
    if user_id != current_user:
        raise HTTPException(status_code=403, detail="Not authorized to access this subscription")
    return {"message": f"Subscription for user {user_id}"}

@router.put("/{user_id}")
def update_subscription(user_id: str, current_user: str = Depends(verify_jwt)):
    if user_id != current_user:
        raise HTTPException(status_code=403, detail="Not authorized to update this subscription")
    return {"message": f"Subscription updated for user {user_id}"}

@router.delete("/{user_id}")
def cancel_subscription(user_id: str, current_user: str = Depends(verify_jwt)):
    if user_id != current_user:
        raise HTTPException(status_code=403, detail="Not authorized to cancel this subscription")
    return {"message": f"Subscription cancelled for user {user_id}"}
