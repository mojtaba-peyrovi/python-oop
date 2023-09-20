class point():

    moji = 10

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)
    
    ## the following functions are built-in Python and we cannot rename them
    
    def move(self, x, y):
         self.x += x
         self.y += y
    
    @classmethod
    def print_coords(cls):
        print(cls.coords)


    def __add__(self, p):
         return point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return point(self.x - p.x, self.y - p.y)
    
    def __mul__(self, p):
        return self.x * p.x + self.y * p.y


    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)



    # greater than
    def __gt__(self, p):
        return self.length() > p.length()

    # greater than or equal    
    def __ge__(self, p):
        return self.length() >= p.length()

    # less than    
    def __lt__(self, p):
        return self.length() < p.length()

    # less than or equal    
    def __le__(self, p):
        return self.length() <= p.length()

    # equal
    def __eq__(self, p) -> bool:
        return self.length() == p.length()

    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"

        


p1 = point(3,4)
p2 = point(3,2)
p3 = point(1,3)
p4 = point(0,1)
p5 = p1 + p2
p6 = p4 - p1
p7 = p2*p3

print(p5, p6, p7)

print(p1 == p2, p3<=p3)


print(point.moji)

print(point.print_coords)