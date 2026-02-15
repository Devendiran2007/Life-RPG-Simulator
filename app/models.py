from sqlalchemy import Column , Integer ,String , BOOLEAN , TIMESTAMP , ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    username = Column(String(50), nullable = False, unique=True)
    email = Column(String(100) , nullable= False , unique = True)
    password  = Column(String(100), nullable = False)

    level = Column(Integer, nullable = False)
    exp = Column(Integer, nullable = False)
    coins = Column(Integer, nullable = False)
    
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = func.now())

    relationship = relationship("Quest", back_populates = "owner" , cascade = "all, delete")


class Quest(Base):
    __tablename__ = "quests"

    id = Column(Integer, primary_key = True)
    title = Column(String(100), nullable = False)
    description = Column(String(255), nullable = False)
    difficulty = Column(Integer, nullable = False)
    xp_reward = Column(Integer, nullable = False)
    coin_reward = Column(Integer, nullable = False)
    
    is_completed = Column(BOOLEAN, nullable = False)

    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User" , back_populates  = "relationship")

    created_at = Column(TIMESTAMP(timezone = True), server_default = func.now())

    
    