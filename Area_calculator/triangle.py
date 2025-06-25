from rectangle import Rectangle


class Triangle(Rectangle):

    def __init__(self, height: float | int, base: float | int):
        super().__init__(height, base)

    def get_area(self):
        return super().get_area() / 2

    def get_perimeter(self):
        return super().get_perimeter() / 2

    def __str__(self):
        return f"base: {self.width}, high: {self.height} "


