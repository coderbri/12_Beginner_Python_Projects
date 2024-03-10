# 07 Tic-Tac-Toe (v2 with AI)

This project builds upon the basic [Tic-Tac-Toe game](https://github.com/coderbri/12_Beginner_Python_Projects/tree/main/06_tic_tac_toe) developed previously by introducing an AI player using the minimax algorithm. The game allows players to play against each other, against a computer player with varying levels of difficulty, or watch the AI play against itself.

## Overview

The Tic-Tac-Toe game consists of two main Python files:

1. **game.py**: This file contains the `TicTacToe` class, which represents the game board and includes methods for making moves, checking for a winner, and printing the board. The `play` function orchestrates the gameplay loop, alternating between players' turns until a winner is determined or the game ends in a tie.

2. **player.py**: This file defines different player classes, including `HumanPlayer` and `RandomComputerPlayer` for human and random AI players, respectively. The new addition, `GeniusComputerPlayer`, implements an AI player using the minimax algorithm to determine the best move.

## New Features

### GeniusComputerPlayer Class

The `GeniusComputerPlayer` class introduces an AI player that employs the minimax algorithm to make strategic moves. The minimax algorithm evaluates all possible future game states to determine the best move, aiming to maximize its chances of winning or minimizing the opponent's chances.

### Game Simulation

The updated `main` section of **game.py** includes a simulation loop where the AI player competes against itself for a specified number of iterations. This allows us to observe the performance of the AI and gather statistics on the outcomes of the games.

## Usage

To play the game interactively, simply run **game.py** and follow the prompts to make moves.

To watch the AI player compete against itself, execute **game.py** and uncomment the simulation loop. You can adjust the number of iterations to simulate more or fewer games.

```zsh
coderBri@Bri-MBP 07_tic_tac_toe_AI % python3 game.py
After 1000 iterations, we see 808 X wins, 0 O wins, and 192 ties.
```

<!-- ## Future Improvements

Possible enhancements to the project include:

- Implementing additional AI algorithms for different levels of difficulty.
- Enhancing the user interface with graphics or a GUI.
- Adding support for larger board sizes or different game variants. -->

---
<p align="right">Completed: ２０２４年０３月０９日（土）</p>

