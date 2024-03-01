# Guess the Number (Computer Version) README

### Game Logic
The "Guess the Number" game is a simple Python program where the computer selects a random number within a specified range, and the player tries to guess that number. Here's how the game works:
1. The program prompts the player to guess a number within a specified range.
2. The player inputs their guess.
3. If the guess is incorrect, the program provides feedback to the player, indicating whether the guess was too high or too low.
4. The player continues to guess until they correctly guess the number chosen by the computer.
5. Once the correct number is guessed, the program congratulates the player and reveals the random number.

## Random Module Usage
The random module in Python is used to generate random numbers. In this game, the random module is employed to select a random number within the specified range (`1` to `x`, where `x` is the upper limit provided by the player). Here's how the random module is used in the program:
- `random.randint(a, b)`: This function generates a random integer between the specified `a` (inclusive) and `b` (inclusive) parameters. In the "Guess the Number" game, `random.randint(1, x)` is used to select a random number between `1` and the upper limit `x` provided by the player.

#### Example Execution
Here's an example of how the game runs:
1. Player specifies the range (e.g., `10`).
2. Computer randomly selects a number between `1` and `10`.
3. Player guesses a number (e.g., `5`).
4. If the guess is incorrect, the program provides feedback (e.g., "Too low.") and prompts the player to guess again.
5. Player continues guessing until they correctly guess the random number.
6. Once the correct number is guessed, the program congratulates the player and reveals the random number.

This project serves as a practical example of utilizing Python's random module to create an interactive guessing game.

---
<p align="right">Completed: ２０２４年０２月２８日（水）</p>