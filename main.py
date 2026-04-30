from database import create_tables, delete_tables
from fastapi import FastAPI
from contextlib import asynccontextmanager
from router import router as books_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Таблица очищена")
    await create_tables()
    print("Таблица готова")
    yield
    print("Выключено")

app = FastAPI(lifespan=lifespan)
app.include_router(books_router)


