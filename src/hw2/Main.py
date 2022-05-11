from hw2.Distributor import Distributor
from hw2.UserList import UserList

def main():
# Прочитать json в строку
    user_list = UserList.parse_file('users.json')

# Создать distributor
    dist = Distributor(user_list, 'books.csv')
    dist.distribute()

# Записать в json
# name, gender, address, age, books: title, author, pages, genre

    include = {'__root__': {'__all__' :
            {
            'name': True,
            'gender': True,
            'address': True,
            'age': True,
            'books': {'__all__': {'title', 'author', 'pages', 'genre'}}
            }}}


    with open('result.json', 'w') as file:
        file.write(user_list.json(include = include, indent=4))

if __name__ == '__main__':
    main()

