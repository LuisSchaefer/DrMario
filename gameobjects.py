import stddraw
from utils import *
from picture import Picture

class GameObject:
    def __init__(self, x, y):
        self.position = [x, y]

    def getColor(self):
       return self.color
       
class Virus(GameObject):
    def __init__(self, x, y, gamefield, color):

        self.gamefield = gamefield
        self.x = x
        self.y = y

        if (color == 1):
         stddraw.picture(Picture("assets/virus_rot.jpeg"), gamefield_to_x_koords(x+0.5, self.gamefield), gamefield_to_y_koords(y+0.5))
        elif (color == 2):
         stddraw.picture(Picture("assets/virus_blau.jpeg"), gamefield_to_x_koords(x+0.5, self.gamefield), gamefield_to_y_koords(y+0.5))
        elif (color == 3):
         stddraw.picture(Picture("assets/virus_gruen.jpeg"), gamefield_to_x_koords(x+0.5, self.gamefield), gamefield_to_y_koords(y+0.5))
        
class Pill(GameObject):
    def __init__(self, color_1, color_2, gamefield):
      
        self.gamefield = gamefield
        self.color1 = setColor(color_1)
        stddraw.filledRectangle(gamefield_to_x_koords(3, self.gamefield), gamefield_to_y_koords(15), 5, 5)
        self.rect1 = [3, 15]
        self.color2 = setColor(color_2)
        stddraw.filledRectangle(gamefield_to_x_koords(4, self.gamefield), gamefield_to_y_koords(15), 5, 5)
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.rectangle(gamefield_to_x_koords(3, self.gamefield), gamefield_to_y_koords(15), 5, 5)
        stddraw.rectangle(gamefield_to_x_koords(4, self.gamefield), gamefield_to_y_koords(15), 5, 5)
        self.rect2 = [4, 15]
        self.koords = [3, 15]
        self.rotation = 0
        

    def falling(self):
       stddraw.setPenColor(stddraw.BLACK)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect1[0], self.gamefield), gamefield_to_y_koords(self.rect1[1]), 5, 5)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect2[0], self.gamefield), gamefield_to_y_koords(self.rect2[1]), 5, 5)

       self.koords[1] = self.koords[1]-1

       
       if (self.rotation == 0 or self.rotation == 2):   
        self.rect1[1] = self.koords[1]
        self.rect2[1] = self.koords[1]
       if (self.rotation == 1):
          self.rect1[1] = self.koords[1]+1
          self.rect2[1] = self.koords[1]
       if (self.rotation == 3):
          self.rect1[1] = self.koords[1]
          self.rect2[1] = self.koords[1]+1

       setColor(self.color1)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect1[0], self.gamefield), gamefield_to_y_koords(self.rect1[1]),5,5)
       setColor(self.color2)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect2[0], self.gamefield), gamefield_to_y_koords(self.rect2[1]),5,5)
       stddraw.setPenColor(stddraw.BLACK)
       stddraw.rectangle(gamefield_to_x_koords(self.rect1[0], self.gamefield), gamefield_to_y_koords(self.rect1[1]),5,5)
       stddraw.rectangle(gamefield_to_x_koords(self.rect2[0], self.gamefield), gamefield_to_y_koords(self.rect2[1]),5,5)


       
    def rotate(self):
       if (self.rotation <= 2):
          self.rotation += 1
       else:
          self.rotation = 0
       stddraw.setPenColor(stddraw.BLACK)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect1[0], self.gamefield), gamefield_to_y_koords(self.rect1[1]), 5, 5)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect2[0], self.gamefield), gamefield_to_y_koords(self.rect2[1]), 5, 5)
       if (self.rotation == 0):
          self.rect1 = [self.rect1[0]-1, self.rect1[1]]
          self.rect2 = [self.rect2[0], self.rect2[1]-1]
          self.koords = [self.rect1[0], self.rect1[1]]          
       elif (self.rotation == 1):
          self.rect1 = [self.rect2[0], self.rect2[1]+1]
          self.koords = [self.rect2[0], self.koords[1]]
       elif (self.rotation == 2):
          self.rect1 = [self.rect2[0]+1, self.rect2[1]]
       elif (self.rotation == 3):
          self.rect1 = [self.rect2[0], self.rect2[1]]
          self.rect2 = [self.rect1[0], self.rect1[1]+1]

       setColor(self.color1)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect1[0], self.gamefield), gamefield_to_y_koords(self.rect1[1]),5,5)
       setColor(self.color2)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect2[0], self.gamefield), gamefield_to_y_koords(self.rect2[1]),5,5)
       stddraw.setPenColor(stddraw.BLACK)
       stddraw.rectangle(gamefield_to_x_koords(self.rect1[0], self.gamefield), gamefield_to_y_koords(self.rect1[1]),5,5)
       stddraw.rectangle(gamefield_to_x_koords(self.rect2[0], self.gamefield), gamefield_to_y_koords(self.rect2[1]),5,5)

       
    def move(self, direction):
       stddraw.setPenColor(stddraw.BLACK)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect1[0], self.gamefield), gamefield_to_y_koords(self.rect1[1]), 5, 5)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect2[0], self.gamefield), gamefield_to_y_koords(self.rect2[1]), 5, 5)
       
       if (self.rotation == 0):
        self.koords[0] = self.rect1[0] = self.koords[0]+direction
        self.rect2[0] = self.koords[0]+1
       elif (self.rotation == 1 or self.rotation == 3):
          self.koords[0] = self.rect1[0] = self.rect2[0] = self.koords[0]+direction
       elif (self.rotation == 2):
        self.koords[0] = self.rect2[0] = self.koords[0]+direction
        self.rect1[0] = self.koords[0]+1          
          
       setColor(self.color1)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect1[0], self.gamefield), gamefield_to_y_koords(self.rect1[1]),5,5)
       setColor(self.color2)
       stddraw.filledRectangle(gamefield_to_x_koords(self.rect2[0], self.gamefield), gamefield_to_y_koords(self.rect2[1]),5,5) 
       stddraw.setPenColor(stddraw.BLACK)
       stddraw.rectangle(gamefield_to_x_koords(self.rect1[0], self.gamefield), gamefield_to_y_koords(self.rect1[1]),5,5)
       stddraw.rectangle(gamefield_to_x_koords(self.rect2[0], self.gamefield), gamefield_to_y_koords(self.rect2[1]),5,5) 




class ColoredField(GameObject):
   
   def __init__(self, x, y, color, gamefield):
      setColor(color)
      self.gamefield = gamefield
      self.x = x
      self.y = y
      stddraw.filledRectangle(gamefield_to_x_koords(self.x, self.gamefield),gamefield_to_y_koords(self.y),5,5)
      self.color = color
      stddraw.setPenColor(stddraw.BLACK)
      stddraw.rectangle(gamefield_to_x_koords(self.x, self.gamefield),gamefield_to_y_koords(self.y),5,5)

   def falling(self):
      stddraw.setPenColor(stddraw.BLACK)
      stddraw.filledRectangle(gamefield_to_x_koords(self.x, self.gamefield), gamefield_to_y_koords(self.y),5,5)

      self.y -= 1
      setColor(self.color)
      stddraw.filledRectangle(gamefield_to_x_koords(self.x, self.gamefield), gamefield_to_y_koords(self.y),5,5)
      stddraw.setPenColor(stddraw.BLACK)
      stddraw.rectangle(gamefield_to_x_koords(self.x, self.gamefield), gamefield_to_y_koords(self.y),5,5)
      stddraw.show(100)
