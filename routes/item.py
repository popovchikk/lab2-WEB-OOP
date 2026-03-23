# routes/item.py - API для Item

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_session
from models import Item
from schemas import ItemCreate, ItemUpdate, ItemResponse


# создаю роутер
router = APIRouter(prefix="/items", tags=["Items"])


# GET - получить все элементы
@router.get("/", response_model=list[ItemResponse])
async def get_all_items(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Item))
    return result.scalars().all()


# GET - получить один элемент по ID
@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()
    
    if not item:
        raise HTTPException(status_code=404, detail="Элемент не найден")
    
    return item


# POST - создать новый элемент
@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate, session: AsyncSession = Depends(get_session)):
    new_item = Item(
        name=item.name,
        text=item.text,
        is_done=item.is_done,
        todo_list_id=item.todo_list_id
    )
    session.add(new_item)
    await session.commit()
    await session.refresh(new_item)
    return new_item


# PUT - обновить элемент
@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: int, item: ItemUpdate, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Item).where(Item.id == item_id))
    existing_item = result.scalar_one_or_none()
    
    if not existing_item:
        raise HTTPException(status_code=404, detail="Элемент не найден")
    
    if item.name:
        existing_item.name = item.name
    if item.text:
        existing_item.text = item.text
    if item.is_done is not None:
        existing_item.is_done = item.is_done
    
    await session.commit()
    await session.refresh(existing_item)
    return existing_item


# DELETE - удалить элемент
@router.delete("/{item_id}")
async def delete_item(item_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()
    
    if not item:
        raise HTTPException(status_code=404, detail="Элемент не найден")
    
    await session.delete(item)
    await session.commit()
    
    return {"message": "Элемент удален"}


# функция инициализации маршрутов
def init_routes(app):
    app.include_router(router)