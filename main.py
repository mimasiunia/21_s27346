class SquareGenerator:
    def generate_squares(self, start, end):
        return [x ** 2 for x in range(start, end + 1)]


square_generator = SquareGenerator()
start_range = 1
end_range = 10
squares_list = square_generator.generate_squares(start_range, end_range)

print(squares_list)
