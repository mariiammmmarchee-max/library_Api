from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Author(Base):
    tablename = "author"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    books = relationship("Book", back_populates="author")

class Book(Base):
    tablename = "book"
    id = Column(Integer, primary_key=True, index=True)