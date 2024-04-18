#!/usr/bin/python3


import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


def solve_nqueens_util(board, col, N):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_nqueens_util(board, col + 1, N):
                return True
            board[i][col] = 0
    return False


def solve_nqueens(N):
    board = [[0 for j in range(N)] for i in range(N)]
    if not solve_nqueens_util(board, 0, N):
        return False
    print_solution(board)
    return True


def print_solution(board):
    N = len(board)
    queens_pos = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                queens_pos.append([i, j])
    print(queens_pos)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(N)
