from pydantic import BaseModel, ConfigDict, field_validator
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool | None = False
    due_date: datetime | None = None

    @field_validator("due_date")
    @classmethod
    def validate_due_date(cls, due_date: datetime | None) -> datetime | None:
        if due_date:
            now = datetime.now(due_date.tzinfo) if due_date.tzinfo else datetime.now()
            if due_date < now:
                raise ValueError("Due date cannot be in the past")
        return due_date

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    user_id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)
