from sqlalchemy.orm import Session
from sqlalchemy import select

from src.models.users import Users
from src.schemas.users import UserCreate


class UsersService:
    def  __init__(self, db: Session):
        self.db = db
        
        
    def create_user(self, user_create: UserCreate) -> Users:
        user = Users(**user_create.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)       
        return user
    
    
    def get_user_by_email(self, email: str) -> Users | None:
        statement = select(Users).where(Users.email == email)
        result = self.db.execute(statement)
        return result.scalar_one_or_none()