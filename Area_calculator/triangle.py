from rectangle import Rectangle


class Triangle(Rectangle):

    def __init__(self, height: float | int, base: float | int):
        super().__init__(height, base)

    def getArea(self):
        return 0.5 *  super().getArea()

    def get_perimeter(self):
        return 3 * self.width

    def __str__(self):
        return f"base: {self.width}, high: {self.height} "


