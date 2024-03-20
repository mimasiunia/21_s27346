import math


class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            print("End of the range must be greater or equal to the start.")
            return []

        return [x ** 2 for x in range(start, end + 1)]

    def square_roots(self, squares_list):
        return [math.sqrt(x) for x in squares_list]


square_generator = SquareGenerator()
start_range = 1
end_range = 10
squares_list = square_generator.generate_squares(start_range, end_range)

if squares_list:
    square_roots_list = square_generator.square_roots(squares_list)
    print("Squares:", squares_list)
    print("Square Roots:", square_roots_list)
else:
    print("No squares generated due to invalid range.")
