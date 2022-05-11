from hw2.User import User
from hw2.Distributor import Distributor
from pydantic import parse_file_as
import json

def main():
# Прочитать json в строку
    users = parse_file_as(list[User],'users.json')


# Создать distributor
    dist = Distributor(users, 'books.csv')
    dist.distribute()

# Записать в json
# name, gender, address, age, books: title, author, pages, genre

    include = {
            'name': True,
            'gender': True,
            'address': True,
            'age': True,
            'books': {'__all__': {'title', 'author', 'pages', 'genre'}}
            }

    result_list = []
    result_list = [user.dict(include = include) for user in users]

    with open('result.json', 'w') as file:
        file.write(json.dumps(result_list))

# Добавить indentation, определить порядок полей


if __name__ == '__main__':
    main()
