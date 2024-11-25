from fastapi import APIRouter, HTTPException, Depends
from typing import List
from models.user_model import User
from config.firebase_config import user_collection

router = APIRouter()





@router.get("/users/", response_model=List[User])
async def list_users():
    users = user_collection.stream()
    return [User(**user.to_dict()) for user in users]

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: str):
    user_ref = user_collection.document(user_id)
    user = user_ref.get()
    if not user.exists:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.to_dict()
    if user_data:
        user_data['id'] = user_id
        return User(**user_data)
    else:
        raise HTTPException(status_code=404, detail="User not created")

@router.post("/users/", response_model=User)
async def create_user(user: User):
    user_ref = user_collection.document(user.id)
    if user_ref.get().exists:
        raise HTTPException(status_code=400, detail="User already exists")
    user_ref.set(user.dict())
    user_ref.set(**user.dict())
    return user

@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: str, user: User):
    user_ref = user_collection.document(user_id)
    user_data = user.dict(exclude_unset=True)
    user_ref.update(user_data)
    updated_user = user_ref.get().to_dict()
    if(updated_user):
        updated_user['id'] = user_id
        return User(**updated_user)
    else:
        return {"detail": "User not updated"}

