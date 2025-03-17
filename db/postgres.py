from settings import (
    POSTGRESQL_USER,
    POSTGRESQL_PASSWORD,
    POSTGRESQL_HOST,
    POSTGRESQL_DATABASE,
    POSTGRESQL_PORT,
    POSTRGESQL_POOL_SIZE,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from typing import AsyncGenerator

db_user = POSTGRESQL_USER
db_password = POSTGRESQL_PASSWORD
db_host = POSTGRESQL_HOST
db_port = POSTGRESQL_PORT
db_pool_size = POSTRGESQL_POOL_SIZE
db_database = POSTGRESQL_DATABASE

postgres_engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}",
    pool_size=db_pool_size,
    max_overflow=db_pool_size,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=True
)

psql_session = sessionmaker(postgres_engine, future=True)
psql_factory_session = scoped_session(psql_session)

def get_db_sync():
    SessionLocal = sessionmaker(
        autocommit=False, 
        autoflush=False, 
        bind=postgres_engine)
        # expire_on_commit=False)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# how to use async session on orm see:
# https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#synopsis-orm
# asyncpg currently not working on PyPy
## Create async session
async_engine = create_async_engine(
   f"postgresql+psycopg://{db_user}:{db_password}@{db_host}:{db_port}/{db_database}",
    # echo=True,
    pool_size=20,
    max_overflow=5,
)
Async_Session = sessionmaker(
    async_engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

async def get_db_async() -> AsyncGenerator[AsyncSession, None]:
    
    async with Async_Session() as session:
        yield session 

# base for model
Base = declarative_base()