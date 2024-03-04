# 04 Rock, Paper, Scissors

This is a simple implementation of the classic Rock Paper Scissors game in Python.

## How to Play

1. Run the script using a Python interpreter.
2. When prompted, input your choice:
   - 'r' for rock
   - 'p' for paper
   - 's' for scissors
3. The computer will randomly select its choice.
4. The game will determine the winner based on the choices:
   - Rock crushes scissors
   - Scissors cuts paper
   - Paper covers rock
5. The result will be displayed in the terminal.


## Implementation Details

- The game logic is implemented in the `play()` function.
- User input is received using the `input()` function.
- The computer's choice is generated randomly using the `random.choice()` function.
- The `is_win()` function checks if the player wins based on the game rules.
- The result is displayed in the terminal, indicating whether the player won, lost, or if it's a tie.

## Example

```bash
$ python3 main.py
What's your choice? 'r' for rock, 'p' for paper, 's' for scissors
r
Player chose rock. Computer chose scissors.
You won!
```
---
<p align="right">Completed: ２０２４年０３月０４日（月）</p>