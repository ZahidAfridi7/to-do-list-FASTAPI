from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.crud.task import create_task_crud, get_tasks,delete_task_crud,update_task_crud,complete_task_crud
from app.schemas.task import TaskUpdate, TaskCreate, TaskResponse
from app.db.models.task import Task
from app.db.session import get_db

router = APIRouter()  

@router.post("/create_task", response_model=TaskResponse)
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    new_task = await create_task_crud(db, task)
    return new_task

@router.get("/task/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar()
    
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/all_task", response_model=list[TaskResponse])
async def get_all_task(db: AsyncSession = Depends(get_db)): 
    return await get_tasks(db)  

@router.put("/task/{task_id}", response_model=TaskResponse)  
async def update_task(task_id: int, task_update: TaskUpdate, db: AsyncSession = Depends(get_db)):
    updated_data = await update_task_crud(db, task_id, task_update)
    
    if not updated_data:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return updated_data 

@router.put("/{task_id}/complete", response_model=TaskResponse)
async def complete_task(task_id:int,db:AsyncSession=Depends(get_db)):
    updated_task = await complete_task_crud(db,task_id)
    
    if not updated_task:
        raise HTTPException(status_code=404, detail="task not found")
    
    return updated_task


@router.delete("/{task_id}/delete_task",response_model=TaskResponse)
async def delete_task(task_id:int, db:AsyncSession=Depends(get_db)):
    dl_task = await delete_task_crud(db,task_id)
    
    if not dl_task:
        raise HTTPException(status_code=404,detail="no task found")
    
    return dl_task