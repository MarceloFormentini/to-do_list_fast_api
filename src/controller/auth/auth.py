from fastapi import HTTPException, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from src.model.repositories.users_repository import UsersRepository


security = HTTPBasic()

class Auth:

	def get_current_user(credentials: HTTPBasicCredentials = Security(security)):
		user = UsersRepository.authenticate_user(
			email=credentials.username,
			password=credentials.password
		)

		if not user:
			raise HTTPException(status_code=401, detail="Não autorizado")

		return user