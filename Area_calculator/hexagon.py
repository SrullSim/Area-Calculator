from  base import Shape
import math


class Hexagon(Shape):

    def __init__(self, side: float|int):
        self.side = side


    def get_area(self):
        return (3 * math.sqrt(3) * self.side ** 2) / 2

    def get_perimeter(self):
        return self.side * 6

    def __str__(self):
        return f"each side in the hexagon is {self.side} "
