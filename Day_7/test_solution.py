from solution import part_2, part_1, read_input

def test_with_example_part_1():
    input = read_input("input_example.txt")
    assert 37 == part_1(input)


def test_with_input_file_part_1():
    input = read_input("input.txt")
    assert 328318 == part_1(input)

def test_with_example_part_2():
    input = read_input("input_example.txt")
    assert 168 == part_2(input)


def test_with_input_file_part_2():
    input = read_input("input.txt")
    assert 89791146 == part_2(input)



