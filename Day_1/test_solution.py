from solution import calculate_measurement_increases, calculate_measurement_increases_part_2

def test_part_1_with_3_increases():
    input = [10, 20, 10, 40, 10, 200]
    assert 3 == calculate_measurement_increases(input)

def test_part_1_with_zero_increases():
    input = [10, 6]
    assert 0 == calculate_measurement_increases(input)

def test_part_1_with_one_increase():
    input = [10, 9, 8, 7, 6, 5, 11]
    assert 1 == calculate_measurement_increases(input)

def test_part_2_with_2_increases():
    input = [2, 9, 8, 15, 5, 6, 20]
    assert 2 == calculate_measurement_increases_part_2(input)

def test_part_2_with_0_increases():
    input = [30, 9, 8, 15, 5, 6, 5]
    assert 0 == calculate_measurement_increases_part_2(input)