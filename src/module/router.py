from fastapi import APIRouter

from controller import read_single_book

router = APIRouter()

@router.get("/books/{book_id}")
def get_book():
    read_single_book()