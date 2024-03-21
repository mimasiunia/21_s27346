from square_generator.square_generator import SquareGenerator
from square_generator.square_generator import CubicGenerator

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

cubic_generator = CubicGenerator()
start_range = 1
end_range = 5
cubes_list = cubic_generator.generate_squares(start_range, end_range)

if cubes_list:
    print("Cubes:", cubes_list)
else:
    print("No cubes generated due to invalid range.")