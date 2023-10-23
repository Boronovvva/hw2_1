# Дз 1
import sqlite3

connect = sqlite3.connect("books.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        year INTEGER
)""")

books_data = [('Химия', 'Г.Е Рудзитис', 2012),
              ('Биология', "А.Т. Ахматова", 2015),]
for book_data in books_data:
    cursor.execute('''INSERT INTO book(title, author, year) VALUES(?, ?, ?)''', book_data)

connect.commit()

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year 

    def display_info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}")



cursor.execute("SELECT * FROM book")
books = cursor.fetchall()
print(books)

for book_info in books:
    book = Book(book_info[0], book_info[1], book_info[2])
    book.display_info()



# Доп дз

def add_book():
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    year = input('Введите год издания: ')

    cursor.execute("INSERT INTO book(title, author, year) VALUES(?, ?, ?)", (title, author, year))
    connect.commit()

def update_book(title, author):
    cursor.execute(f"UPDATE book SET author = '{author}' title = ?", (title,))
    connect.commit()

def delete_book(title):
    cursor.execute("DELETE FROM book WHERE title = ?", (title,))
    connect.commit()