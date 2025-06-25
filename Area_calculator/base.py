from abc import abstractmethod, ABC


class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    def __str__(self):
        pass

    def __add__(self, other):
        if type(other) != Shape:
            raise ValueError
        return self.get_area() + other.get_area()

