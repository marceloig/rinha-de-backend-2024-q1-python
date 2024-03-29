from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_DB = os.environ["POSTGRES_DB"]
DB_HOSTNAME = os.environ["DB_HOSTNAME"]

SQLALCHEMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOSTNAME}/{POSTGRES_DB}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()