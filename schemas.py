from typing import Optional
from pydantic import BaseModel


class BookAdd(BaseModel):
    name: str
    author: str
    description: Optional[str] = None

class BookUpdate(BookAdd):
    id: int

class BookUpdateId(BaseModel):
    ok: bool = True
    book_id: int
