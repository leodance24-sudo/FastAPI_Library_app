from schemas import BookAdd, BookUpdate
from database import new_session, BookTable
from sqlalchemy import select


class BookRepository:
    @classmethod
    async def  add_one(cls, data: BookAdd) -> int:
        async with new_session() as session:
            book_dict = data.model_dump()

            book = BookTable(**book_dict)
            session.add(book)
            await session.flush()
            await session.commit()
            return book.id

    @classmethod
    async def find_all(cls) -> list[BookUpdate]:
        async with new_session() as session:
            query = select(BookTable)
            result = await session.execute(query)
            book_models = result.scalars().all()
            book_schemas = [BookUpdate.model_validate(db_book) for db_book in book_models]
            return book_schemas