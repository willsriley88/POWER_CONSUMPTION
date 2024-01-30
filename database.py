from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings


SQLALCHEMY_DATABASE_URL = f'{settings.database_name}://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_schema_name}'
ENGINE = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(autoflush=False, bind=ENGINE)

Base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()