import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = BASE_DIR / ".env"

# Force load the .env file
load_dotenv(dotenv_path=ENV_PATH)

# Debug: Print the DATABASE_URL value
print("DEBUG: DATABASE_URL ->", os.getenv("DATABASE_URL"))

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Check your .env file.")

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)
SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session