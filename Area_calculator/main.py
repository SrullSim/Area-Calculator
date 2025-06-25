import menu
import manager
from Area_calculator.manager import factory_of_shapes, display_shapes
from Area_calculator.menu import main_menu, add_shape, detail_of_shape, combine_shapes
from base import Shape
from rectangle import Rectangle
from square import Squere
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon

print("1. add shape")
print("2. see all shapes")
print("3. detail of shape")
print("4. combine 2 shapes")
print("5. exit")

def managing():
    """ managing the process """
    shapes = []
    father = Shape()
    first_choice = main_menu()
    if first_choice is not None:

    # option 1 - to add a shape
        if first_choice == "1":

        # get kind of shape
            choice = add_shape()
        # make shape
            shape = factory_of_shapes(choice)
        # add shape to list
            shapes.append(shape)

        # option 2 - to display the list
        elif first_choice == "2":
            display_shapes(shapes)

        # option 3 - display one shape
        elif first_choice == "3":
            index = int(detail_of_shape())
            print(shapes[index].__str__())

        elif first_choice == "4":
            first, sec = combine_shapes()
            first, sec = int(first), int(sec)
            if first <= len(shapes) >= sec:
                first, sec = shapes[first], shapes[sec]
                both = father.__add__(first, sec)
























# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
