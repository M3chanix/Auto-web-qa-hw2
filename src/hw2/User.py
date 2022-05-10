from datetime import datetime
from pydantic import BaseModel
from hw2.Book import Book

# Создать юзера с помощью dataclass
# 

class User(BaseModel):
    _id: str
    index: int
    guid: str
    isActive: bool
    balance: float
    picture: str
    age: int
    eyeColor: str
    name: str
    gender: str
    company: str
    email: str
    phone: str
    address: str
    about: str
    registered: datetime
    latitude: float
    longitude: float
    tags: list[str]
    friends: list[dict]
    greeting: str
    favoriteFruit: str
    books: list[Book]
