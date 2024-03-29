import time


def time_timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f'{fname} took {after-before} seconds to execute')

        return value 
    
    return wrapper

@time_timed
def myfunc(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result


myfunc(90000)
