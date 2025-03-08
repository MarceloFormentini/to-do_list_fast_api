from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interface.users_repository import UsersRepositoryInterface


class UsersCreator:
	def __init__(self, users_repository: UsersRepositoryInterface):
		self.__users_repository = users_repository

	def create(self, http_request: HttpRequest) -> HttpResponse:
		users_info = http_request.body['data']
		self.__check_email(email=users_info['email'])
		self.__insert_user(users_info=users_info)
		return self.__format_response(users_info=users_info)

	def __check_email(self, email: str):
		response = self.__users_repository.select_user_email(email=email)
		if response:
			raise Exception("Email already exists")

	def __insert_user(self, users_info: dict):
		self.__users_repository.insert(user=users_info)

	def __format_response(self, users_info: str) -> HttpResponse:
		return HttpResponse(
			body={
				"message": "Event created successfully",
				"data": {
					"Type": "Event",
					"count": 1,
					"atributes": {
						"name": users_info['name'],
						"email": users_info['email']
					}
				}
			},
			status_code=201
		)