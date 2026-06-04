from fastapi import APIRouter

from src.api.routers import users

api_router = APIRouter()
api_router.include_router(users.router)