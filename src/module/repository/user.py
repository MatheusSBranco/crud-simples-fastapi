from sqlmodel import Session, SQLModel, create_engine
from ..models.user import User

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
        
def get_user(session: Session, user_name: int):
    return session.get(User, user_name)

def get_all_users(session: Session):
    return session.query(User).all()

def create_user(session: Session, user: User):
    db_user = User(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def update_user(session: Session, user_id: int, updated_data: dict):
    db_user = session.get(User, user_id)
    
    for key, value in updated_data.items():
        setattr(db_user, key, value)
    
    session.commit()
    session.refresh(db_user)
    return db_user

def delete_user(session: Session, user_id: int):
    db_user = session.get(User, user_id)
    session.delete(db_user)
    session.commit()
