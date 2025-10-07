from game import TicTacToeGame
class Player:
    def __init__(self, mark):
        self.mark = mark   

    def get_move(self, game):
        while True:
            try:
                row, col = input("Enter move as row,col: ").split(',')
                row = int(row.strip())
                col = int(col.strip())
                
                if game.position_is_valid(row, col):
                    return row, col
                else:
                    print("You can't go there - try again!")
            except:
                print("Invalid input, try again")
