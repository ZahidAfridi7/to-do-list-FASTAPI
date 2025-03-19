from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models.task import Task


async def create_task(db:AsyncSession, task:Task):
    new_task = task(
        id = task.id,
        title = task.title,
        description = task.description,
        status = task.status,
        created_at = task.created_at
    )
    
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

async def get_task(db:AsyncSession,task_id:int):
    result = await db.execute(select(task_id).filter(Task.id==task_id))
    return result.scalars().first()


 