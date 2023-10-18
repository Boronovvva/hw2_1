#Дз 1 

# class Shape:
#     def draw(self):
#         print("Рисуем фигуру")

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def draw(self):
#         print(f"Рисуем круг с радиусом {self.radius}")

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def draw(self):
#         print(f"Рисуем прямоугольник шириной {self.width} и высотой {self.height}")


# shape = Shape()
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
# shape.draw()     
# circle.draw()    
# rectangle.draw()

# Дз 2 

# class Counter:
#     def __init__(self):
#         self.value = 0

#     def increment(self, value):
#         self.value += value

#     def get_value(self):
#         return self.value


# counter = Counter()  
# print(counter.get_value())  
# counter.increment(5)   
# print(counter.get_value())  
# counter.increment(3)  
# print(counter.get_value())