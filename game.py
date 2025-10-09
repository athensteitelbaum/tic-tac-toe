class TicTacToeGame:
    def __init__(self):
        self.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'X'],
            ['O', 'O', 'O']
        ]
        self.reset_board()
    
    def get_available_spaces(self):
        available_spaces = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "_":
                    available_spaces.append((row, col))

        return available_spaces


    def mark_board(self, mark, row, col):
        self.board[row][col] = mark

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = "_"

    def print_board(self):
        for row in range(3):
            for col in range(3):
                print(self.board[row][col], end=" ")
            print()
        print()

    def position_is_valid(self, row, col):
        if not (0 <= row < 3 and 0 <= col < 3):
            return False
        return self.board[row][col] == '_'

    def test_positions(self):
        positions_to_check = [(3, 1), (-4, 1), (1, 5), (1, 1), (0, 1), (2, 2)]
        for row, col in positions_to_check:
            print(f"position_is_valid({row}, {col}) -> {self.position_is_valid(row, col)}")

    VICTORY_PATHS = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(2, 0), (1, 1), (0, 2)]
    ]

    def check_win(self, mark):
        for path in self.VICTORY_PATHS:
            if all(self.board[r][c] == mark for r, c in path):
                return True
        return False
