from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr
from src.config import settings
from src.users.source import UsersData

pwd_context = CryptContext(schemes=['bcrypt'], deprecated=['auto'])

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(input_password, hashed_password) -> bool:
    return pwd_context.verify(input_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = dict(data)
    expire = datetime.utcnow() + timedelta(minutes=50)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.TOKEN, algorithm=settings.ALGORITHM)
    return encoded_jwt

async def authenticate_user(email: EmailStr, password: str):
    user = await UsersData.find_one_or_none(email=email)
    if not user and not verify_password(password, user.id):
        return None
    return user

