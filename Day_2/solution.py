def calculate_final_position(directions, values):
    x_position = 0
    y_position = 0 
    for index, value in enumerate(directions):
        if value == "forward":
            x_position += values[index]
        elif value == "up":
            y_position -= values[index]
        elif value == "down":
            y_position += values[index]
    return x_position * y_position

def calculate_final_position_part2(directions, values):
    x_position = 0
    y_position = 0 
    aim = 0
    for index, value in enumerate(directions):
        if value == "forward":
            x_position += values[index]
            y_position += aim * values[index]
        elif value == "up":
            aim -= values[index]
        elif value == "down":
            aim += values[index]
    return x_position * y_position
    

if __name__ == '__main__':
    directions = []
    values = []
    with open('input.txt', 'r') as f:
        for line in f:
            directions.append(str(line.split()[0]))
            values.append(int(line.split()[1]))
    print(calculate_final_position(directions, values))
    print(calculate_final_position_part2(directions, values))
        
    
    