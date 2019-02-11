# link: https://www.youtube.com/watch?v=39m3rstTN8w

#tutorial 2
# class dog(object):
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#     def speak(self):
#         print("Hi, I am", self.name, 'and I am', self.age, 'years old')
#     def talk(self):
#         print('Bark!')
#
# class cat(dog):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color
#     def talk(self):
#         print('Meow!')
# tim = dog('tim', 5, 'blue')
# #tim.speak()
# tim.talk()


#tutorial 3
# class vehicle():
#     def __init__(self, price, gas, color):
#         self.price = price
#         self.gas = gas
#         self.color = color
#
#     def fillUpTank(self):
#         self.gas = 100
#     def emptyTank(self):
#         self.gas = 0
#     def gasLeft(self):
#         return self.gas
#
# class car(vehicle):
#     def __init__(self, price, gas, color, speed):
#         super().__init__(price, gas, color)
#         self.speed = speed
#
#     def beep(self):
#         print('beep beep')
#
#
# class truck(vehicle):
#     def __init__(self, price, gas, color, tires):
#         super().__init__(price, gas, color)
#         self.tires = tires
#     def beep(self):
#         print('Honk Honk')



# tutorial 4
# class point():
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         self.coords = (self.x, self.y)
#     def move(self, x, y):
#          self.x += x
#          self.y += y
#     def __add__(self, p):
#          return point(self.x + p.x, self.y + p.y)
#
#     def __sub__(self, p):
#         return point(self.x - p.x, self.y - p.y)
#     def __mul__(self, p):
#         return self.x * p.x + self.y * p.y
#     def length(self):
#         import math
#         return math.sqrt(self.x**2 + self.y**2)
#
#
#     #greater than
#     def __gt__(self, p):
#         return self.length() > p.length()
#     # greater than or equal to
#     def __ge__(self, p):
#         return self.length() >= p.length()
#     # less than
#     def __lt__(self, p):
#         return self.length() < p.length()
#     #less than or equal to
#     def __le__(self, p):
#         return self.length() <= p.length()
#     #equal to
#     def __eq__(self, p):
#         return self.x == p.x and self.y == p.y
#     def __str__(self):
#         return "(" + str(self.x) + ',' + str(self.y) + ')'
#
# p1 = point(3,4)
# p2 = point(3,2)
# p3 = point(1,3)
# p4 = point(0,1)
# p5 = p1 + p2
# p6 = p4 - p1
# p7 = p2*p3
#
# print(p1 == p2)
# print(p1 > p2)
# print(p4 >= p3)

# tutorial 5
# class dog:
#     dogs = []
#
#     def __init__(self, name):
#         self.name = name
#         self.dogs.append(self)
#
#     @classmethod
#     def num_dogs(cls):
#         return len(cls.dog)
#
#     staticmethod
#     def bark(n):
#         """bark n times"""
#         for _ in range(n):
#             print('Bark!')
#
#
# # tim = dog("Tim")
# # jim = dog("Jim")
# # print(dog.dogs)
#
# # print(dog.num_dogs())
#
#
# dog.bark(4)


#tutorial 6
from first.mod import notPrivate
test = notPrivate('tim')
test.display()
