from hw2.User import User
from hw2.Book import Book
from hw2.Distributor import Distributor
from pydantic import parse_file_as

def main():
# Прочитать json в строку
    users = parse_file_as(list[User],'users.json')


# Создать distributor
    dist = Distributor(users, 'books.csv')
    dist.distribute()


# Записать в json


# Выгрузить результат в json
if __name__ == '__main__':
    main()
