import math


class SquareGenerator:
    def generate_squares(self, start, end):
        return [x ** 2 for x in range(start, end + 1)]

    def square_roots(self, squares_list):
        return [math.sqrt(x) for x in squares_list]


square_generator = SquareGenerator()
start_range = 1
end_range = 10
squares_list = square_generator.generate_squares(start_range, end_range)

square_roots_list = square_generator.square_roots(squares_list)

print(f"Squares List: {squares_list}")
print(f"Square Roots List: {square_roots_list}")
