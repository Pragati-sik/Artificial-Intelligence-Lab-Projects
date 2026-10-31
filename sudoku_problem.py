
# Sudoku Solver using Backtracking

# 0 represents an empty cell

sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


# Check whether a number can be placed
def is_safe(row, col, num):

    # Check row
    for i in range(9):
        if sudoku[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    # Check 3x3 sub-grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:
                return False

    return True


# Solve Sudoku using Backtracking
def solve():

    for row in range(9):
        for col in range(9):

            # Find empty cell
            if sudoku[row][col] == 0:

                # Try numbers from 1 to 9
                for num in range(1, 10):

                    if is_safe(row, col, num):

                        sudoku[row][col] = num

                        if solve():
                            return True

                        # Backtrack
                        sudoku[row][col] = 0

                return False

    return True


# Print Sudoku
if solve():
    print("Solved Sudoku:")

    for row in sudoku:
        print(row)
else:
    print("No solution exists")
