from solution import play_bingo

def test_with_example_from_task_part_1():
    draws = ['7','4','9','5','11','17','23','2','0','14','21','24','10','16','13','6','15','25','12','22','18','20','8','19','3','26','1']
    boards = [[['22', '13', '17', '11', '0'], ['8', '2',  '23', '4', '24'], ['21', '9',  '14',  '16', '7'],  ['6', '10', '3', '18', '5'], ['1', '12', '20', '15', '19']], 
    [['14', '21', '17', '24',  '4'], ['10', '16', '15',  '9', '19'], ['18',  '8', '23', '26', '20'], ['22', '11', '13',  '6',  '5'], ['2' , '0' ,'12',  '3' , '7']] ]
    assert 4512 == play_bingo(draws, boards)

def test_with_input__file_task_part_1():
    with open('input.txt', 'r') as f:
        input = [str(line.strip().splitlines()) for line in f]
    draw = input[0]

    # convert draw to list
    draw = draw[2:-2].split(",")

    boards_list = input[2:]
    boards_list = [x for x in boards_list if x != '[]'] # remove empty lists
    
    # separate each boards
    x = 5
    final__board_list = [boards_list[i:i+x] for i in range(0, len(boards_list), x)]
    
    # format data to lists
    final_board_list_formatted = []
    for listt in final__board_list:
        board = []
        for value in listt:
            result = value[2: -2].split()
            board.append(result)
        final_board_list_formatted.append(board)
    assert 3048 == play_bingo(draw, final_board_list_formatted)

