# hangman.py - Logic Elaborated

1. **Importing Libraries**: The script begins by importing necessary libraries including `random`, `string`, and two modules from the project: `words` and `hangman_visual`.

2. **`get_valid_word` Function**: This function selects a valid word from the list of words provided in the `words` module. It ensures that the chosen word does not contain hyphens or spaces, which are not valid for the Hangman game. The selected word is converted to uppercase and returned.

3. **`hangman` Function**: This is the main function responsible for running the Hangman game. It begins by calling `get_valid_word` to choose a word for the game. Key variables such as `word_letters` (set of letters in the word), `alphabet` (set of uppercase alphabet letters), `used_letters` (set of letters guessed by the user), and `lives` (number of remaining lives) are initialized.

4. **Game Loop**: The game continues in a loop as long as there are letters remaining to be guessed (`len(word_letters) > 0`) and the player has remaining lives (`lives > 0`). Within each iteration of the loop:

   - The user is informed about the number of remaining lives and the letters they have guessed so far.

   - The current state of the word (with guessed letters revealed and dashes for unguessed letters) is displayed.

   - The user is prompted to guess a letter.

   - Input validation is performed to ensure that the guessed letter is a valid uppercase letter that has not been guessed before.

   - If the guessed letter is correct, it is added to the set of used letters, and occurrences of the letter in the word are removed from the set of word letters.

   - If the guessed letter is incorrect, the player loses a life, and a message is displayed.

   - If the guessed letter has already been used, the player is informed, and they are prompted to guess again.

   - If the input is invalid (e.g., not an uppercase letter), an appropriate message is displayed.

5. **End of Game**: The game loop terminates when either all letters have been guessed (`len(word_letters) == 0`) or the player runs out of lives (`lives == 0`). Depending on the outcome:

   - If the player runs out of lives, a message indicating failure is displayed along with the correct word.
   
   - If the player successfully guesses the word, a congratulatory message is displayed.

6. **Main Block**: The `hangman` function is called when the script is executed directly (`__name__ == '__main__'`). This allows the game to be played by running the script.

Overall, the script provides a complete implementation of the classic Hangman game, allowing users to interactively guess letters and try to uncover a hidden word within a limited number of attempts.