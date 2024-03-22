# 12 Beginner Python Projects

Based on this [freeCodeCamp Beginner Python Projects coding course](https://youtu.be/8ext9G7xspg?si=0wxN4enC_zf7KdcQ) by Kylie Ying.


### 1. [Madlibs](01_madlibs/)

The **Madlibs project** is a Python program that demonstrates string manipulation techniques, particularly string concatenation with f-strings, and user interaction through the input function. Users provide words and phrases which are then dynamically incorporated into a predefined Madlib template, showcasing how Python can generate personalized narratives based on user input. This specific Madlib adventure, titled "VISITING CHINA," serves as an example, where users input various details to create a customized story set in China.


### 2. [Number Guessing Game (Computer Version)](02_number_guessing_game_computer/)

The **Number Guessing Game** project demonstrates the use of the random module to create an interactive guessing game. In this game, the computer selects a random number within a specified range, and the player attempts to guess that number. Through a series of input prompts and feedback messages, the player refines their guesses until they correctly identify the randomly chosen number.


### 3. [Number Guessing Game (User Version)](03_number_guessing_game_user/)

Similar to the previous project, this version of the **Number Guessing Game** implements two modes of playing: one where the user guesses a randomly generated number and another where the computer attempts to guess the user's chosen number. In the user-guessing mode, players input guesses until they correctly identify the randomly generated number, receiving feedback after each attempt. In the computer-guessing mode, the computer iteratively makes guesses based on user feedback, adjusting its strategy until it identifies the user's number or the user opts to quit the game. The project highlights key programming concepts like loops, conditionals, user input handling, and random number generation, ensuring an engaging and dynamic experience. Additionally, users have the option to exit the game at any time by typing 'q'.


### 4. [Rock Paper Scissors](04_rock_paper_scissors/)

In this **Rock Paper Scissors** game, players can input their choice ('r' for rock, 'p' for paper, 's' for scissors), and the computer will randomly select its choice. The game logic determines the winner based on the traditional rules: rock crushes scissors, scissors cuts paper, and paper covers rock. The result is displayed in the terminal, indicating whether the player won, lost, or if it's a tie. 


### 5. [Hangman](05_hangman/)

The **Hangman** game project is a Python-based console game that challenges players to guess a hidden word before running out of lives. The game randomly selects a word from a predefined list and presents it as a series of dashes representing each letter. Players guess letters one at a time, with correct guesses revealing the corresponding letters in the word, while incorrect guesses deduct lives. The game incorporates ASCII art to visually represent the Hangman's stages as players progress.


### 6. [Tic-Tac-Toe](06_tic_tac_toe/)

The **Tic-Tac-Toe** project is a simple yet classic implementation of the popular game in Python. It allows two players to compete against each other, with one player being a human and the other being a computer (or another player*). The game logic is encapsulated within the `TicTacToe` class, where the board is represented as a single list and moves are validated and executed accordingly. Players can make their moves either by inputting their choice as a human player or by having the computer randomly select its moves as the opponent. The game continues until one player achieves three marks in a row (horizontally, vertically, or diagonally) or until the board is full without a winner, resulting in a tie. The project demonstrates basic concepts of object-oriented programming, inheritance, and game logic implementation in Python.


### 7. [Tic-Tac-Toe AI](07_tic_tac_toe_AI/)

The updated version of this **Tic-Tac-Toe** game introduces a more challenging opponent with the addition of the `GeniusComputerPlayer` class, which utilizes the minimax algorithm to make strategic moves. This AI player evaluates all possible future game states to determine the optimal move, providing a more engaging experience for players seeking a tougher challenge. Additionally, the project includes a simulation loop that allows users to observe the AI player competing against itself, providing insights into its performance and effectiveness. With these enhancements, the tic-tac-toe game offers an improved gaming experience, combining classic gameplay with advanced AI techniques.


### 8. [Binary Search](08_binary_search/)

The **Binary Search** project showcases the implementation and comparison of two fundamental search algorithms: naive search and binary search. Naive search involves sequentially scanning a list to find a target value, while binary search leverages the concept of divide and conquer to efficiently locate the target in a sorted list. The Python code provided demonstrates these algorithms' functionality and performance difference by measuring the time taken to search for elements in a sorted list.
<!-- Through this project, users can understand the logic behind both search algorithms and appreciate the significant efficiency improvement offered by binary search, particularly for large datasets. -->


### 9. [Minesweeper](09_minesweeper/)

This project implements the classic **Minesweeper** game in Python, allowing players to experience the familiar puzzle challenge of uncovering safe cells while avoiding hidden bombs on a grid-based game board. The game logic is implemented through a `Board` class, which dynamically generates a game board with randomly placed bombs and assigns values to each cell indicating the number of neighboring bombs. Players interact with the game by selecting cells to uncover, and the game recursively reveals neighboring cells until all safe cells are uncovered or a bomb is hit. Input validation ensures that players input valid cell coordinates. This implementation provides a console-based Minesweeper experience in the Python environment.


### 10. [Sudoku Solver](10_sudoku_solver/)

This Python **Sudoku Solver** project utilizes recursion to efficiently solve Sudoku puzzles. Recursion is a key programming technique where a function calls itself to solve smaller instances of the same problem, eventually reaching a base case. The solver systematically fills empty cells in the Sudoku grid with valid numbers, backtracking when necessary if a guess leads to a dead end. By recursively exploring all possible combinations of numbers, the solver determines the correct arrangement of digits that satisfies Sudoku rules. This project provides a clear demonstration of how recursion can be applied to solve complex logic puzzles like Sudoku.


### 11. [Photo Manipulation](11_photo_manipulation/)

This **Photo Manipulation** project is a Python-based photo manipulation tool in which it enables users to perform various image editing operations such as brightening, contrast adjustment, blur, edge detection, and image combination. Each function within the `transform.py` script applies a specific manipulation technique to input images, producing modified versions as output. Overall, the project offers a simple yet effective tool for performing basic photo editing tasks using Python.

### 12. Markov Chain Composer

<!-- The **Markov Chain Text Composer** is a Python-based tool designed to generate new text compositions inspired by existing sources, such as song lyrics. Leveraging the principles of Markov chains, graph theory, and probability, the tool analyzes input text data to model the statistical relationships between words. The project consists of several modules, each serving a specific function: `lyrics.py` facilitates the retrieval and storage of song lyrics using the Genius API, `graph.py` constructs and manipulates graph structures to represent word relationships, and `compose.py` orchestrates the composition process using the Markov Chain model. By combining these components, the Markov Chain Text Composer can create compelling and coherent text compositions that mimic the style and structure of the original input text. Whether used for artistic expression, creative writing, or linguistic analysis, this project offers a versatile and powerful tool for generating unique textual content. -->

---
**Duration:** ２０２４年０２月２８日（水）ー ２０２４年０３月２１日（木）