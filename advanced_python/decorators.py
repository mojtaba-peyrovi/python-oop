def mydecorator(function):
    
    def wrapper():
        print('I am a decorator!')
        function()

    return wrapper

@mydecorator
def hello_world():
    print('hello world')


hello_world()