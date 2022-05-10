from datetime import datetime
from typing import List
from pydantic import BaseModel

# Создать юзера с помощью dataclass
# 

class Book(BaseModel):
    title: str
    author: str
    genre: str
    pages: int
    publisher: str
