# routes/todo_list.py - API для TodoList

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_session
from models import TodoList
from schemas import TodoListCreate, TodoListUpdate, TodoListResponse


# создаю роутер
router = APIRouter(prefix="/todo", tags=["TodoList"])


# GET - получить все списки
@router.get("/", response_model=list[TodoListResponse])
async def get_all_lists(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(TodoList))
    return result.scalars().all()


# GET - получить один список по ID
@router.get("/{list_id}", response_model=TodoListResponse)
async def get_list(list_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(TodoList).where(TodoList.id == list_id))
    todo_list = result.scalar_one_or_none()
    
    if not todo_list:
        raise HTTPException(status_code=404, detail="Список не найден")
    
    return todo_list


# POST - создать новый список
@router.post("/", response_model=TodoListResponse)
async def create_list(todo: TodoListCreate, session: AsyncSession = Depends(get_session)):
    new_list = TodoList(name=todo.name)
    session.add(new_list)
    await session.commit()
    await session.refresh(new_list)
    return new_list


# PUT - обновить список
@router.put("/{list_id}", response_model=TodoListResponse)
async def update_list(list_id: int, todo: TodoListUpdate, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(TodoList).where(TodoList.id == list_id))
    todo_list = result.scalar_one_or_none()
    
    if not todo_list:
        raise HTTPException(status_code=404, detail="Список не найден")
    
    if todo.name:
        todo_list.name = todo.name
    
    await session.commit()
    await session.refresh(todo_list)
    return todo_list


# DELETE - удалить список
@router.delete("/{list_id}")
async def delete_list(list_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(TodoList).where(TodoList.id == list_id))
    todo_list = result.scalar_one_or_none()
    
    if not todo_list:
        raise HTTPException(status_code=404, detail="Список не найден")
    
    await session.delete(todo_list)
    await session.commit()
    
    return {"message": "Список удален"}


# функция инициализации маршрутов
def init_routes(app):
    app.include_router(router)