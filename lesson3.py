# Магический метод
# class Animals:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animals):
#     def sound(self):
#         return"Гаф-Гаф-Гаф!!!"

# dog = Dog(Animals)


# class Cat(Animals):
#     def sound(self):
#         return"Мяу Мяу"

# cat= Cat("Мурка") 
# cat.sound()
# print(f"{cat.name}:{cat.sound()}")

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def __str__(self):
#         return f"Круг с радиусом: {self.radius}"

# circle = Circle(8)
# print(str(circle))   


# Инкапсуляция 
#1 Публичный 
# class User:
#     name = "Nurbolot"

# user = User()
# print(user.name)

# 2 Защищеный 
# class Auto:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self._year = year

# auto = Auto("Toyota", 2020)
# print(auto.brand)
# print(auto._year)

# class Animals:
#     def __init__(self, name):
#         self.name = name

#     def _cat(self):
#         return f"Я кот, меня зовут: {self.name}"
# animals = Animals("Мурка")
# print(animals._cat())
        
# 3 Приватный 
# class MyClass:
#     def __init__(self):
#         self.__private_age = 20

# myclass = MyClass()
# print(myclass.__private_age)

# class Car:
#     def __init__(self, model, year):
#         self.__model = model
#         self.__year = year

#     def __info(self):
#         return f"Модель: {self.__model}, Год: {self.__year}"
    
#     def set_year(self, new_year):
#         self.__year = new_year

#     def get_info(self):
#         message = self.__info()
#         return message
    
# car = Car("BMW", 2023) 
# print(car.get_info()) 
# car.set_year(2022) 
# print(car.get_info())