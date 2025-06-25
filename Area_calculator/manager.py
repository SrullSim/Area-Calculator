from menu import (add_rectangle, add_circle, add_hexagon, add_square, add_triangle, main_menu, add_shape, get_index,
                  combine_shapes)
# from base import Shape
from rectangle import Rectangle
from square import Squere
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon



class ManagerProcess:

    @staticmethod
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

    @staticmethod
    def display_shapes(shapes: list):
        for shape in shapes:
            print(shape.__str__())

    @staticmethod
    def managing():
        """ managing the process """
        shapes = []
        # father = Shape()
        run = True
        while(run):

            first_choice = main_menu()
            if first_choice is not None:

            # option 1 - to add a shape
                if first_choice == "1":

                # get kind of shape
                    choice = add_shape()
                # make shape
                    shape = ManagerProcess.factory_of_shapes(choice)
                # add shape to list
                    shapes.append(shape)

                # option 2 - to display the list
                elif first_choice == "2":
                    if len(shapes) > 0 :
                        ManagerProcess.display_shapes(shapes)
                    else:
                        print("no shape added yet")

                # option 3 - display one shape
                elif first_choice == "3":
                    if len(shapes) > 0:
                        index = int(get_index())
                        if index <= len(shapes)-1:
                            print(shapes[index].__str__())
                        else:
                            print("wrong index given")
                    else:
                        print("no shape added yet")

                # option 4 - display area of shape
                elif first_choice == "4":
                    if len(shapes) > 0:
                        index = int(get_index())
                        print(shapes[index].get_area())
                    else:
                        print("no shape added yet")


                # option 5 - combine two shapes
                elif first_choice == "5":
                    if len(shapes) > 0:
                        first, sec = combine_shapes()
                        first, sec = int(first), int(sec)
                        if first <= len(shapes) >= sec:
                            first, sec = shapes[first], shapes[sec]
                            total_area = first + sec
                            print(total_area)
                        else:
                            raise IndexError
                    else:
                        print("no shape added yet")


                # exit from program
                elif first_choice == "6":
                    print("hope you find what you look for")
                    run = False