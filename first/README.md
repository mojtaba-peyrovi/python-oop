
link: [Tech With Tim](https://www.youtube.com/watch?v=xY__sjI5yVU)

in this code:
```
class dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
       
    def speak(self):
        print("Hi, I am", self.name, 'and I am', self.age, 'years old')
     

class cat(dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def talk(self):
        print('Meow!')
tim = dog('tim', 5, 'blue')
tim.speak()
```

cat class inherits from dog class. we need to use super() to initialize the variables from the main class inside the child class.
speak() function is inherited from dog to cat.


we can overwrite an inherited function for example: 
if in the parent class we have a function to print something, we can re-write it in the parent function to print something else.


##### class methods:  @classmethod:
we can use it to call directly on the name of the class. in this example: dog.num_dogs()

##### static methods:   @staticmethod:
they dont need the class to be called. we dont reference cls, or self in them.
Also we dont need to initialize the variables of static method. we just simply call them. like: dog.bark(5)

__@classmethod and @static method are called decorators.__

__private classes:__ classes that can be used within the same file or class.

__public classes:__ classes that are accessible by other classes and files. also other classes can modify the public classes 

in Python when we want to define a private class, we just add _ in the beginning of the class name and that will be provate. example:
class _getPoints():
