from services.db_connect import Base

from sqlalchemy import (
Column,
Integer
)

class Category(Base):
    __tablename__: str = 'category'
    id: Column = Column(Integer, primary_key=True, autoincrement=True)