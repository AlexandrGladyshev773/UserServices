from pydantic_settings import BaseSettings
from pydantic import validator

class AppSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str


    @property
    def DATABASE_URL(self):
        root_value = f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return root_value

    class Config:
        env_file = ".env"

settings = AppSettings()
root_path = settings.DATABASE_URL

