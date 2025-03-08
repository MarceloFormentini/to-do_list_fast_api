from typing import List

from sqlalchemy import desc
from src.model.config.connection import DBConnectionHandler
from src.model.entities.task import Task
from src.model.repositories.interface.task_repository import TaskRepositoryInterface


class TaskRepository(TaskRepositoryInterface):

	def select_task(self, task_id: int, user_id: int) -> Task:
		with DBConnectionHandler() as db:
			task = (
				db.session
				.query(Task)
				.filter(
					Task.id == task_id,
					Task.user_id == user_id
				)
				.one_or_none()
			)

			return task

	def select_task_all_user(self, user_id: int) -> List[Task]:
		with DBConnectionHandler() as db:
			tasks = (
				db.session
				.query(Task)
				.filter(
					Task.user_id == user_id
				)
				.all()
				.order_by(desc('created_at'))
			)

			return tasks

	def insert(self, task: dict) -> None:
		with DBConnectionHandler() as db:
			try:
				new_task = Task(
					title=task.get('title'),
					description=task.get('description'),
					priority=task.get('priority'),
					status=task.get('status'),
					user_id=task.get('user_id')
				)

				db.session.add(task)
				db.session.commit()

			except Exception as e:
				db.session.rollback()
				raise e

	def update(self, task: dict) -> None:
		with DBConnectionHandler() as db:
			try:
				task_update = self.select_task(task.get('id'), task.get('user_id'))

				task_update.title = task.get('title')
				task_update.description = task.get('description')
				task_update.priority = task.get('priority')
				task_update.status = task.get('status')

				db.session.update(task_update)
				db.session.commit()

			except Exception as e:
				db.session.rollback()
				raise e

	def delete(self, task_id: int) -> None:
		with DBConnectionHandler() as db:
			try:
				task = self.select_task(task_id)

				db.session.delete(task)
				db.session.commit()

			except Exception as e:
				db.session.rollback()
				raise e