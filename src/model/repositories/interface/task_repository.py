from abc import ABC, abstractmethod
from asyncio import Task
from typing import List


class TaskRepositoryInterface(ABC):
	@abstractmethod
	def select_task(self, task_id: int, user_id: int) -> Task:
		pass

	@abstractmethod
	def select_task_all_user(self, user_id: int) -> List[Task]:
		pass

	@abstractmethod
	def insert(self, task: dict) -> None:
		pass

	@abstractmethod
	def update(self, task: dict) -> None:
		pass

	@abstractmethod
	def delete(self, task_id: int) -> None:
		pass