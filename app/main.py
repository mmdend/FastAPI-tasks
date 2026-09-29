from fastapi import FastAPI

from app import models  # noqa: F401 (for ruff)
from app.database import Base, engine
from app.routers import tasks

# Create the tables if they do not exist.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description=(
        "A simple and efficient Todo management API built with FastAPI. "
        "This API allows users to create, retrieve, update, and delete tasks. "
    ),
    version="1.0.0",
    contact={
        "name": "Mohammad (Mehrad) Mousapour",
        "url": "https://http://github.com/mmdend",
        "email": "mmdend.dev@gmail.com",
    },
)

app.include_router(tasks.router)
