from sqlmodel import Session, SQLModel, create_engine
from ..models.book import Book

engine = create_engine("postgresql://myuser:mypassword@localhost:5432/fastapi")

SQLModel.metadata.create_all(engine)

def get_session():
    try:
        with Session(engine) as session:
            yield session
    except Exception as err:
        print(err)
        session.rollback()   
    finally:
        session.close()

def get_book(session: Session, book_id: int):
    return session.get(Book, book_id)

def get_all_books(session: Session):
    return session.query(Book).all()

def create_book(session: Session, book: Book):
    db_book = Book(**book.dict())
    session.add(db_book)
    session.commit()
    session.refresh(db_book)
    return db_book

def update_book(session: Session, book_id: int, updated_data: dict):
    db_book = session.get(Book, book_id)
    
    for key, value in updated_data.items():
        setattr(db_book, key, value)
    
    session.commit()
    session.refresh(db_book)
    return db_book

def delete_book(session: Session, book_id: int):
    db_book = session.get(Book, book_id)
    session.delete(db_book)
    session.commit()