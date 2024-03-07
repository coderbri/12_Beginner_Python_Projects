import time
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to represent 3x3 board
        self.current_winner = None # keep track of winner
    
    def print_board(self):
        for row in [self.board[i*3: (i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        #  0 | 1 | 2 etc (tells us number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        '''Alternative to:
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves
        '''
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            # how do we check for a winner? that needs to be checked after a move is made?
            if self.determine_winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def determine_winner(self, square, letter):
        # winner if 3 in a row anywhere — but we have to check all possibilities!
        # first check row
        row_idx = square // 3 # the "//" will check how many times does 3 go into sqaure
        row = self.board[row_idx * 3 : (row_idx + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        # if not, keep going --> check column
        col_idx = square % 3
        column = [self.board[col_idx + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        # if not, keep going --> check diagonals
        # but only if the sqaure is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # top left to bottom right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # top right to bottom left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        
        # if all of these fail
        return False


def play(game, x_player, o_player, print_game=True):
    # returns the winner of the game(the letter that gave the win) or None for a tie
    if print_game:
        game.print_board_nums()
    
    letter = 'X' # starting letter
    '''
    iterate while the game still has empty squares
    (we don't have to worry about winner as that result
    will be returned which breaks the loop) 
    '''
    while game.empty_squares():
        # get the move from the appropiate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to sqaure {square}')
                game.print_board()
                print('') # just an empty line
        
        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
            return letter
        
        # after we made our move, we need to alternate letters
        letter = 'O' if letter == 'X' else 'X'
        '''
        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'
        '''
    
    # tiny break so computer feedback doesn't occur so fast
    time.sleep(0.8)
    
    if print_game:
        print('It\'s a tie!')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    tttGame = TicTacToe()
    play(tttGame, x_player, o_player, print_game=True)