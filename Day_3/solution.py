from collections import Counter

def binary_diagnostic_part_1(binary_list):
    gama_rate = []
    for i in range(len(binary_list[0])):
        all_numbers_per_index = []
        for number in binary_list:
            all_numbers_per_index.append(number[i])
        gama_rate.append(int(max(set(all_numbers_per_index), key=all_numbers_per_index.count)))

    # list to int for gama rate
    gama_rate_string_array = [str(integer) for integer in gama_rate]
    game_rate_string = "".join(gama_rate_string_array)

    # get epsilon_rate by flipping game_rate_string
    epsilon_rate = ''.join('1' if x == '0' else '0' for x in game_rate_string)

    # binary int to int
    gama_rate_int = int(game_rate_string,2)
    epsilon_rate_int = int(epsilon_rate,2)

    return gama_rate_int * epsilon_rate_int

def binary_diagnostic_part_2(binary_list): 
    return get_oxygen(binary_list) * get_co2(binary_list)

def get_oxygen(binary_list):
    while len(binary_list) > 1:
        for i in range(len(binary_list[0])):
            all_numbers_per_index = []
            for number in binary_list:
                all_numbers_per_index.append(number[i])

            # get number of occurrences 0/1 to find out oxygen rate
            number_of_zeros = Counter(all_numbers_per_index)['0']
            number_of_ones = Counter(all_numbers_per_index)['1']

            if number_of_zeros > number_of_ones:
                # save all binaries that have 0 at index i
                binary_list_new = []
                for number in binary_list:
                    if number[i] == '0':
                        binary_list_new.append(number)
                binary_list = binary_list_new
            elif number_of_ones > number_of_zeros or number_of_zeros == number_of_ones: 
                # save all binaries that have 1 at index i
                binary_list_new = []
                for number in binary_list:
                    if number[i] == '1':
                        binary_list_new.append(number)
                binary_list = binary_list_new


            if len(binary_list) == 1:
                return int(binary_list[0],2)
                

def get_co2(binary_list):
    while len(binary_list) > 1:
        for i in range(len(binary_list[0])):
            all_numbers_per_index = []
            for number in binary_list:
                all_numbers_per_index.append(number[i])

            # get number of occurrences 0/1 to find out oxygen rate
            number_of_zeros = Counter(all_numbers_per_index)['0']
            number_of_ones = Counter(all_numbers_per_index)['1']

            if number_of_zeros < number_of_ones or number_of_zeros == number_of_ones:
                # save all binaries that have 0 at index i
                binary_list_new = []
                for number in binary_list:
                    if number[i] == '0':
                        binary_list_new.append(number)
                binary_list = binary_list_new
            elif number_of_ones < number_of_zeros: 
                # save all binaries that have 1 at index i
                binary_list_new = []
                for number in binary_list:
                    if number[i] == '1':
                        binary_list_new.append(number)
                binary_list = binary_list_new


            if len(binary_list) == 1:
                return int(binary_list[0],2)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = [str(line.strip()) for line in f]
    # input = ["110001010110", "011101111101", "111010110101", "111011110101"]
    print(binary_diagnostic_part_1(input))
    print(binary_diagnostic_part_2(input))
    
        
    
    