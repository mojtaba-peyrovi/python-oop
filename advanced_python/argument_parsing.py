import sys

# the first postion is argv or index 0 is alwayd the name of the python file name
print(sys.argv[0])

# the second postion is the argument we pass in the runtime (e.g. python argument_parsing.py test) -> the line below returns the word 'test'
print(sys.argv[1])


# we can also print argv and it retuens all variables we pass in the runtime inside a list
#  python argument_parsing.py test here is my dog -> returns:
#['argument_parsing.py', 'test', 'here', 'is', 'my', 'dog']
print(sys.argv)



