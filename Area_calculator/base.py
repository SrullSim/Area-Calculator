from abc import abstractmethod, ABC


class Shape(ABC):

    @abstractmethod
    def getArea(self):
        pass
    def get_perimeter(self):
        pass