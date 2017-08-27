import numpy as np
import random

# create a matrix with random integer
def create_board(*, n, colors=3):
    """

    :param n: dimension of the board
    :param colors: number of colors
    :return:
        np.matrix matrix n x n with random colors between 1 and 3
    """
    matrix = []
    for i in range(n):
        matrix.append([random.randint(1, colors) for a in range(n)])

    return np.matrix(matrix)


def get_tile(board):
    """
    Given a board determine the longest tile starting from the origin
    :param board:
    :return:
        list of list: each element is the el x,y of the matrix
    """
    t = [[0,0]]
    for i in range(board.shape[0] -1):
        for j in range(board.shape[1] -1):
            if board[i, j] == board[i +1, j]:
                t.append([i +1, j])
            if board[i, j] == board[i, j+1]:
                t.append([i, j+1])
            if board[i, j] == board[i+1, j+1]:
                t.append([i+1, j+1])
    # print(t)
    t = list(np.unique(t, axis=0))
    return t


def decide_color(tile, board, n, colours):
    """ Given a board decide which the color to choose
    Limitation: for now support only 3 colors

    """
    list_c = colours.copy()
    origin_color = board[0,0]
    list_c.remove(origin_color)
    colour_2 = list_c[0]
    list_c.remove(colour_2)
    colour_3 = list_c[0]
    c2_count = 0
    c3_count = 0
    for el in tile:
        el_x = el[0]
        el_y = el[1]
        if el_x + 1 < n:
            if board[el_x+1, el[1]] == colour_2:
                c2_count += 1
            if board[el_x+1, el_y] == colour_3:
                c3_count += 1
        if el_y + 1 < n:
            if board[el_x, el_y+1] == colour_2:
                c2_count += 1
            if board[el_x, el_y+1] == colour_3:
                c3_count += 1

    if c2_count > c3_count:
        colour = colour_2

    if c2_count <c3_count:
        colour = colour_3

    if c2_count == c3_count:
        colour = colour_2
    return colour


def change_color(board, tile, color):
    """ Change color of the board"""
    for el in tile:
        el_x = el[0]
        el_y = el[1]
        board[el_x,el_y] = color

n = 10
col_n = 3
colours = [i+1 for i in range(col_n)]
sample_board = create_board(n=n, colors=col_n)
moves = 0
print(sample_board)
# start game
while True:
    moves += 1
    tile = get_tile(sample_board)
    if len(tile) == (n*n):
        print(f'Total moves {moves}')
        print(sample_board)
        break
    else:
        col = decide_color(tile, sample_board, n, colours)
        print(f'Decided for color: {col}')
        change_color(sample_board, tile, col)

