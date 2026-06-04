from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr = Field(max_length=255, examples=['user@example.com.br'])
    name: str = Field(max_length=255, examples=['João'])
    is_active: bool = Field(default=True)
    
    cep: Optional[str] = Field(default=None, max_length=8, examples=['77059020'])
    state: Optional[str] = Field(default=None, max_length=2, examples=['TO'])
    city: Optional[str] = Field(default=None, max_length=255, examples=['Palmas'])
    neighborhood: Optional[str] = Field(default=None, max_length=255, examples=['Bertaville'])
    street: Optional[str] = Field(default=None, max_length=255, examples=['Rua Paulo Sabino'])
    number: Optional[int] = Field(default=None, examples=[14, 123])
    

class UserCreate(UserBase):
    email: EmailStr = Field(max_length=255)
    name: str = Field(max_length=255)
    
    
class UserUpdate(BaseModel):
    name: Optional[str] = Field(default=None, max_length=255)
    is_active: Optional[bool] = Field(default=None)

    cep: Optional[str] = Field(default=None, max_length=8)
    state: Optional[str] = Field(default=None, max_length=2)
    city: Optional[str] = Field(default=None, max_length=255)
    neighborhood: Optional[str] = Field(default=None, max_length=255)
    street: Optional[str] = Field(default=None, max_length=255)
    number: Optional[int] = Field(default=None)
    
    
class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: UUID
    updated_at: datetime