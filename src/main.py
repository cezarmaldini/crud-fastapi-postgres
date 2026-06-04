from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.routes import api_router
from src.config.settings import settings

def create_application():
    
    app = FastAPI(
        title=settings.API_TITLE,
        version=settings.API_VERSION,
        openapi_url=f'{settings.API_VERSION}/openapi.json'
    )
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
    
    app.include_router(api_router, prefix=settings.API_VERSION)
    
    return app


app = create_application()