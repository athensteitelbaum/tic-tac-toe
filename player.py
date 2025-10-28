import random
from game import TicTacToeGame
from copy import deepcopy

class Player:
    def __init__(self, mark):
        self.mark = mark

    def get_move(self, game):
        while True:
            try:
                user_input = input("Enter your move as 'row col' (0-2 0-2): ").strip()
                row_str, col_str = user_input.split()
                row, col = int(row_str), int(col_str)
                if game.position_is_valid(row, col):
                    return row, col
                print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Please enter two numbers like: 1 2")


class AIRandomPlayer:
    def __init__(self, mark):
        self.mark = mark

    def get_move(self, game):
        spaces = game.get_available_spaces()
        return random.choice(spaces) if spaces else (0, 0)


class PeakAheadAIPlayer (Player):
    def __init__(self, mark):
        super().__init__(mark)

    def get_move(self,game):
        available_spaces = game.get_available_spaces()
        for row, col in available_spaces:
            future_game = TicTacToeGame()
            future_game.board = deepcopy(game.board)
            future_game.board[row][col] = self.mark
            if future_game.check_win(self.mark):
                return (row, col)
            opposite_mark = 'X' if self.mark == 'O' else 'O'
            for row, col in available_spaces:
             future_game = TicTacToeGame()
             future_game.board = deepcopy(game.board)
             future_game.board[row][col] = opposite_mark
             if future_game.check_win(opposite_mark):
                return (row, col)
        row, col = random.choice(available_spaces)
        return (row, col) 