from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.config import settings, root_path


engine = create_async_engine(settings.DATABASE_URL)

async_session = sessionmaker(engine, class_=AsyncSession,
                             expire_on_commit=False)


@as_declarative()
class Base:
    pass
