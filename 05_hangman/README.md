# 05 Hangman

This Hangman game is a simple console-based game implemented in Python. It allows users to guess letters to uncover a hidden word before running out of lives.

## How to Play

1. Run the `hangman.py` script.
2. The game will randomly select a word from the provided list of words in `words.py`.
3. You have 7 lives to start with.
4. Guess letters one at a time.
5. If the guessed letter is correct, it will be revealed in the word.
6. If the guessed letter is incorrect, you lose a life.
7. Keep guessing until you either uncover the entire word or run out of lives.

## Files

### `hangman.py`

This is the main script that implements the Hangman game logic. It imports the list of words from `words.py` and the visual representations of the Hangman stages from `hangman_visual.py`.

### `hangman_visual.py`

This file contains a dictionary mapping each stage of the Hangman to its visual representation. These visuals are displayed as ASCII art in the console to represent the Hangman's current state.

### `words.py`

Contains a list of words for the Hangman game to choose from. Make sure to customize this list with your own words if desired.

## Dependencies

This game requires Python 3.x to run. No additional dependencies are needed.

## How to Run

Simply run the `hangman.py` script using Python 3.x.

```bash
python3 hangman.py
```

## Screenshots

### Winning Hangman Demo
![Gameplay Screenshot](./imgs/Hangman-Demo-Win.GIF)

### Losing Hangman Demo
![Gameplay Screenshot](./imgs/Hangman-Demo-Loss.GIF)

---
<p align="right">Completed: ２０２４年０３月０５日（水）</p>