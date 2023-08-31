def generate_squares_list():
    squares_list = [x ** 2 for x in range(1, 11)]
    return squares_list

squares = generate_squares_list()
print(squares)
