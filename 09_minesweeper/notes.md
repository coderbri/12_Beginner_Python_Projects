# Minesweeper - Game Logic

1. **Board Class**:
    - `__init__(self, dim_size, num_bombs)`: Initializes the board with the given dimensions and number of bombs. It creates the board, plants the bombs, and assigns values to each cell indicating the number of neighboring bombs.
    
    - `make_new_board(self)`: Creates a new board and randomly plants bombs on it.
    
    - `assign_values_to_board(self)`: Assigns values to each cell on the board indicating the number of neighboring bombs.
    
    - `get_num_neighboring_bombs(self, row, col)`: Counts the number of neighboring bombs for a given cell.
    
    - `dig(self, row, col)`: Allows the player to dig at a specified location. If the location has a bomb, the game is over. If it's an empty cell, it recursively digs neighboring cells until cells next to bombs are revealed.
    
    - `__str__(self)`: Converts the board state into a string representation to display to the player.

2. **play() Function**:
    - `play(dim_size=10, num_bombs=10)`: Initiates the game. It creates a new board, displays it to the player, prompts the player for input on where to dig, and continues until the game is won or lost.

3. **Game Flow**:
    - The game continues until either all non-bomb cells are dug, resulting in victory, or the player digs a cell with a bomb, resulting in defeat.
    - During each turn, the player inputs the row and column coordinates to dig.
    - The `dig()` method is called to dig at the specified location.
    - If the dig uncovers a bomb, the game ends. Otherwise, it continues until either all safe cells are uncovered or a bomb is uncovered.

4. **Input Validation**:
    - The input from the player is validated to ensure it falls within the board dimensions.

5. **Output**:
    - The game provides feedback to the player after each move, indicating whether they won or lost.

Overall, the code follows the classic rules and logic of Minesweeper, where the player must uncover all non-bomb cells without detonating any bombs. The game utilizes recursion to reveal neighboring cells and ensures proper validation of user input.