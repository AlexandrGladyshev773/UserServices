from fastapi import APIRouter, HTTPException
from src.auth.auth import get_password_hash
from src.auth.schemas import SUserRegister
from src.auth.source import UsersData
from src.database import async_session


router  = APIRouter(
    prefix="/auth",
    tags=["Авторизация"],
)

@router.post("/register")
async def register_users(user_data: SUserRegister):
    async with async_session() as session:
        existings_user = await UsersData.find_one_or_none(email=user_data.email)
        if existings_user:
            raise HTTPException(status_code=500)
        hashed_password = get_password_hash(user_data.password)
        await UsersData.add(username=user_data.username, email=user_data.email, password=hashed_password)

