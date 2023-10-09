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

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Круг с радиусом: {self.radius}"

circle = Circle(8)
print(str(circle))        