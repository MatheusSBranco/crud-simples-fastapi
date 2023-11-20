from sqlmodel import Session
from .repository import get_book, get_all_books, create_book, update_book, delete_book
from .models import Book

def read_book(db: Session, book_id: int):
    return get_book(db, book_id)

def read_all_books(db: Session):
    return get_all_books(db)

def create_a_book(db: Session, book: Book):
    return create_book(db, book)

def update_a_book(db: Session, book_id: int, updated_data: dict):
    return update_book(db, book_id, updated_data)

def delete_a_book(db: Session, book_id: int):
    return delete_book(db, book_id)