from game import TicTacToeGame
from player import Player


def main():
  game = TicTacToeGame()
  players = [
    Player("X"),
    Player("O")
  ]
  
  print("TIC-TAC-TOE!")
  while True:
    for player in players:
      row, col = player.get_move(game)

    game.mark_board(player.mark, row, col)
    game.print_board()
    if game.check_win(player.mark):
           print(f"Player {player.mark} wins!!!")
           break
    

main()

