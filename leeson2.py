#class User:
#     def __init__(self, name, email, phone):
#         print(name)
        
#     def info(self):
#         print(self.name)
        
        
# user = User("Нурболот", "email@gmail.com", "8943893")
# user.info()

# class User:
#     def __init__(self, name, email, phone):
#         self.name   = name 
#         self.email   = email
#         self.phone = phone
        
#     def info(self):
#         print(self.name)

# user = User("Нурболот", "email@gmail.com", "8943893")
# user.info()


# class Dad:
#     def info_dad(self):
#         print("Я отец")

#         def info_dad(self):
#         print("Я отец")

#         def info_dad(self):
#         print("Я отец")

# class Son(Dad):
#     def info_son(self):
#         print("Я сын")


# son = Son()       
# son.info_son()
# son.info_dad()


# class Dog:
#     def speak_dog(self):
#         print("Гаф Гаф")
# # dog = Dog()
# # dog.speak_dog()
# class Cat(Dog):
#     def speak_cat(self):
#         print("Мияу Мияу")
# cat = Cat()
# cat.speak_cat()
# cat.speak_dog()

# class Mother:
#     def info_mom(self):
#         print("Я мама. Я родительский класс  Mother")

# class Father:
#     def info_dad(self):
#         print("Я папа. Я родительский класс  Father")

# class Son(Mother,Father):
#     def info_son(self):
#         print("Я сын. Я дочерный класс Son,Я наследуюсь от класса Mother u Father")
# son = Son()
# son.info_mom()
# son.info_dad()
# son.info_son()

# class Phone:
#     def call_phone(self):
#         print("Я звоню маме")

# class Camera:
#     def take_photo(self):
#         print("Я фоткаю отца")

# class Smartphone(Phone, Camera):
#     def all(self):
#         print("Я фоткаю и также звоню")

# smtph = Smartphone()
# smtph.call_phone()
# smtph.take_photo()
# smtph.all()