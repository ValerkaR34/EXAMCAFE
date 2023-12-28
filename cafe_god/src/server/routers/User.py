from typing import List
import fastapi
from fastapi import HTTPException
from server.sql_base.models import User

from server.resolvers.User import new_user, get_user, get_all_users, delete_user, update_user

users_router = fastapi.APIRouter(prefix="/users", tags=["Users"])

@users_router.get("/")
def start_page():
    return ""

@users_router.get('/get/')
def get_users() -> List[User]:
    return get_all_users()

@users_router.get('/get/{user_id}')
def get_current_user(user_id: int) -> User:
    return get_user(user_id)

@users_router.post('/new/')
def add_user(user: User) -> User:
    return new_user(user)

@users_router.put('/update/{user_id}')
def update_user_info(user_id: int, updated_user: User) -> User:
    return update_user(updated_user, user_id)

@users_router.delete("/delete/{user_id}")
def delete_user_info(user_id: int):
    result = delete_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
