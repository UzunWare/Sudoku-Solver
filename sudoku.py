import math
import numpy as np


def check_vertically(board, siz, r, number_list):
    for i in range(siz):
        if board[r][i] in number_list:
            number_list.remove(board[r][i])
    return number_list


def check_horizontally(board, siz, col, number_list):
    for i in range(siz):
        if board[i][col] in number_list:
            number_list.remove(board[i][col])
    return number_list


def container_block(board, siz, srow, scol, number_list):
    for i in range(srow, siz + srow):
        for j in range(scol, siz + scol):
            if board[i][j] in number_list:
                number_list.remove(board[i][j])
    if len(number_list) == 1:
        return number_list[0]
    else:
        return 0


def fill_board(board, siz):
    srow = 0
    scol = 0
    for r in range(siz):
        for c in range(siz):
            number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            if board[r][c] == 0:
                if c < 3 and r < 3:
                    srow = 0
                    scol = 0
                elif c < 3 and r < 6:
                    srow = 3
                    scol = 0
                elif c < 3 and r < 9:
                    srow = 6
                    scol = 0
                elif c < 6 and r < 3:
                    srow = 0
                    scol = 3
                elif c < 6 and r < 6:
                    srow = 3
                    scol = 3
                elif c < 6 and r < 9:
                    srow = 6
                    scol = 3
                elif c < 9 and r < 3:
                    srow = 0
                    scol = 6
                elif c < 9 and r < 6:
                    srow = 3
                    scol = 6
                elif c < 9 and r < 9:
                    srow = 6
                    scol = 6
                number_list = check_horizontally(board, siz, c, number_list)
                number_list = check_vertically(board, siz, r, number_list)
                key = container_block(board, int(math.sqrt(siz)), srow, scol, number_list)
                if key != 0:
                    board[r][c] = key


def is_solved(board, siz):
    for i in range(siz):
        for j in range(siz):
            if board[i][j] == 0:
                return False
    return True

def compare_lists(board, copy_board):
    if len(board) != len(copy_board):
        return False
    for i in range(len(board)):
        for j in range(len(copy_board)):
            if board[i][j] == copy_board[i][j]:
                return False
    return True

def solve_sudoku(board, siz):
    keep_solving = False
    copy_board = []
    while keep_solving == False:
        copy_board = board
        fill_board(board, siz)
        if compare_lists(board, copy_board):
            print("Sorry can not solve this. Too difficult for me :(")
            break
        keep_solving = is_solved(board, siz)
    print("Before Solving: ")
    drawBoard(board, siz)
    print("After Solving: ")
    drawBoard(board, siz)



def drawBoard(board, siz):
    print("   [__________ SUDOKU BOARD __________]\n")
    for i in range(siz):
        for j in range(siz):
            print('\t', board[i][j], end='')
        print('\n')

def read_sudoku_file():
    quizzes = np.zeros((1000000, 81), np.int32)
    solutions = np.zeros((1000000, 81), np.int32)
    for i, line in enumerate(open('sudoku.csv', 'r').read().splitlines()[1:]):
        quiz, solution = line.split(",")
        for j, q_s in enumerate(zip(quiz, solution)):
            q, s = q_s
            quizzes[i, j] = q
            solutions[i, j] = s
    quizzes = quizzes.reshape((-1, 9, 9))
    solutions = solutions.reshape((-1, 9, 9))

    solve_sudoku(quizzes[300], len(quizzes[0]))
    print("Original Solution: ")
    print(solutions[300])


if __name__ == "__main__":
    #sudoku_board = [
    #    [0, 0, 0, 8, 0, 5, 0, 1, 3],
    #   [0, 0, 0, 2, 0, 3, 6, 0, 0],
    #   [6, 0, 0, 0, 9, 0, 2, 0, 4],
    #   [0, 0, 0, 0, 0, 0, 0, 0, 5],
    #   [0, 4, 0, 1, 0, 0, 7, 0, 6],
    #   [2, 5, 6, 3, 0, 4, 8, 9, 0],
    #   [5, 9, 0, 0, 0, 7, 1, 0, 2],
    #   [1, 0, 2, 0, 8, 0, 4, 7, 0],
    #   [0, 0, 4, 9, 1, 0, 0, 3, 8]
    #]
    #siz = len(sudoku_board[0])
    #solve_sudoku(sudoku_board, siz)
    read_sudoku_file()
