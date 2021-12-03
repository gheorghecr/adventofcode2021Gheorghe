from solution import calculate_final_position, calculate_final_position_part2

def test_with_example_from_task_part_1():
    directions = ["forward", "down", "forward", "up", "down", "forward"]
    values = [5, 5, 8, 3, 8, 2]
    assert 150 == calculate_final_position(directions, values)

def test_with_random_input_task_part_1():
    directions = ["forward", "down", "down", "up"]
    values = [5, 5, 8, 3]
    assert 50 == calculate_final_position(directions, values)

def test_with_input__file_task_part_1():
    directions = []
    values = []
    with open('input.txt', 'r') as f:
        for line in f:
            directions.append(str(line.split()[0]))
            values.append(int(line.split()[1]))
    assert 1990000 == calculate_final_position(directions, values)


def test_with_example_from_task_part_2():
    directions = ["forward", "down", "forward", "up", "down", "forward"]
    values = [5, 5, 8, 3, 8, 2]
    assert 900 == calculate_final_position_part2(directions, values)

def test_with_random_input_task_part_2():
    directions = ["forward", "down", "down", "up", "forward"]
    values = [5, 5, 8, 3, 6]
    assert 660 == calculate_final_position_part2(directions, values)

def test_with_input__file_task_part_2():
    directions = []
    values = []
    with open('input.txt', 'r') as f:
        for line in f:
            directions.append(str(line.split()[0]))
            values.append(int(line.split()[1]))
    assert 1975421260 == calculate_final_position_part2(directions, values)