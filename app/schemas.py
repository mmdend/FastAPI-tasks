from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    """POST /tasks/"""

    title: str = Field(..., min_length=1, max_length=255)
    description: str | None = None


class TaskUpdate(BaseModel):
    """PUT /tasks/{task_id} (full update)"""

    title: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    is_completed: bool = False


class TaskRead(BaseModel):
    """Response model returned to clients"""

    id: int
    title: str
    description: str | None
    is_completed: bool
    created_at: datetime

    # Allows building this schema directly from a SQLAlchemy object
    model_config = ConfigDict(from_attributes=True)
