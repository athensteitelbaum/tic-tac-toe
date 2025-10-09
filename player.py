
from game import TicTacToeGame
import random
class Player:
    def __init__(self,mark):
        self.mark = mark
    
    def get_move(self,game):
       while True:
        try:
         print("input a row and col!")
         row, col = input().split(',')
         row = int(row.strip())
         col = int(col.strip())
         if game.position_is_valid(row,col):
            return row,col
         else:
            print("You can't go there - Try again!")
        except:
           print("Invalid input, try again")
      
class AIRandomPlayer:
   def __init__(self,mark):
      self.mark = mark 

   def get_move(self,game):
      available_spaces = game.get_available_spaces()
       
      row, col = random.choice(available_spaces)
      return (row,col)
       

