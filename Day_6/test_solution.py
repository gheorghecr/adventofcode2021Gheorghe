from solution import part_1_and_2, read_input

def test_with_input_file_task_part_1_18_days():
    input = read_input("input_example.txt")
    assert 26 == part_1_and_2(input, 18)

def test_with_input_file_task_part_1_80_days():
    input = read_input("input_example.txt")
    assert 5934 == part_1_and_2(input, 80)

def test_with_example_task_part_1_80_days():
    input = read_input("input.txt")
    assert 352151 == part_1_and_2(input, 80)

def test_with_example_task_part_2_256_days():
    input = read_input("input.txt")
    assert 1601616884019 == part_1_and_2(input, 256)

