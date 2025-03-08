from fastapi import APIRouter

from src.model.repositories.task_repository import TaskRepository

task_router = APIRouter()

@task_router.post("/task/{user_id}/{task_id}")
def select_task(user_id: int, task_id: int):
	return TaskRepository.select_task(user_id, task_id)

@task_router.get("/task/{user_id}")
def get_task_all_user(user_id: int):
	return TaskRepository.select_task_all_user(user_id)

@task_router.post("/task")
def insert(task: dict):
	return TaskRepository.insert(task)

@task_router.put("/task")
def update(task: dict):
	return TaskRepository.update(task)

@task_router.delete("/task/{task_id}")
def delete(task_id: int):
	return TaskRepository.delete(task_id)