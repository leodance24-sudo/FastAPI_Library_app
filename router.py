from typing import Annotated
from repository import BookRepository
from schemas import BookAdd, BookUpdate, BookUpdateId
from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/library",
    tags=["Библиотека"],
)

@router.post("/books")
async def add_book(
        book: Annotated[BookAdd, Depends()],
) -> list[BookUpdateId]:
    book_id = await BookRepository.add_one(book)
    return {"message":"Книга добавлена", "book_id": book_id}

@router.get("")
async def get_books() -> list[BookUpdate]:
    books = await BookRepository.find_all()
    return  books