"""
we can decorate a function with another function. 
"""
def mydecorator(function):
    
    def wrapper():
        print('I am a decorator!')
        function()

    return wrapper

@mydecorator
def hello_world():
    print('hello world')


hello_world()

#----------------------------------------
# If we have to pass variables in the hello world function and make it dynamic in terms of number of variables:
def mydecorator_2(function):
    
    def wrapper(*args, **kwargs):
        print('I am a decorator!')
        function(*args, **kwargs)

    return wrapper


@mydecorator_2
def hello(person1, person2):
    print(f'Hello, {person1}, {person2}!')


hello('Moji', 'Anna')    

#----------------------------------------
# if instead of print we want to return:

def mydecorator_3(function):
    
    def wrapper(*args, **kwargs):
        print('I am a decorator!')
        return function(*args, **kwargs)

    return wrapper

@mydecorator_3
def hello(person1, person2):
    return f'Hello, {person1}, {person2}!'


hello('MOji','Anna')   
