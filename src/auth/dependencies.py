from datetime import datetime
from fastapi import Depends, Request
from jose import jwt, JWTError 
from src.config import settings
from src.auth.exceptions import ExpiredTokenExeption, IncorrectTokenFormatException, TokenExistFaliedException, UserFaliedException, UserFaliedException2
from src.auth.repositories import UsersData

def get_token(request: Request):
    token = request.cookies.get("user_token")
    if not token:
        raise TokenExistFaliedException  
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.TOKEN, algorithms=[settings.ALGORITHM])
    except JWTError:
        raise IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if int(expire) < datetime.utcnow().timestamp() or not expire:
        raise ExpiredTokenExeption
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserFaliedException
    user = await UsersData.find_by_id(int(user_id))
    if not user:
        raise UserFaliedException2
    return user
