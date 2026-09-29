from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

# every path start with /tasks
router = APIRouter(prefix="/tasks", tags=["tasks"])

# any parameter with this type receives a DB session
SessionDep = Annotated[Session, Depends(get_db)]


@router.get("/", response_model=list[schemas.TaskRead])
def list_tasks(
    db: SessionDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
):
    return crud.get_tasks(db, skip=skip, limit=limit)


@router.get("/{task_id}", response_model=schemas.TaskRead)
def get_task(task_id: int, db: SessionDep):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/", response_model=schemas.TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(data: schemas.TaskCreate, db: SessionDep):
    return crud.create_task(db, data)


@router.put("/{task_id}", response_model=schemas.TaskRead)
def update_task(task_id: int, data: schemas.TaskUpdate, db: SessionDep):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db, task, data)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: SessionDep):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, task)
