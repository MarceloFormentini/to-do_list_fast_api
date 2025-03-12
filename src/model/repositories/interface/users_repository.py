from abc import ABC, abstractmethod
from src.model.entities.users import Users

class UsersRepositoryInterface(ABC):

	@abstractmethod
	def insert(self, user: dict) -> None:
		pass

	@abstractmethod
	def select_user(self, user_id: int) -> Users:
		pass

	@abstractmethod
	def select_user_email(self, email: str) -> Users:
		pass

	@abstractmethod
	def authenticate_user(self, email: str, password: str) -> Users:
		pass