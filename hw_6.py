# ДЗ 1
# import sqlite3

# connect = sqlite3.connect("auto_service.db")
# cursor = connect.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS cars(
#     id INTEGER PRIMERI KEY,
#     number INTEGER,
#     brand TEXT,
#     model TEXT,
#     year INTEGER,
#     description TEXT,
#     status TEXT
#     )''')

# while True:
#     data_vub = input("1 - Добавить автомобиль, 2 - Обновить информация автомобиль, 3 - Просмотреть все автомобили, 4 - Просмотреть готовые автомобили, 0 - Выйти: ")
#     if data_vub == "1":
#         number = input("Введите номер автомобиля: ")
#         brand = input("Введите марка автомобиля: ")
#         model = input("Введите модель автомобиля: ")
#         year = input("Введите год выпуска: ")
#         description = input("Описание работ и статусе обслуживания автомобиля: ")
#         status = input("Статус обслуживания: ")
#         cursor.execute(f"""INSERT INTO cars(number, brand, model, year, description, status ) VALUES('{number}','{brand}','{model}',{year}, '{description}', '{status}')""")
#         connect.commit()
#         print(f"Ваши данные успешно добавлены!!!")
#     elif data_vub =="2":
#         number = int(input("Номер автомобиля: "))
#         brand = input("Новая марка (оставьте пустым, если не хотите изменять): ")
#         model = input("Новая модель (оставьте пустым, если не хотите изменять): ")
#         year = int(input("Новый год выпуска (оставьте пустым, если не хотите изменять): "))
#         description = input("Новое описание работ (оставьте пустым, если не хотите изменять): ")
#         status = input('Новый статус обслуживания (оставьте пустым, если не хотите изменять): ')
       
#         print("Информация об автомобиле успешно обновлена!")
#     elif data_vub == "3":
#         print('Список всех автомобилей:')
        
#     elif data_vub == '4':
#         print('Список готовых автомобилей:')
       
#     elif data_vub == '0':
#         print("Программа остановлена!!!")
#         break
#     else:
#         print("Такой команды нет!!!")