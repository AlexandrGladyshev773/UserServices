from fastapi import APIRouter, Depends

from src.models import Users
from src.users.dependencies import get_current_user
from src.users.source import UsersData

router = APIRouter(
    prefix="/posts",
    tags=["Посты"]
)

@router.get("")
async def get_posts(user: Users = Depends(get_current_user)):
    print(user, user.email)
    # return await UsersData.find_all()