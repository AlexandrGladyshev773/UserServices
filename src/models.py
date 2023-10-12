from sqlalchemy import Column, Integer, String, JSON, TIMESTAMP, ForeignKey, Text
from sqlalchemy.orm import relationship
from src.database import Base




class Articles(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    author = relationship("Users", back_populates="articles")
    posts = relationship("Posts", back_populates="article")

class Posts(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    article_id = Column(Integer, ForeignKey('articles.id'))
    
    author = relationship("Users", back_populates="posts")
    article = relationship("Articles", back_populates="posts")
    
class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    
    articles = relationship("Articles", back_populates="author")
    posts = relationship("Posts", back_populates="author")