import stddraw
import random

class GameObject:
    def __init__(self, x, y):
        self.position = [x, y]
        self.idle = True
        self.size

    def getrandomColor(self):
        self.color = random.randint(1,3)
        if (self.color == 1):
          stddraw.setPenColor(stddraw.color.RED)
          return 1
        elif (self.color == 2):
          stddraw.setPenColor(stddraw.BLUE)
          return 2
        else:
          stddraw.setPenColor(stddraw.GREEN)
          return 3
        
    def getColor(self, color):
        if (color == 1):
          stddraw.setPenColor(stddraw.color.RED)
          return 1
        elif (color == 2):
          stddraw.setPenColor(stddraw.BLUE)
          return 2
        else:
          stddraw.setPenColor(stddraw.GREEN)
          return 3
               
class Virus(GameObject):
    def __init__(self, x, y):
        self.idle = True
        #Rot = 1, Blau = 3, Grün = 3
        self.color = self.getrandomColor()

        stddraw.filledRectangle(x, y, 5, 5)

class Pill(GameObject):
    def __init__(self):
        self.idle = False
        self.color1 = self.getrandomColor()
        #print(self.color1)
        stddraw.filledRectangle(45, 80, 5, 5)
        self.rect1 = [45, 80]
        self.color2 = self.getrandomColor()
        #print(self.color2)
        stddraw.filledRectangle(50, 80, 5, 5)
        self.rect2 = [50, 80]
        self.koords = [45, 80]
        self.rotation = 0

    def falling(self):
       stddraw.setPenColor(stddraw.BLACK)
       stddraw.filledRectangle(self.rect1[0], self.rect1[1], 5, 5)
       stddraw.filledRectangle(self.rect2[0], self.rect2[1], 5, 5)

       self.koords[1] = self.koords[1]-5

       self.getColor(self.color1)
       self.rect1[1] = self.koords[1]
       stddraw.filledRectangle(self.rect1[0], self.rect1[1],5,5)
       self.getColor(self.color2)
       self.rect2[1] = self.koords[1]
       stddraw.filledRectangle(self.rect2[0], self.rect2[1],5,5)


       
    def rotate(self):
       if (self.rotation <= 2):
          self.rotation += 1
       else:
          self.rotation = 0

       stddraw.filledRectangle(self.rect1[0], self.rect1[1], 5, 5)
       stddraw.filledRectangle(self.rect2[0], self.rect2[1], 5, 5)
       if (self.rotation == 0):
          self.rect1 = [self.rect1[0]-5, self.rect1[1]]
          self.rect2 = [self.rect2[0], self.rect2[1]-5]
          self.koords = [self.rect1[0], self.rect1[1]]          
       elif (self.rotation == 1):
          self.rect1 = [self.rect2[0], self.rect2[1]+5]
          self.koords = [self.rect2[0], self.koords[1]]
       elif (self.rotation == 2):
          self.rect1 = [self.rect2[0]+5, self.rect2[1]]
       elif (self.rotation == 3):
          self.rect1 = [self.rect2[0], self.rect2[1]]
          self.rect2 = [self.rect1[0], self.rect1[1]+5]

       print("Rotierung: " + str(self.rotation) + " X: " + str(self.koords[0]) + " Y: " + str(self.koords[1]))
       self.getColor(self.color1)
       stddraw.filledRectangle(self.rect1[0], self.rect1[1],5,5)
       self.getColor(self.color2)
       stddraw.filledRectangle(self.rect2[0], self.rect2[1],5,5)
       
    def move(self, direction):
       stddraw.setPenColor(stddraw.BLACK)
       stddraw.filledRectangle(self.koords[0], self.koords[1], 10,5)
       
       if (self.rotation == 0):
        self.koords[0] = self.rect1[0] = self.koords[0]+direction
        self.rect2[0] = self.koords[0]+5
        self.getColor(self.color1)
        stddraw.filledRectangle(self.koords[0], self.koords[1],5,5)
        self.getColor(self.color2)
        stddraw.filledRectangle(self.koords[0]+5, self.koords[1],5,5)
       elif (self.rotation == 1):
          pass
       elif (self.rotation == 2):
          pass
       elif (self.rotation == 4):
          pass        



class ColoredField(GameObject):
   
   def __init__(self, x, y, color):
      self.getColor(color)
      self.koords = [x, y]
      stddraw.filledRectangle(x,y,5,5)


   def falling():
    pass