def generate_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


start_range = 1
end_range = 10
squares_list = generate_squares(start_range, end_range)
print(squares_list)
