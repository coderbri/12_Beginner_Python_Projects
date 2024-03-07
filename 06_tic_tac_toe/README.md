# 06 Tic-Tac-Toe

This is a simple implementation of the classic Tic Tac Toe game in Python. The game allows two players to play against each other: one player being a human and the other being a computer.

## Contents

- [Overview](#overview)
- [Player Types](#player-types)
  - [Human Player](#human-player)
  - [Random Computer Player](#random-computer-player)
- [Tic Tac Toe Logic](#tic-tac-toe-logic)
  - [Board Representation](#board-representation)
  - [Available Moves](#available-moves)
  - [Making a Move](#making-a-move)
  - [Determining the Winner](#determining-the-winner)
- [How to Play](#how-to-play)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Tic Tac Toe game consists of a 3x3 grid where two players take turns marking spaces ('X' or 'O') until one player wins by getting three of their marks in a horizontal, vertical, or diagonal row, or if the board is full without a winner, resulting in a tie.

## Player Types

### Human Player

The `HumanPlayer` class represents a player controlled by a human. This player type prompts the user for input to make their move. If the input is invalid (e.g., not within the available moves or not an integer), the player is prompted to try again until a valid move is entered.

### Random Computer Player

The `RandomComputerPlayer` class represents a player controlled by the computer. This player type randomly selects an available move from the list of available moves on the board.

## Tic Tac Toe Logic

### Board Representation

The game board is represented by a single list of length 9, with each element representing a space on the 3x3 grid. Empty spaces are represented by a space character (' '), and player moves are represented by their respective letters ('X' or 'O').

### Available Moves

The `available_moves()` method returns a list of indices representing the available moves on the board. These are the indices corresponding to empty spaces (' ') on the board.

### Making a Move

The `make_move()` method takes a square index and a player's letter as input. It checks if the move is valid (i.e., if the square is empty) and makes the move if valid. After making the move, it checks for a winner.

### Determining the Winner

The `determine_winner()` method checks if the latest move resulted in a win for the player. It checks all possible winning combinations: rows, columns, and diagonals.

## How to Play

To play the Tic Tac Toe game, simply run the `game.py` script. You will be prompted to input your move as a human player, and the computer will randomly select its moves as the opponent. The game will continue until there is a winner or a tie.

## Usage

To play the game, execute the following command in your terminal:

```bash
python game.py
```

<!-- ![Tic-Tac-Toe Game Demo](./imgs/TicTacToe-demo.png) -->

---
<p align="right">Completed: ２０２４年０３月０５日（水）</p>