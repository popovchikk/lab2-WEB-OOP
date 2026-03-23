# models.py - модели для базы данных

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# модель TodoList (список дел)
class TodoList(Base):
    __tablename__ = "todo_lists"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    # связь с элементами
    items = relationship("Item", back_populates="todo_list", cascade="all, delete-orphan")


# модель Item (элемент списка)
class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    text = Column(String, nullable=True)
    is_done = Column(Boolean, default=False)
    
    # связь со списком
    todo_list_id = Column(Integer, ForeignKey("todo_lists.id"))
    todo_list = relationship("TodoList", back_populates="items")