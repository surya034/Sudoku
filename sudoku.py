import tkinter as tk


def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    s = 3
    start_row = row - row % s
    start_col = col - col % s

    for r in range(start_row, start_row + s):
        for c in range(start_col, start_col + s):
            if board[r][c] == num:
                return False
    return True


def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False


def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def solve():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            x = entry_grid[i][j].get()
            if x.isdigit():
                board[i][j] = int(x)

    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                entry_grid[i][j].delete(0, tk.END)
                entry_grid[i][j].insert(0, str(board[i][j]))
    else:
        result_label.config(text="No solution found!")


# ...


def solve():
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            x = entry_grid[i][j].get()
            if x.isdigit():
                board[i][j] = int(x)

    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:  # Preserve initial input values
                    entry_grid[i][j].delete(0, tk.END)
                    entry_grid[i][j].insert(0, str(board[i][j]))
    else:
        result_label.config(text="No solution found!")


root = tk.Tk()
root.title("Sudoku Solver")


entry_grid = []
for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(root, width=2, font=("Helvetica", 20))
        entry.grid(row=i, column=j)
        row_entries.append(entry)
    entry_grid.append(row_entries)
solve_button = tk.Button(root, text="Solve Sudoku", command=solve)
solve_button.grid(row=9, columnspan=9)
result_label = tk.Label(root, text="")
result_label.grid(row=10, columnspan=9)

root.mainloop()
