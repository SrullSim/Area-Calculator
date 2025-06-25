from base import Shape




class Rectangle(Shape):

    def __init__(self, height: float | int, width: float | int):
        self.height = height
        self.width = width

    def getArea(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) *2

    def __str__(self):
        return f"length: {self.height}, width: {self.width}, area: {self.getArea()}"







