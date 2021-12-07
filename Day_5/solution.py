from io import TextIOWrapper
import numpy

def read_input(filename):
    with open(filename, 'r') as f:
        input = [line.strip().split(" -> ") for line in f]
    
    # format values
    for index, line in enumerate(input):
        input[index] = [line[0].split(","), line[1].split(",")]

    return input

def get_direct_lines_only(input):
    filtered_input = []
    for value in input:
        if value[0][0] == value[1][0] or value[0][1] == value[1][1]:
            filtered_input.append(value)
    
    # get max value
    max_value = int(max(max(list(map(max, filtered_input)))))

    return filtered_input, max_value + 1

def create_2d_array(max_value):
    # return [[0]*max_value]*max_value 
    return numpy.zeros((max_value, max_value))

def mark_lines(direct_lines, two_d_array):
    for line in direct_lines:
        # check if line is horizontal or vertical
        if int(line[0][0]) == int(line[1][0]):
            # vertical
            if int(line[0][1]) > int(line[1][1]):
                list_of_index_to_update = []
                for value in range (int(line[1][1]), int(line[0][1]) + 1):
                    list_of_index_to_update.append(value)
                print(list_of_index_to_update, " list ", int(line[0][0]) )
                for to_update in list_of_index_to_update:
                    two_d_array[to_update][int(line[0][0])] += 1
            else:
                list_of_index_to_update = []
                for value in range (int(line[0][1]), int(line[1][1]) + 1):
                    list_of_index_to_update.append(value)
                print(list_of_index_to_update, " list ", int(line[0][0]) )
                for to_update in list_of_index_to_update:
                    two_d_array[to_update][int(line[0][0])] += 1
        else:
            # horizontal 
            if int(line[0][0]) > int(line[1][0]):
                list_of_index_to_update = []
                for value in range (int(line[1][0]), int(line[0][0]) + 1):
                    list_of_index_to_update.append(value)
                for to_update in list_of_index_to_update:
                    two_d_array[int(line[0][1])][to_update] += 1
            else:
                list_of_index_to_update = []
                for value in range (int(line[0][0]), int(line[1][0]) + 1):
                    list_of_index_to_update.append(value)
                for to_update in list_of_index_to_update:
                    two_d_array[int(line[0][1])][to_update] += 1


    print(two_d_array)
    return count_number_of_values_higher_than_2(two_d_array)

def count_number_of_values_higher_than_2(two_d_array):
    total = 0
    for line in two_d_array:
        for value in line:
            if value > 1:
                total += 1
    print(total, "total")
    return total

def part_1(input):
    direct_lines, max_value = get_direct_lines_only(input)
    two_d_array = create_2d_array(max_value)
    print(two_d_array)
    return mark_lines(direct_lines, two_d_array)


if __name__ == '__main__':
    input = read_input("input.txt")
    part_1(input)
    # direct_lines, max_value = get_direct_lines_only(input)
    # two_d_array = create_2d_array(max_value)

    


    
    
        
    
    