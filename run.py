from fastapi import FastAPI
from src.main.routes.users_routes import users_router
from src.main.routes.task_routes import task_router

app = FastAPI()
app.include_router(users_router)
app.include_router(task_router)