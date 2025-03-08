from model.config.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func

class Task(Base):
	__tablename__ = 'task'
	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String(100), nullable=False)
	description = Column(String(255), nullable=False)
	priority = Column(String(1), nullable=False)
	status = Column(String(1), nullable=False)
	created_at = Column(DateTime, nullable=False, default=func.now())
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)