from solution import binary_diagnostic_part_1

def test_with_example_from_task_part_1():
    input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
    assert 198 == binary_diagnostic_part_1(input)

def test_with_input__file_task_part_1():
    with open('input.txt', 'r') as f:
        input = [str(line.strip()) for line in f]
    assert 2035764 == binary_diagnostic_part_1(input)

