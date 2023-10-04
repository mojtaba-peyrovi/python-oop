class Person:
    def __init__(self, name, age, gender):
        # double underscore for variables shows they are private attributes
        self.__name = name
        self.__age = age
        self.__gender = gender

    # the function below lets us access __name (private) as a property outside the class
    @property
    def Name(self):
        return self.__name
    
    # in the setter function we can set constraints to the variable. for example we can say age cannot be negative. and writing this way the variables are still kept private in the class and we can let the applicaiton use the instances we define for it
    @Name.setter
    def Name(self, value):
        self.__name = value



    @property
    def Age(self):
        return self.__age
    
    @Age.setter
    def Age(self, value):
        # we can define here that if a negative age is going to be assigned to age, we change it to zero
        if value < 0:
            self.__age = 0
        else: 
            self.__age = value    
        self.__age = value


    # in static methods we dont need to pass self variable. we can directly call a static method on the top of the class name without initializing an object
    @staticmethod
    def mymethod():
        print("hello world!")

Person.mymethod()




p1 = Person('Mike', 20, 'm')

# print(p1.Name)


# p1.Age = 10
p1.Age = -10


print(p1.Age)