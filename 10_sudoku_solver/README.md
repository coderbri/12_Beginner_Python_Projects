# 10 Sudoku Solver

## Overview

This Python project is a Sudoku solver based on the principles taught in Kylie Ying's Beginner Python Projects Course. Sudoku is a logic-based number-placement puzzle. The objective is to fill a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids that compose the grid contain all of the digits from 1 to 9.

## Recursion

Recursion is a programming technique where a function calls itself in order to solve smaller instances of the same problem. In simpler terms, recursion involves breaking down a problem into smaller, more manageable subproblems until a base case is reached, at which point the solutions to the subproblems are combined to solve the original problem.

## Logic of the Sudoku Solver

1. **Finding the Next Empty Cell**: The solver starts by finding the next empty cell (represented by -1) in the Sudoku grid.

2. **Validating Guesses**: For each empty cell, the solver iterates over possible guesses (numbers 1 to 9) and validates whether each guess is valid based on Sudoku rules (i.e., no repeated numbers in rows, columns, or 3x3 subgrids).

3. **Making Guesses and Backtracking**: If a guess is valid, the solver places the guess in the cell and recursively calls itself to solve the updated Sudoku grid. If the guess leads to a solution, the recursion stops. If the guess does not lead to a solution, the solver backtracks by resetting the cell and tries the next guess.

4. **Base Case**: The recursion stops when there are no more empty cells in the grid, indicating that the Sudoku puzzle has been solved.

## Recursion in the Project

Recursion plays a crucial role in solving the Sudoku puzzle. The `solve_sudoku()` function uses recursion to explore all possible combinations of numbers until a valid solution is found. Each recursive call attempts to fill the next empty cell with a valid number and continues until the puzzle is solved or until it encounters a dead end (i.e., no valid numbers can be placed), in which case it backtracks to try a different number.

## Usage

To use the Sudoku solver, simply provide a valid Sudoku puzzle as a 9x9 grid, where empty cells are represented by -1. Call the `solve_sudoku()` function with the puzzle grid as an argument. If a solution exists, the function will return `True`, and the puzzle grid will be updated with the solution.

```python
if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
```

## Credits
This project is inspired by Kylie Ying's Beginner Python Projects Course.

---
<p align="right">Completed: ２０２４年０３月１３日（水）</p>