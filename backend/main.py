
from unittest import result
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

app = FastAPI()

# Разрешаем фронтенду подключаться к бэкенду
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. ЧЕРТЕЖ (Схема того, как выглядит дом)
class HouseSchema(BaseModel):
    id: int
    title: str
    price: int
    city: str

# Подключение к базе данных
def get_db_connection():
    conn = sqlite3.connect("houses.db")
    conn.row_factory = sqlite3.Row
    return conn

# 3. СОЗДАНИЕ ТАБЛИЦЫ (Запускается один раз при старте сервера)
with get_db_connection() as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS houses (
        id INTEGER PRIMARY KEY,
        title TEXT,
        price INTEGER,
        city TEXT
    )
    """)

# 2. СКЛАД (Наш временный список домов)
DATABASE_LIST: List[HouseSchema] = [
    HouseSchema(id=1, title="4-Хонага", price=3500000, city="Душанбе"),
    HouseSchema(id=2, title="3-Хонага", price=3000000, city="Душанбе"),
    HouseSchema(id=3, title="2-Хонага", price=2500000, city="Хуҷанд"),
    HouseSchema(id=4, title="1-Хонага", price=2000000, city="Хуҷанд"), 
]

# --- МАРШРУТЫ ---

# 1. ПОИСК (Оставили как есть)
@app.get("/search") 
def search_houses(city: Optional[str] = None):
    conn = get_db_connection()
    if city:
        # Ищем в базе по названию города
        cursor = conn.execute("SELECT * FROM houses WHERE city LIKE ?", (f"%{city}%",))
    else:
        # Забираем всё
        cursor = conn.execute("SELECT * FROM houses")

    rows = cursor.fetchall()
    conn.close()

    # Превращаем результат из формата базы в обычный список\
    results = [dict(row) for row in rows]
    return {"Box_houses": results}


# 2. ДОБАВЛЕНИЕ (Поменяли адрес двери на /add-dom)
@app.post("/add-dom") 
def create_house(New_house: HouseSchema):
    # Логика: берем данные и "приклеиваем" (append) к списку
    DATABASE_LIST.append(New_house)
    return {"message": "Дом добавлен!", "Box_houses": New_house}

# 3. УДАЛЕНИЕ (Поменяли адрес двери на /remove-dom)
@app.delete("/remove-dom/{house_id}") 
def delete_house(house_id: int):
    global DATABASE_LIST
    # Логика: перезаписываем список, исключая ДОМ с этим ID
    DATABASE_LIST = [ДОМ for ДОМ in DATABASE_LIST if ДОМ.id != house_id]
    return {"message": "Дом удален из базы"}


