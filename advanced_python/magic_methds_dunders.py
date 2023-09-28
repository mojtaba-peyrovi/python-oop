
# dunders are the methods with double __a__
class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x , self.y + other.y)

    """
     This function tells the class how we want the object to be reprseneted. for example if we didnt have
     this method here, and we wanted to print v3, it would have only show the object type not the actual values
    """
    def __repr__(self):
        return f'x: {self.x}, y:{self.y}'


v1 = Vector(20,30)             
v2 = Vector(20,30)
v3 = v1 + v2

print(v3)