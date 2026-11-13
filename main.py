from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

library = {}
app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    pages: int


class Message(BaseModel):
    message: str


@app.get("/books", response_model=Message)
async def get_books(author: str):
    if author not in library:
        raise HTTPException(status_code=404, detail = "Автора не знайдено")
    return library[author]


@app.post("/books", response_model=Book)
async def create_book(book: Book):
    author = book.author
    if author in library:
        library[author].append(book)
    else:
        library[author] = [book]
    return book


