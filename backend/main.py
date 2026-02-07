from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class House(BaseModel):
    id: int
    title: str
    price: int
    city: str


HOUSES: List[House] = [
    House(id=1, title="4-Хонага", price=3500000, city="Душанбе"),
    House(id=2, title="3-Хонага", price=3000000, city="Душанбе"),
    House(id=3, title="2-Хонага", price=2500000, city="Хуҷанд"),
    House(id=4, title="1-Хонага", price=2000000, city="Хуҷанд"), 
]

@app.get("/houses", response_model=List[House])
def get_houses(city: Optional[str] = None):
    if city is None:
        return HOUSES

    return [
    house for house in HOUSES
    if house.city.lower() == city.lower()
]

@app.get("/houses/{house_id}", response_model=House)
def get_house(house_id: int):
    for house in HOUSES:
        if house.id == house_id:
            return house

    return ("eror, House not found")





# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import uvicorn

# app = FastAPI()

# books = [
#     {
#     "id": 1,
#     "title": "Асинхронность в Python",
#     "author": "Мэттью"
# },
# {
#     "id": 2,
#     "title": "Backend разработка в Python",
#     "author": "Артём",
# }
# ]

# @app.get(
#     path="/books",
#     tags=["Книги 📚"],
#     summary="Получить все книги"
# )
# def read_books():
#     return books


    
# @app.get(path="/books/{books_id}",
#         tags=["Книги 📚"],
#         summary="Получить конкретную книгу")
# def get_book(books_id: int):
#     for book in books:
#         if book["id"] == books_id:
#             return book

#     raise HTTPException(status_code=404, detail="Книга не найдена")

# class NewBook(BaseModel):
#     title: str
#     author: str

# @app.post(path="/book", tags=["Книги 📚"])
# def create_book(new_book: NewBook):
#     books.append({
#         "id": len(books) +1,
#         "title": new_book.title,
#         "author": new_book.author,
#     })
#     return {"success": True, "message": "Книга успешно добавлена"}




# from pydantic import BaseModel, Field, EmailStr

# data = {
#     "email": "abc@mail.ru",
#     "bio": Я пирожок,
#     "age": 12,
# }


# data_wo_Age = {
#     "email": "abc@mail.ru",
#     "bio": Я пирожок,
# }



# class UserSchema(BaseModel):
#     email: EmailStr
#     bio: str | Field(max_length=10)


#     class UserAgeSchema(UserSchema):
#     age: int = Field(ge=0, le=130)


# print(UserSchema(**data))


# # def func(data_: dict):
# #     data_["age"] += 1



# from fastapi import Depends, FastAPIб Depends
# from sqlite3 import connect
# from turtle import title
# 
# from pydantic import BaseModel
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
# from sqlalchemy.orm import declarativeBase
# 
# app = FastAPI()
# 
# engine = create_async_engine('sqlite+aiosqlite:///books.db')
# 
# with engine.connect() as conn:
# 
# new_session = async_sessionmaker(engine, expire_on_commit=False)
# 
# async def get_session():
    # async with new_session() as session:
        # yield session
# 
# 
# class Base(declarativeBase):
    # pass
# 
# class Boocmodel(Base):
    # __tablename__ = "books"
# 
    # id: Mapped[int] = mapped_column(primery_key=True)
    # title: Mapped[str]
    # author: Mapped[str]
# 
# @app.post("/setup_database")
# async def setup_database():
    # async with engine.bagin() as conn:
        # await conn.run_sync(base.metadata.drop_all)
        # await conn.run_sync(base.metadata.create_all)
    # return {"ok": True}
# 
    # class BookAddSchema(BaseModel):
        # title: str
        # author: str
# 
    # class Bookschema(BookAddSchema):
        # id: int
# 
# 
    # @app.post("/books")
    # async def add_book(data: BookAddSchema):
# 
# 
    # @app.get("/books")
    # async def get_book():
# 




import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)



Изменение в файле 07.02.2026 18:26. Всем привет!



НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ
НОВОЕ ПРИМЕНЕНИЕ



