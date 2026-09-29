from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings

engine = create_engine(settings.database_url)

# A factory that creates a new session per request
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    """Base class for all ORM models."""


def get_db():
    """FastAPI dependency: open a session per request and always close it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
