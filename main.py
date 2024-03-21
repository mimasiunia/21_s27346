from square_generator.square_generator import SquareGeneratorImpl, CubicGenerator

try:
    square_generator = SquareGeneratorImpl()
    start_range = 1
    end_range = 10
    squares_list = square_generator.generate_squares(start_range, end_range)
    square_roots_list = square_generator.square_roots(squares_list)
    print("Squares:", squares_list)
    print("Square Roots:", square_roots_list)
except ValueError as e:
    print(e)

try:
    cubic_generator = CubicGenerator()
    start_range = 1
    end_range = 10
    cubes_list = cubic_generator.generate_squares(start_range, end_range)
    print("Cubes:", cubes_list)
except ValueError as e:
    print(e)