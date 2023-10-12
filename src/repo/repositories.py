from src.models import Users, Posts, Articles
from src.source.base_class import BaseRepo
from src.database import async_session
from sqlalchemy import select


class UserReposotories(BaseRepo):
    model = Users
    
