from pydantic import BaseModel, Field

# Создать юзера с помощью dataclass
# 

class Book(BaseModel):
    title: str = Field(alias='Title')
    author: str = Field(alias='Author')
    genre: str = Field(alias='Genre')
    pages: int = Field(alias='Pages')
    publisher: str = Field(alias='Publisher')

