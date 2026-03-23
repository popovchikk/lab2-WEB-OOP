# main.py - главный файл приложения

from fastapi import FastAPI
import uvicorn
from database import init_db
from routes.todo_list import init_routes as init_todo_routes
from routes.item import init_routes as init_item_routes


# создаю приложение
app = FastAPI(title="TodoList API")


# инициализация маршрутов
def bootstrap(app: FastAPI):
    init_todo_routes(app)
    init_item_routes(app)


# при запуске создаю таблицы
@app.on_event("startup")
async def on_startup():
    await init_db()
    print("База данных инициализирована!")


if __name__ == "__main__":
    bootstrap(app)
    uvicorn.run(app, host="0.0.0.0", port=8000)