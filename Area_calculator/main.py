import menu
import manager
from Area_calculator.manager import ManagerProcess
from Area_calculator.menu import main_menu, add_shape, get_index, combine_shapes
from base import Shape
from rectangle import Rectangle
from square import Squere
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ManagerProcess.managing()
