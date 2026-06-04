from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import Engine

from src.config.settings import settings

engine: Engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI),
    pool_pre_ping=True, # testa a conexão antes de usar
    pool_size=10, # mantém 10 conexões abertas e prontas
    max_overflow=20, # se as 10 estiverem ocupadas, abre até 20 extras temporárias
    pool_timeout=30, # se não houver conexão disponível em 30s, lança erro
    echo=False # imprime o SQL real no terminal
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()