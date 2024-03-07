import math
import random

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter
    
    # Let all players get their next move given a game
    def get_move(self, game):
        pass

# Implement Inheritance
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        # return super().get_move(game)
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            '''Accomplish a series of checks:
            we're going to check that this is a correct value by trying to cast
            it to an integer, and if it's not, and if not, then we say its invalid
            if that spot is not available on the board, we also say its invalid
            '''
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print('Invalid square. Please try again.')
        
        return val
