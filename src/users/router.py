from fastapi import APIRouter, HTTPException, Response, status
from src.users.auth import authenticate_user, create_access_token, get_password_hash, verify_password
from src.users.exceptions import IncorrectEmailOrPasswordExeption, UserAlreadyExistsException
from src.users.schemas import SUserAuth
from src.users.source import UsersData
from src.database import async_session


router  = APIRouter(
    prefix="/auth",
    tags=["Авторизация"],
)

@router.post("/register")
async def register_users(user_data: SUserAuth):
    async with async_session() as session:
        existings_user = await UsersData.find_one_or_none(email=user_data.email)
        if existings_user:
            raise UserAlreadyExistsException
        hashed_password = get_password_hash(user_data.password)
        await UsersData.add(email=user_data.email, password=hashed_password)


@router.post("/login")
async def login_users(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordExeption
    assec_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("user_token", assec_token, httponly=True)
    return assec_token 
            
        
