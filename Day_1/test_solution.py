from solution import calculate_measurement_increases

def test_1():
    input = [10, 20, 10, 40, 10, 200]
    assert 3 == calculate_measurement_increases(input)

def test_2():
    input = [10, 6]
    assert 0 == calculate_measurement_increases(input)

def test_3():
    input = [10, 9, 8, 7, 6, 5, 11]
    assert 1 == calculate_measurement_increases(input)