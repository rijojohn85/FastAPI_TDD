import os
import sys

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from services.logging import logger

DEV_DATABASE_URL:str = os.getenv("DEV_DATABASE_URL")

engine: Engine = create_engine(DEV_DATABASE_URL)

SessionLocal: sessionmaker[Session]= sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()

def get_db_session():
    db:Session = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(e)
        db.close()
        sys.exit(1)
    finally:
        db.close()