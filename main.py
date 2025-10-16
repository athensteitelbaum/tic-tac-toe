from game import TicTacToeGame
from player import Player, AIRandomPlayer, PeakAheadAIPlayer


def main():
    game = TicTacToeGame()
    players = [
        Player("X"),
        PeakAheadAIPlayer("O")
    ]

    print(game.welcome)
    game.reset_board()
    game.print_board()

    while True:
        for player in players:
            row, col = player.get_move(game)
            game.mark_board(player.mark, row, col)
            game.print_board()
            if game.check_win(player.mark):
                print(f"Player {player.mark} wins!!!")
                print("Let's Play Again")
                game.reset_board()
                break


if __name__ == "__main__":
    main()
