# Sudoku game
# -------------------------------------------
class Validate:
    """
    Validate Class where:
    line means either row, column or box,
    validating method finds whether the line contains 0's 
    or repeated values and store it into valid variable"""
    def __init__(self, line):
        self.line = line
        self.valid = self.validating()

    def validating(self):
        if 0 in self.line or len(set(self.line)) != 9:
            return False
        return True

class ValidateBox(Validate):
    """
    Due the box size is 3 x 3 instead of being linear,
    just like rows and columns."""
    def validating(self):
        numbers = set()
        for i in range(3):
            if 0 in self.line[i]:
                return False
            numbers = numbers.union(set(self.line[i]))
        if len(numbers) != 9:
            return False
        return True


def validSolution(sudoku):
    """
    Iterates over one row, one column
    and one 3 by 3 box at a time."""
    for i in range(9):
        # validating row
        row = Validate(sudoku[i])
        if not row.valid:
            return False
        
        # validating column
        col = Validate([sudoku[j][i] for j in range(9)])
        if not col.valid:
            return False

        # validating box
        xi = i % 3 + 1
        yi = i // 3 + 1
        # selecting 3 by 3 box on sudoku
        box = [sudoku[(yi - 1) * 3: yi * 3][j][(xi - 1) * 3: xi * 3] for j in range(3)]
        box = ValidateBox(box)
        if not box.valid:
            return False

    return True