# Number Guessing Game (User Version)

This Python project implements a number-guessing game where the computer tries to guess the user's number. It is based on the project, [Number Guessing Game (Computer Version)](../02_number_guessing_game_computer/).

## 1. `guess(x)`

This function allows the user to guess a randomly generated number within a specified range.

### Logic:
- The computer generates a random number between 1 and the specified upper limit `x`.
- The user is prompted to input guesses until they correctly guess the randomly generated number.
- Feedback is provided after each guess, informing the user if their guess was too low or too high.

## 2. `computer_guess(x)`

This function implements the reverse scenario, where the computer attempts to guess the user's number.

### Logic:
- The computer starts with an initial range between 1 and the specified upper limit `x`.
- It iteratively makes guesses within this range based on user feedback.
- If the user's feedback indicates the guess is too high, the upper bound of the range is adjusted accordingly.
- If the feedback indicates the guess is too low, the lower bound of the range is adjusted.
- The process continues until the computer correctly guesses the user's number or the user quits the game by typing 'q'.

### Commented-Out Code:
- The commented-out code section explains a potential alternative approach that automatically determines the correct answer. However, it's commented out to maintain user interaction.

---
<p align="right">Completed: ２０２４年０３月０１日（金）</p>