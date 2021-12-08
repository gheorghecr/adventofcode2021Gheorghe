from solution import part_1, read_input

def test_with_input_file_task_part_1():
    input = read_input("input_example.txt")
    result = part_1(input)
    assert 5 == result

def test_with_example_task_part_1():
    input = read_input("input.txt")
    result = part_1(input)
    assert 7297 == result

