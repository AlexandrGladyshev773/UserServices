from src.models import Users
from src.source.base_class import BaseRepo


class UsersData(BaseRepo):
    model = Users
