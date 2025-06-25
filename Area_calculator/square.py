from  rectangle import Rectangle

class Squere(Rectangle):

    def __init__(self, side: float|int):
        super().__init__(side, side)

    def __str__(self):
        return f"Square size - each side = {self.width}"

