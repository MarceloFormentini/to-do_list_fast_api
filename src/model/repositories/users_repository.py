from src.model.config.connection import DBConnectionHandler
from src.model.entities.users import Users
from src.model.repositories.interface.users_repository import UsersRepositoryInterface


class UsersRepository(UsersRepositoryInterface):

	def insert(self, user: dict) -> None:
		with DBConnectionHandler() as db:
			try:
				new_user = Users(
					name=user.get('name'),
					email=user.get('email'),
					password=user.get('password')
				)

				db.session.add(new_user)
				db.session.commit()

			except Exception as e:
				db.session.rollback()
				raise e

	def select_user(self, user_id: int) -> Users:
		with DBConnectionHandler() as db:
			user = (
				db.session
				.query(Users)
				.filter(
					Users.id == user_id
				)
				.one_or_none()
			)

			return user

	def select_user_email(self, email: str) -> Users:
		with DBConnectionHandler() as db:
			user = (
				db.session
				.query(Users)
				.filter(
					Users.email == email
				)
				.one_or_none()
			)

			return user
