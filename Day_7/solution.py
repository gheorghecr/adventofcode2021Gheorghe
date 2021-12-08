from statistics import median

def read_input(filename):
    input = [int(value) for value in open(filename).read().split(',')]
    return input


def part_1(input):
    median_value = int(median(input))
    # fuel = 0
    # for i, value in enumerate(input):
    #     if value > median_value:
    #         fuel += value - median_value
    #         input[i] = median_value
    #     else:
    #         fuel += median_value - value
    #         input[i] = median_value

    # return fuel
    return sum(abs(n - median_value) for n in input)

def part_2(input):
    target_value = (sum(input) + 1) // len(input)
    
    return(sum(abs(n - target_value) * (abs(n - target_value) + 1) // 2 for n in input))
                

if __name__ == '__main__':
    # input = read_input("input_example.txt")
    input = read_input("input.txt")
    print(part_1(input))
    print(part_2(input), "here")

    


    
    
        
    
    