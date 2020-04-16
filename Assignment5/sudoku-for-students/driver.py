
from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv, mac, forward_checking, lcv
from backtrack import backtracking_search


def puzzleSolved(sudoku: Sudoku):
    for i in sudoku.curr_domains:
        if len(sudoku.curr_domains[i]) is not 1:
            return False
    return True


if __name__ == "__main__":

    for puzzle in [easy1, harder1]:
        s = Sudoku(puzzle)  # construct a Sudoku problem
        print("New Puzzle!")
        s.display(s.infer_assignment())
        AC3(s)
        if puzzleSolved(s):
            print("Puzzle was solved via AC3!")
            s.display(s.infer_assignment())
        else:
            print("Puzzle could not be solved")
            s.display(s.infer_assignment())
            backtracking_search(s, inference=forward_checking,
                                order_domain_values=lcv, select_unassigned_variable=mrv)
            if puzzleSolved(s):
                print("Puzzle was solved via Backtracking!")
                s.display(s.infer_assignment())
            else:
                print("Puzzle could not be solved")
                s.display(s.infer_assignment())
