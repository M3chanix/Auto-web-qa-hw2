from hw2.User import User
from pydantic import BaseModel

class UserList(BaseModel):
    __root__: list[User]

