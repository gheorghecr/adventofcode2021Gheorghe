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
    

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = [str(line.strip()) for line in f]
    # input = ["110001010110", "011101111101", "111011110101"]
    print(binary_diagnostic_part_1(input))
    
        
    
    