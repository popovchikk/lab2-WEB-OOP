# Лабораторная работа №2 - WEB-приложение (FastAPI + PostgreSQL)

## Что сделал:

 1) Настроил подключение к PostgreSQL через ENV переменные
 2) Реализовал CRUD для двух сущностей: TodoList и Item
 3) API выполнено в стандарте RESTful
 4) Каждая сущность имеет свой модуль с init_routes

## Стек технологий(которые я знаю - я их использовал):

- Python 3.14
- FastAPI
- SQLAlchemy (async)
- asyncpg
- PostgreSQL
- Uvicorn

## Как запустить:

1. Установить все стек технологии(выше, можно через терминал)
   
2. Создать файл .env с данными для подключения к БД:
   DB_HOST=localhost
   DB_PORT=5432
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_NAME=todolist_db

3. Запустить приложение:
   python main.py

4. Открыть Swagger UI:
   http://localhost:8000/docs

## API Endpoints:

### TodoList:
- GET /todo/ - получить все списки
- GET /todo/{id} - получить список по ID
- POST /todo/ - создать список
- PUT /todo/{id} - обновить список
- DELETE /todo/{id} - удалить список

### Items:
- GET /items/ - получить все элементы
- GET /items/{id} - получить элемент по ID
- POST /items/ - создать элемент
- PUT /items/{id} - обновить элемент
- DELETE /items/{id} - удалить элемент

## Структура проекта:

lab2/
├── main.py
├── config.py
├── database.py
├── models.py
├── schemas.py
└── routes/
    ├── __init__.py
    ├── todo_list.py
    └── item.py

## Студент: Попов Никита
## Группа: ИВТ-241