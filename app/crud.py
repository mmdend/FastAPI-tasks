from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models, schemas


def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> list[models.Task]:
    stmt = select(models.Task).order_by(models.Task.id).offset(skip).limit(limit)
    return db.scalars(stmt).all()


def get_task(db: Session, task_id: int) -> models.Task | None:
    return db.get(models.Task, task_id)


def create_task(db: Session, data: schemas.TaskCreate) -> models.Task:
    task = models.Task(title=data.title, description=data.description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def update_task(
    db: Session, task: models.Task, data: schemas.TaskUpdate
) -> models.Task:
    task.title = data.title
    task.description = data.description
    task.is_completed = data.is_completed
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task: models.Task) -> None:
    db.delete(task)
    db.commit()
