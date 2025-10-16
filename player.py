import random


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


class PeakAheadAIPlayer:
    def __init__(self, mark):
        self.mark = mark

    def get_move(self, game):
        opponent = "O" if self.mark == "X" else "X"

        # 1) Win if possible
        move = self._find_winning_move(game, self.mark)
        if move:
            return move

        # 2) Block opponent's winning move
        move = self._find_winning_move(game, opponent)
        if move:
            return move

        # 3) Prefer center, then corners, then random
        if game.position_is_valid(1, 1):
            return (1, 1)

        for r, c in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if game.position_is_valid(r, c):
                return (r, c)

        spaces = game.get_available_spaces()
        return random.choice(spaces) if spaces else (0, 0)

    def _find_winning_move(self, game, mark):
        for r, c in game.get_available_spaces():
            game.board[r][c] = mark
            wins = game.check_win(mark)
            game.board[r][c] = "_"  # revert
            if wins:
                return (r, c)
        return None
