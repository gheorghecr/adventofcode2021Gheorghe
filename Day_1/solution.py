def calculate_measurement_increases(input):
    measurement_increases = 0
    for index, value in enumerate(input[:-1]):
        if value < input[index + 1]:
            measurement_increases += 1
    return measurement_increases

def calculate_measurement_increases_part_2(input):
    measurement_increases = 0
    for index, value in enumerate(input[:-1]):
        if sum(input[index: index + 3]) < sum(input[index + 1:  index + 4]):
            measurement_increases += 1
    return measurement_increases



if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = [int(line.strip()) for line in f]
    print(calculate_measurement_increases(input))
    print(calculate_measurement_increases_part_2(input))
    