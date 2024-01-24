class Cell:
    def __init__(self, value, editable=True):
        self.value = value
        self.editable = editable


class Sudoku:
    def __init__(self, board):
        self.board = [[Cell(board[i][j]) for j in range(9)] for i in range(9)]

    def get_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j].value is None:
                    return self.board[i][j]
        return False

    def check_move(self, cell, value):
        row_vals = [self.board[cell.row][j].value for j in range(9)]
        col_vals = [self.board[i][cell.col].value for i in range(9)]
        box_vals = []
        start_row, start_col = 3 * (cell.row // 3), 3 * (cell.col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                box_vals.append(self.board[i][j].value)

        return value not in row_vals and value not in col_vals and value not in box_vals

    def reset(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j].editable:
                    self.board[i][j].value = None
