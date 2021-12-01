def calculate_measurement_increases(input):
    measurement_increases = 0
    for index, value in enumerate(input[:-1]):
        if value < input[index + 1]:
            measurement_increases += 1
    return measurement_increases



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = [int(line.strip()) for line in f]
    print(calculate_measurement_increases(input))
    