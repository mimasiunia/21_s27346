from square_generator import SquareGenerator

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
