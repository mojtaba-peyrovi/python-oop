# sequence of numbers between 0 and 9000000


def mygenerator(n):
    for x in range(n):
        yield x ** 3


values = mygenerator(9000000)


# print(next(values))
# print(next(values))
# print(next(values))

# using yeild, we wont have the results of numbers between 0 and 9000000 cube, as a list with length of 9M, 
# yield always returns the next number and we can return then anytime needed.

values = mygenerator(100)
for x in values:
    print(x)


# using generators, we can have the raneg as big as we want and it doesnt change the size of the generator
# because it acts as a placeholder and doesnt actually return results until they are yielded.



def infinite_sequence():
    results = 1
    while True:
        yield results
        results *= 5


values = infinite_sequence()

print(next(values))
print(next(values))
print(next(values))
     
# with generators, we can even have infinite loops, as the above function. using print(x), we fall into an infinite loop




