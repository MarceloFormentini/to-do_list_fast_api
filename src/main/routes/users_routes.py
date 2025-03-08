
from fastapi import APIRouter
from src.model.repositories.users_repository import UsersRepository


users_router = APIRouter()

@users_router.post("/users")
def select_user():
	return UsersRepository.insert_user()

@users_router.get("/users")
def select_user():
	return UsersRepository.select_user()