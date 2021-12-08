from collections import Counter

def read_input(filename):
    with open(filename) as f:
        input = Counter(map(int, f.read().split(',')))
    return input


def part_1_and_2(input, number_of_days):
    for _ in range(number_of_days):
        new_fish = {timer - 1: count for timer, count in input.items()}
        new_fish.pop(-1, None)
        if 0 in input:
            new_fish[8] = input[0]
            new_fish[6] = input[0] + new_fish.get(6, 0)
        input = new_fish
    return sum(input.values())
                

if __name__ == '__main__':
    input = read_input("input.txt")
    print(part_1_and_2(input, 80))
    print(part_1_and_2(input, 256))

    


    
    
        
    
    