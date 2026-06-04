from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from src.config.db import SessionLocal

def get_db():
    db = SessionLocal() # abre sessão
    try:
        yield db # injeta no endpoint
        
    finally:
        db.close() # sempre fecha, com ou sem erro
        
SessionDep = Annotated[Session, Depends(get_db)]