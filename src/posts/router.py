from fastapi import APIRouter, Depends

from src.models import Users
from src.auth.dependencies import get_current_user
from src.posts.source import PostsData

router = APIRouter(
    prefix="/posts",
    tags=["Посты"]
)

@router.get("")
async def get_posts(user: Users = Depends(get_current_user)):
    return await PostsData.find_all(user_id=1)
