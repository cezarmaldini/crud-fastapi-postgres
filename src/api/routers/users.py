from fastapi import APIRouter, HTTPException

from src.services.users import UsersService
from src.api.deps import SessionDep
from src.schemas.users import UserResponse, UserCreate


router = APIRouter(prefix='/users', tags=['users'])

@router.post('/{user_email}', response_model=UserResponse)
def create_user(session: SessionDep, user_create: UserCreate):
    crud = UsersService(session)
    user = crud.get_user_by_email(email=user_create.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail='O usuário já existe.'
        )
        
    user = crud.create_user(user_create)
    return user