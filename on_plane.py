def find_equation(input):
    slope = (input[1][1] - input[0][1]) / (input[1][0] - input[0][0])
    b = input[1][1] - slope*input[1][0]
    return slope, b


def find_point(slope, b, new_x):
    new_y = slope * new_x + b
    return new_y

def main(input, new_x):
    slope, b = find_equation(input)
    new_y = find_point(slope, b, new_x)
    return (new_x, new_y)
