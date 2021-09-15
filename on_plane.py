def find_equation(input):
    slope = (input[1][1] - input[0][1]) / (input[1][0] - input[0][0])
    b = input[1][1] - slope * input[1][0]
    return slope, b


def find_point(slope, b, new_x):
    new_y = slope * new_x + b
    return new_y


def main(input, new_x):
    slope, b = find_equation(input)
    new_y = find_point(slope, b, new_x)
    print((new_x, new_y))
    return (new_x, new_y)


if __name__ == "__main__":

    raw_input_1 = input("Type the first coordinates (Please omit '(' and ')') :")
    input_1 = tuple(int(x.strip()) for x in raw_input_1.split(','))
    raw_input_2 = input("Type the second coordinates:")
    input_2 = tuple(int(x.strip()) for x in raw_input_2.split(','))

    new_x = int(input("whats your new x coordinates:"))
    input = [input_1, input_2]

    main(input, new_x)

