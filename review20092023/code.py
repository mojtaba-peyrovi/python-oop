
# class Dog(object):

#     def __init__(self, name, age):
#         print('a new dog is created')
#         self.name = name
#         self.age = age
#     def speak(self):
#         print(f"HI, I'm {self.name}, I'm {self.age} years old")

#     def change_age(self, age):
#         self.age = age


#     def add_weight(self, weight):
#         self.weight = weight


# tim = Dog("Tim", 23)
# fred = Dog("fred", 12)


# tim.speak()
# tim.change_age(1)
# tim.speak()


# class Dog(object):

#     def __init__(self, name, age):
#         print('a new dog is created')
#         self.name = name
#         self.age = age
#     def speak(self):
#         print(f"HI, I'm {self.name}, I'm {self.age} years old")

    

# class Cat(Dog):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         self.color = color



# cat1 = Cat('kitty', 5, 'pink')

# cat1.speak()
    



class Vehicle(object):
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color


    def fillUpTank(self):
        self.gas = 100


    def defineEmptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas



class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(self, price, gas, color)
        self.speed = speed

    def beep(self):
        print('beep beep')



class Truck(Vehicle):
    def __init__(self, price, gas, color, speed, tires):
        super().__init__(self, price, gas, color) 
        self.tires = tires

    def beep(self):
        print('honk honk')



