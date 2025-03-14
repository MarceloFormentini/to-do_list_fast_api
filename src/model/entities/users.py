from src.model.config.base import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

class Users(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(100), nullable=False)
	email = Column(String(100), nullable=False)
	password = Column(String(100), nullable=False)
	created_at = Column(DateTime, nullable=False, default=func.now())