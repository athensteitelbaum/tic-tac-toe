class TicTacToeGame:
    def __init__(self):
        self.board = [
            ['X', 'O', 'X'],
            ['O', 'X', 'X'],
            ['O', 'O', 'O']
        ]
        self.welcome = """
   ________   ________  ________     ________  ________  ________     ________  ________  ________ 
  ╱        ╲ ╱        ╲╱        ╲   ╱        ╲╱        ╲╱        ╲   ╱        ╲╱        ╲╱        ╲
 ╱        _╱_╱       ╱╱         ╱  ╱        _╱         ╱         ╱  ╱        _╱         ╱         ╱
 ╱       ╱ ╱         ╱       --╱   ╱       ╱╱         ╱       --╱   ╱       ╱╱         ╱        _╱ 
 ╲______╱  ╲________╱╲________╱    ╲______╱ ╲___╱____╱╲________╱    ╲______╱ ╲________╱╲________╱   """

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
        self.board = [["_"] * 3 for _ in range(3)]
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
        if row not in range(0, 3) or col not in range(0, 3):
            return False
        if self.board[row][col] != '_':
            return False
        return True

    def test_positions(self):
        positions_to_check = [(3, 1), (-4, 1), (1, 5), (1, 1), (0, 1), (2, 2)]
        for row, col in positions_to_check:
            str_command = f"position_is_valid({row},{col})"
            print(str_command + " -> " + str(eval(str_command)))

    def check_win(self, mark):
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
        for path in VICTORY_PATHS:
            test_marks = []
            for row, col in path:
                test_marks.append(self.board[row][col])
            if test_marks.count(mark) == 3:
                return True
        return False
    
    
    def check_tie():
        return False
