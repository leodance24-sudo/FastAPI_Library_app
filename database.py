from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# Создание движка
engine = create_async_engine("sqlite+aiosqlite:///books.db")

# Создание фабрики сессий
new_session = async_sessionmaker(engine, expire_on_commit=False)


# Базовый класс для моделей
class Model(DeclarativeBase):
    pass

# Модель таблицы
class BookTable(Model):
    __tablename__ = "books"

    # ОБЯЗАТЕЛЬНО: первичный ключ
    id: Mapped[int] = mapped_column(primary_key=True)
    # Теперь с указанием типа колонки в БД
    name: Mapped[str]
    author: Mapped[str]
    description: Mapped[Optional[str]]


# Функции для создания/удаления таблиц
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)