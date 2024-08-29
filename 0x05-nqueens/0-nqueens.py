#!/usr/bin/python3
''' n-queen problem '''


def solve_nqueens(n):
    def is_safe(board, row, col):
        # Check this column
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def solve(board, row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)
                board[row] = -1  # Backtrack

    solutions = []
    board = [-1] * n
    solve(board, 0)
    return solutions

def format_solutions(solutions):
    formatted_solutions = []
    for sol in solutions:
        formatted_solutions.append([[row, sol[row]] for row in range(len(sol))])
    return formatted_solutions

def print_solutions(solutions):
    formatted_solutions = format_solutions(solutions)
    for board in formatted_solutions:
        print(board)

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1])
    solutions = solve_nqueens(n)
    print_solutions(solutions)

