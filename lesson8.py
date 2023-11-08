#id, first_name, last_name, phone, devop, mounth, age

import sqlite3

connect = sqlite3.connect("user_students.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS user_student(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    phone TEXT,
    devop TEXT,         
    mounth INTEGER,
    age INTEGER)
    """)

class Data:
    def add_data(self):
        while True:
            first_name = input("Введите имя: ")
            last_name = input("Введите Фамилию: ")
            phone = input("Введите номер: ")
            devop = input("Введите направления: ")
            mounth = int(input("Введите месяц обучения: "))
            age = int(input("Введите возраст: "))
            cursor.execute(f'''INSERT INTO user_student(first_name,last_name,phone,devop,mounth,age) VALUES("{first_name}","{last_name}","{phone}","{devop}",{mounth},{age})''')
            connect.commit()
data = Data()
data.add_data()

