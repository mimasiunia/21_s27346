import math
from abc import ABC, abstractmethod


class SquareGenerator(ABC):
    @abstractmethod
    def generate_squares(self, start, end):
        pass

    def square_roots(self, squares_list):
        return [math.sqrt(x) for x in squares_list]


class SquareGeneratorImpl(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than the start.")
        return [x ** 2 for x in range(start, end + 1)]


class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of the range must be greater than the start.")
        return [x ** 3 for x in range(start, end + 1)]
