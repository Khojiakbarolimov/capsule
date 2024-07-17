class Shape:
    def __init__(self, symbol: str = "*", length: int = 5) -> None:
        self.symbol = symbol
        self.length = length
    
    def setsymbol(self, symbol: str)->None:
        self.symbol = symbol

    def setlength(self, length: int)->None:
        self.length = length
class Line(Shape):
    def show(self)->None:
        print(self.symbol*self.length, end="")

class Triangle(Shape):
    def show(self):
        for i in range(self.length+1):
            print(self.symbol*i)

class Rectangle(Shape):
    def show(self):
        for i in range(self.length+1):
            print(self.symbol*self.length)

class Shape:
    def __init__(self, symbol: str, length: int = 5) -> None:
        self.symbol = symbol
        self.length = length
    
    def setsymbol(self, symbol: str)->None:
        self.symbol = symbol

    def setlength(self, length: int)->None:
        self.length = length

class Line(Shape):
    def show(self)->None:
        print(self.symbol * self.length)

class Triangle(Shape):
    def show(self)->None:
        for i in range(1, self.length + 1):
            print(self.symbol * i)

class Rectangle(Shape):
    def show(self)->None:
        for i in range(self.length+1):
            print(self.symbol * (self.length+1))

class Nullshape(Shape):
    def show(self)->None:
        print("Bo'sh shakl")


line = Line(symbol='-', length=10)
print("Line:")
line.show()
line.setlength(15)
print("Line after setting length:")
line.show()

print("\n" + "="*20 + "\n")

triangle = Triangle(symbol='*', length=5)
print("Triangle:")
triangle.show()

print("\n" + "="*20 + "\n")

rectangle = Rectangle(symbol='#', length=4)
print("Rectangle:")
rectangle.show()
