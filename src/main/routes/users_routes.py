
from fastapi import APIRouter
from fastapi import Request
from fastapi import HTTPException
from src.model.repositories.users_repository import UsersRepository
from src.validators.users_creator_validator import users_creator_validator

users_router = APIRouter()

@users_router.post("/users")
def select_user(request: Request):
	users_creator_validator(request=request)

	# repository = UsersRepository()
	# repository.insert(user=user)

@users_router.get("/users/{user_id}")
def select_user(user_id: int):
	repository = UsersRepository()
	user = repository.select_user(user_id=user_id)

	if not user:
		raise HTTPException(status_code=404, detail="User not found")

	return user