#Дз 1 

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def info(self):
#         print(f"Марка: {self.brand}, Модель: {self.model}")

# class Car(Vehicle):
#     def __init__(self,brand, model, year):
#         super().__init__(brand, model)
#         self.year = year

    
#     def info(self):
#         super().info()
#         print(f"Год выпуска: {self.year}")

# car = Car("KIA","Rio","2015")
# car.info()

# #Дз 2 

# class Parent():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name

#     def get_full_name(self):
#         print(f"Полное имя родителя: {self.first_name}, {self.last_name}")

# class Mother(Parent):
#     def __init__(self,first_name, last_name, child_count):
#         super().__init__(first_name, last_name)
#         self.child_count = child_count

#     def get_child_count(self):
#         print(f"Количество детей у родителя: {self.child_count}")

# class Father(Parent):
#     def __init__(self, first_name, last_name, child_count):
#         super().__init__(first_name, last_name)
#         self.child_count = child_count

#     def get_child_count(self):
#         print(f"Количество детей у родителя: {self.child_count}")

# parent = Mother("Bibisara", "Boronova", "1")
# parent.get_full_name()
# parent.get_child_count()

