import stddraw
import random

def x_koords_to_gamefield( x):
       return int((x-25)/5)-1
    
def y_koords_to_gamefield(y):
       return int(y/5)-1
    
def gamefield_to_x_koords(gamefield):
       return ((gamefield+1)*5)+25
    
def gamefield_to_y_koords(gamefield):
       return (gamefield+1)*5

def getrandomColor():
        color = random.randint(1,3)
        if (color == 1):
          stddraw.setPenColor(stddraw.color.RED)
          return 1
        elif (color == 2):
          stddraw.setPenColor(stddraw.BLUE)
          return 2
        else:
          stddraw.setPenColor(stddraw.GREEN)
          return 3
        
def setColor(color):
        if (color == 1):
          stddraw.setPenColor(stddraw.color.RED)
          return 1
        elif (color == 2):
          stddraw.setPenColor(stddraw.BLUE)
          return 2
        else:
          stddraw.setPenColor(stddraw.GREEN)
          return 3