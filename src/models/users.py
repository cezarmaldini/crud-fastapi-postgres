import uuid
from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import Column, String, Boolean, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID

from src.config.db import Base


def get_datetime_utc() -> datetime:
    return datetime.now(ZoneInfo('America/Sao_Paulo'))


class Users(Base):
    __tablename__ = 'users'
    
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    
    cep = Column(String(8), nullable=True)
    state = Column(String(2), nullable=True)
    city = Column(String(255), nullable=True)
    neighborhood = Column(String(255), nullable=True)
    street = Column(String(255), nullable=True)
    number = Column(Integer, nullable=True)
    
    updated_at = Column(
        DateTime,
        default=get_datetime_utc,
        nullable=False
    )