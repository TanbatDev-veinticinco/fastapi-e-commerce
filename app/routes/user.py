from fastapi import APIRouter, HTTPException
from schemas.user import UserCreate, UserOut
from services import user_service


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserOut)
def create_user(user: UserCreate):
    return user_service.create_user(user)


@router.get("/", response_model=list[UserOut])
def get_users():
    return user_service.get_all_user()