# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import List, Optional

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class House(BaseModel):
#     id: int
#     title: str
#     price: int
#     city: str


# HOUSES: List[House] = [
#     House(id=1, title="4-Хонага", price=3500000, city="Душанбе"),
#     House(id=2, title="3-Хонага", price=3000000, city="Душанбе"),
#     House(id=3, title="2-Хонага", price=2500000, city="Хуҷанд"),
#     House(id=4, title="1-Хонага", price=2000000, city="Хуҷанд"), 
# ]

# @app.get("/houses", response_model=List[House])
# def get_houses(city: Optional[str] = None):
#     if city is None:
#         return HOUSES

#     return [
#     house for house in HOUSES
#     if house.city.lower() == city.lower()
# ]

# @app.get("/houses/{house_id}", response_model=House)
# def get_house(house_id: int):
#     for house in HOUSES:
#         if house.id == house_id:
#             return house

#     return ("eror, House not found")





from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

books = [
    {
    "id": 1,
    "title": "Асинхронность в Python",
    "author": "Мэттью"
},
{
    "id": 2,
    "title": "Backend разработка в Python",
    "author": "Артём",
}
]

@app.get(
    path="/books",
    tags=["Книги 📚"],
    summary="Получить все книги"
)
def read_books():
    return books


    
@app.get(path="/books/{books_id}",
        tags=["Книги 📚"],
        summary="Получить конкретную книгу")
def get_book(books_id: int):
    for book in books:
        if book["id"] == books_id:
            return book

    raise HTTPException(status_code=404, detail="Книга не найдена")