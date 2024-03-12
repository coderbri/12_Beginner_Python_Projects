# Minesweeper

Minesweeper is a classic single-player puzzle game where the player must uncover all non-bomb cells on a grid without detonating any bombs. The game board consists of a grid of cells, some of which contain hidden bombs. The player must use logic to determine which cells are safe to uncover by revealing the number of neighboring bombs in each cell.


## Game Logic

1. **Board Initialization**: 
    - The game begins by creating a game board of a specified size (`dim_size`) and planting a certain number of bombs (`num_bombs`) randomly on the board.
    - Each cell on the board is initially hidden.

2. **Game Flow**:
    - The player starts by selecting a cell to uncover.
    - If the selected cell contains a bomb, the game is over, and the player loses.
    - If the selected cell does not contain a bomb, the player uncovers the cell, revealing either a number indicating the number of neighboring bombs or an empty space.
    - If an empty space is revealed, the game recursively uncovers neighboring cells until cells next to bombs are revealed.
    - The game continues until either all safe cells are uncovered (player wins) or a bomb is uncovered (player loses).

3. **Input Validation**:
    - Player input is validated to ensure it falls within the board dimensions.


## How to Play

1. **Setup**:
    - Ensure Python is installed on your system.
    - Clone or download the Minesweeper Python script.

2. **Running the Game**:
    - Open a terminal or command prompt.
    - Navigate to the directory containing the Minesweeper script.
    - Run the script using the command `python minesweeper.py`.

3. **Gameplay**:
    - The game will prompt you to enter the row and column coordinates of the cell you want to uncover.
    - Input the coordinates in the format `row,col`.
    - Continue uncovering cells until either all safe cells are revealed (you win) or a bomb is uncovered (you lose).


## Sample Gameplay

```bash
$ python3 minesweeper.py
```

<div align="center">
    <img src="" alt="minesweeper_playthrough" width="450px" height="auto">
</div>

4. **Game Over**:
    - If you uncover a cell containing a bomb, the game will display a game over message and reveal the entire board with all bomb locations.

5. **Victory**:
    - If you successfully uncover all safe cells without hitting any bombs, the game will display a victory message.


---
<p align="right">Completed: ２０２４年０３月１２日（火）</p>