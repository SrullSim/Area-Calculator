
def main_menu() -> str:
    """choose function"""
    print("=========hello to the shape calculator=========")
    print("1. add shape")
    print("2. see all shapes")
    print("3. detail of shape")
    print("4. combine 2 shapes")
    print("5. exit")
    choice = input("your choice - ")
    if choice.isdigit() and "0" < choice > "5":
        return choice
    else:
        print("invalid choice")



def add_shape() -> str:
    """ choose shape to add """
    print("which shape you want to add")
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Circle")
    print("5. Hexagon")
    choice = input("enter nuber between 1-5")
    if choice.isdigit() and "0" < choice > "5":
        return choice
    else:
        print("invalid choice")



def add_rectangle() -> tuple[str,str]:
    """add rectangle"""
    high = input("enter the height - ")
    width = input("enter the width - ")
    if high.isdigit() and width.isdigit() and (width > "0" < high):
        return high, width
    else:
        print("invalid choice")


def add_square():
    """add square"""
    side = input("enter length of the side - ")
    if side.isdigit() and side > "0":
        return side
    else:
        print("invalid choice")


def add_triangle() -> tuple[str,str]:
    """add triangle"""
    height = input("enter the height - ")
    base = input("enter the length of the base - ")
    if height.isdigit() and base.isdigit() and (base > "0" < height):
        return height, base
    else:
        print("invalid choice")

def add_circle() -> str:
    """add circle"""
    radius = input("enter radius - ")
    if radius.isdigit() and radius > "0":
        return radius
    else:
        print("invalid choice")

def add_hexagon() -> str :
    """add hexagon"""
    side = input("enter length of side - ")
    if side.isdigit() and side > "0":
        return side
    else:
        print("invalid choice")

def detail_of_shape() -> str:
    """get index of shape to display"""
    index = input("enter the index of the shape you want")
    if index.isdigit():
        return index
    else:
        print("invalid choice")

def combine_shapes() -> tuple[str,str]:
    """ get two indexes of shapes to combine"""
    s1 = input("enter the index of the first shape you want to combine")
    if not s1.isdigit():
        raise ValueError
    s2 = input("enter the index of the second shape you want to combine")
    if s2.isdigit():
        return s1, s2