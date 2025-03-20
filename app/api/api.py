from fastapi import APIRouter

api_router = APIRouter()

from app.api import (
    task
)

api_router.include_router(task.router, prefix="/api/v1/task", tags=["Tasks"])

