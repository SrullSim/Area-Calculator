from menu import (add_rectangle,add_circle,add_hexagon,add_square,add_triangle)
# from base import Shape
from rectangle import Rectangle
from square import Squere
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon




def factory_of_shapes(shape: str):
    if shape is not None:
        try:
            if shape == "1":
                high , width = add_rectangle()
                high , width = float(high),float(width)
                rec = Rectangle(high, width)
                return rec
            elif shape == "2":
                side = float(add_square())
                squ = Squere(side)
                return squ
            elif shape == "3":
                high, base = add_triangle()
                high, base = float(high),float(base)
                tri = Triangle(high, base)
                return tri
            elif shape == "4":
                radius = float(add_circle())
                cir = Circle(radius)
                return cir
            elif shape == "5":
                side = float(add_hexagon())
                hexa = Hexagon(side)
                return hexa
            else:
                print("invalid choice")
                raise ValueError
        except Exception as ex:
            print("failed to create shape because : ", ex)


def display_shapes(shapes: list):
    for shape in shapes:
        print(shape.__str__())
