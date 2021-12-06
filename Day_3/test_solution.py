from solution import binary_diagnostic_part_1, binary_diagnostic_part_2

def test_with_example_from_task_part_1():
    input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    assert 198 == binary_diagnostic_part_1(input)

def test_with_input__file_task_part_1():
    with open('input.txt', 'r') as f:
        input = [str(line.strip()) for line in f]
    assert 2035764 == binary_diagnostic_part_1(input)

def test_with_example_from_task_part_2():
    input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    assert 230 == binary_diagnostic_part_2(input)

def test_with_input_file_part_2():
    with open('input.txt', 'r') as f:
        input = [str(line.strip()) for line in f]
    assert 2817661 == binary_diagnostic_part_2(input)

