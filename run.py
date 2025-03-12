from fastapi import FastAPI
from fastapi import HTTPException
from src.main.exception.exception_handler import http_exception_handler
from src.main.routes.users_routes import users_router
from src.main.routes.task_routes import task_router

app = FastAPI()
app.include_router(users_router)
app.include_router(task_router)

# Adicionado tratamento de exceções globalmente
app.add_exception_handler(HTTPException, http_exception_handler)