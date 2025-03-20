from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.task import Task
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from datetime import datetime, timezone


async def create_task_crud(db: AsyncSession, task: TaskCreate):
    new_task = Task(
        id=task.id,
        title=task.title,
        description=task.description,
        status=task.status,
        created_at=task.created_at or datetime.now(timezone.utc)
    )
    
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task


async def get_tasks(db: AsyncSession, skip: int = 0):
    result = await db.execute(select(Task).offset(skip))
    return result.scalars().all()


async def get_task_by_id(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).filter(Task.id == task_id))
    return result.scalar()


async def update_task_crud(db: AsyncSession, task_id: int, task_update: TaskUpdate):
    task = await get_task_by_id(db, task_id)
    if not task:
        return None
    
    update_data = task_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(task, key, value)

    await db.commit()
    await db.refresh(task)
    
    return task
