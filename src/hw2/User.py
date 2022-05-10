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
    # присутствует символ $
    balance: str
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
    # неправильный datetime?
    registered: str
    latitude: float
    longitude: float
    tags: list[str]
    friends: list[dict]
    greeting: str
    favoriteFruit: str
    # поставить необязательность
    books: list[Book] = []

