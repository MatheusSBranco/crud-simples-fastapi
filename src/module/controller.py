from fastapi import HTTPException, Depends
from sqlmodel import Session

from repository import get_session
from service import read_book, read_all_books, create_a_book, update_a_book, delete_a_book
from models import Book

def read_single_book(book_id: int, db: Session = Depends(get_session)):
    db_book = read_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

def read_books(db: Session = Depends(get_session)):
    return read_all_books(db)

def create_one_book(book: Book, db: Session = Depends(get_session)):
    return create_a_book(db, book)

def update_one_book(book_id: int, updated_data: dict, db: Session = Depends(get_session)):
    return update_a_book(db, book_id, updated_data)

def delete_one_book(book_id: int, db: Session = Depends(get_session)):
    delete_a_book(db, book_id)
    return {"message": "Book deleted successfully"}