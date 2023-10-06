# def test(value: int):
#     print(value)

# test('hello world')

# in the code above, we declated the variable value as an integer but we passed a string when we called the function
# Python code runs as usual, but if we want it to fail, we can use a library called mypy

# we can run "mypy <type_hint.py>" and it returns the error

def test2(value: int=0) -> str:
    print(f'my parameter is {value}')
test2 ()


