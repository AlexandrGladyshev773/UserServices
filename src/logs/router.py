from fastapi import APIRouter
from src.database import async_session
from src.repo.repositories import UserReposotories


router  = APIRouter(
    prefix="/users",
    tags=["Список пользователей"],
)

@router.get("")
async def get_users():
    async with async_session() as session:
        return await UserReposotories.find_all()


