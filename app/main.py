from fastapi import FastAPI

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


@app.get("/", tags=["health"])
def health_check():
    return {"status": "ok"}
