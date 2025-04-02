from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.auth.dependencies import get_current_user
from app.models.task import Task as TaskModel
from app.schemas.task import TaskCreate, Task
from app.models.user import User
from app.utils.constants import constants

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post(
    "/",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
    summary="Create a task",
    description="Creates a task associated with the current user.",
    responses={
        status.HTTP_201_CREATED: {"description": constants.TASK_CREATED},
        status.HTTP_401_UNAUTHORIZED: {"description": constants.UNAUTHORIZED},
    },
)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_task = TaskModel(**task.model_dump(), user_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@router.get(
    "/",
    response_model=list[Task],
    summary="List user tasks",
    description="Returns a list of tasks belonging to the current user with optional pagination and search.",
    responses={
        status.HTTP_200_OK: {"description": constants.TASKS_RETRIEVED},
        status.HTTP_401_UNAUTHORIZED: {"description": constants.UNAUTHORIZED},
    },
)
def get_user_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    search: str = Query(None),
):
    query = db.query(TaskModel).filter(TaskModel.user_id == current_user.id)
    if search:
        query = query.filter(TaskModel.title.ilike(f"%{search}%"))
    tasks = query.offset(skip).limit(limit).all()
    return tasks


@router.put(
    "/{task_id}",
    response_model=Task,
    status_code=status.HTTP_200_OK,
    summary="Update a task",
    description="Updates the title and description of a specific task.",
    responses={
        status.HTTP_200_OK: {"description": constants.TASK_UPDATED},
        status.HTTP_401_UNAUTHORIZED: {"description": constants.UNAUTHORIZED},
        status.HTTP_404_NOT_FOUND: {"description": constants.TASK_NOT_FOUND},
    },
)
def update_task(
    task_id: int,
    task_update: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = db.query(TaskModel).filter(TaskModel.id == task_id, TaskModel.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=constants.TASK_NOT_FOUND)
    task.title = task_update.title
    task.description = task_update.description
    db.commit()
    db.refresh(task)
    return task


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a task",
    description="Deletes a task owned by the current user.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": constants.TASK_DELETED},
        status.HTTP_401_UNAUTHORIZED: {"description": constants.UNAUTHORIZED},
        status.HTTP_404_NOT_FOUND: {"description": constants.TASK_NOT_FOUND},
    },
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = db.query(TaskModel).filter(TaskModel.id == task_id, TaskModel.user_id == current_user.id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=constants.TASK_NOT_FOUND)
    db.delete(task)
    db.commit()
    return