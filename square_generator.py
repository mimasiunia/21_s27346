import math


class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            print("End of the range must be greater or equal to the start.")
            return []

        return [x ** 2 for x in range(start, end + 1)]

    def square_roots(self, squares_list):
        return [math.sqrt(x) for x in squares_list]
