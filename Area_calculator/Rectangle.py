from Calculator import Shape




class Rectangle(Shape):

    def __init__(self, length: float|int, width: float|int ):
        self._length = length
        self.width = width

    def getArea(self):
        return self.width * self._length

    def __str__(self):
        return f"length: {self._length}, width: {self.width}"

    @property
    def length(self):
        return self.length

    @length.setter
    def set_lengh(self, length):
        self._length = length
