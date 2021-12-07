import numpy as np
from numpy.lib.shape_base import split

def play_bingo(draws, boards): 
    print(boards)
    for draw in draws:
        for board in boards: 
            for row in board:
                for index, row_value in enumerate(row):
                    if row[index] == draw:
                        row[index] = 'X'
                                     
        # check if there is a winner,
        for board in boards:
            result = check_winner_row(board)
            result2 = check_winner_col(board)
            if result > 0:
                return int(result) * int(draw)
            elif result2 > 0:
                return int(result2) * int(draw)
    

def check_winner_row(board):
    for row in board:
        if row.count('X') == len(row):
            # user win
            points = count_points(board)
            return points
        else:
            return 0

def check_winner_col(board):
    columns = []
    # extract columns to a separate list
    for i in range(len(board[0])):
        for board_entry in board:
            columns.append(board_entry[i])
   
   # split into separate lists for each column
    splitted_list = np.array_split(columns, 5)
    for col in splitted_list:
        num_of_x = (col == 'X').sum()
        if num_of_x == len(col):
            # user win
            points = count_points(board)
            return points
        else:
            return 0
            

def count_points(board):
    points = 0
    for row in board:
        for value in row:
            if value != 'X':
                points += int(value)
    return points


if __name__ == '__main__':
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

    print(play_bingo(draw, final_board_list_formatted))


    
    
        
    
    