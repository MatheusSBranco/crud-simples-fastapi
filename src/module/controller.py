from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session

from .repository import get_session
from .service import read_book, read_all_books, create_a_book, update_a_book, delete_a_book
from .models import Book

controller = APIRouter()
        
@controller.get("/books/{book_id}", response_model=Book)
def get_single_book(book_id: int, db: Session = Depends(get_session)):
    db_book = read_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@controller.get("/books/", response_model=list[Book])
def get_all_books(db: Session = Depends(get_session)):
    return read_all_books(db)

@controller.post("/books/", response_model=Book)
def create_one_book(book: Book, db: Session = Depends(get_session)):
    return create_a_book(db, book)

@controller.put("/books/{book_id}", response_model=Book)
def update_one_book(book_id: int, updated_data: dict, db: Session = Depends(get_session)):
    return update_a_book(db, book_id, updated_data)

@controller.delete("/books/{book_id}")
def delete_one_book(book_id: int, db: Session = Depends(get_session)):
    delete_a_book(db, book_id)
    return {"message": "Book deleted successfully"}