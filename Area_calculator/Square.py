from  Calculator import Shape

class Squere(Shape):

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def getArea(self):
        return self.width * self.length

    def __str__(self):
        return f"length: {self.length}, width: {self.width}"


