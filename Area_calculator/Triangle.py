from Rectangle import Rectangle


class Triangle(Rectangle):

    def __init__(self, length: float|int, width: float|int):
        super().__init__(length,width)
        self.base = length/2
        self.high = width

    def getArea(self):
        return self.base * self.high

    def __str__(self):
        return f"base: {self.base}, high: {self.high}, area: {self.getArea()}"

