from hw2.User import User
from hw2.Book import Book
import csv


class Distributor():

    def __init__(self, users: list[User], books_file: str):
        self._users = users
        self._books_file = books_file

    def get_book_per_user(self) -> list[dict]:
        books_number = 0
        # Посчитать количество строк в books_file
        with open(self._books_file, 'r') as file:
            books_number = sum(1 for line in file) - 1 # первая строка - titles
        # разбить это количество по пользователям
        int_number = books_number // len(self._users)
        modulo = books_number % len(self._users)
        # возвращает [{user: user1, books_num: 3}, ]
        dist = list({'user': u, 'books_num': int_number} for u in self._users)
        for i in range(modulo):
            dist[i]['books_num'] += 1
        return dist

    def book_generator(self, num):
        book_list = []
        # хранить количество прочитанных строк из файла
        # Прочитать из csv переданное количество строк, распарсить и вернуть в виде list - csv возвращает словарь
        with open(self._books_file, 'r') as file:
            reader = csv.DictReader(file)
            for i in range(num):
            # Здесь я получаю словарь из строчки
                row = next(reader)
            # получить из словаря объект Book
                book = Book(**row)
            # сложить их в list и выкинуть
                book_list.append(book)
            yield book_list


    def distribute(self):
        # вызвать get_book_per_user
        dist = self.get_book_per_user()
        # идти по возвращённому списку, вызывать book_generator с books_number, добавлять возвращённые книги user
        for user in dist:
            user['user'].books = next(self.book_generator(user['books_num']))

        
