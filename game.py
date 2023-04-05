import sys
import stddraw
import random
from gameobjects import Virus, Pill, ColoredField
import pygame.key

class DrMario:
    def __init__(self, difficulty, speed, player):
        stddraw.setCanvasSize(900,900)
        stddraw.setXscale(0,100)
        stddraw.setYscale(0,100)
        self.difficulty = int(difficulty)*4+4
        self.speed = speed
        b = False
        #init gametable
        #background
        r = c = 0
        while r < stddraw._canvasHeight:
            while c < stddraw._canvasWidth:
                stddraw.filledRectangle(c, r, 5, 5)
                if (b == True):
                  stddraw.setPenColor(stddraw.color.BLACK)
                  b = False
                else:
                  stddraw.setPenColor(stddraw.color.GRAY)
                  b = True
                c += 5
            r += 5
            c = 0
            if (b == True):
              stddraw.setPenColor(stddraw.color.BLACK)
              b = False
            else:
              stddraw.setPenColor(stddraw.color.GRAY)
              b = True
        stddraw.setPenColor(stddraw.color.BLACK)
        stddraw.filledRectangle(30, 5, 40, 80)
        stddraw.filledRectangle(45,85,10,10)  
        stddraw.filledRectangle(75, 60, 20, 20)
        stddraw.setPenColor(stddraw.CYAN)
        stddraw.rectangle(30,5,40,80)
        stddraw.line(45,85,45,95)
        stddraw.line(55,85,55,95)
        stddraw.line(45,95,55,95)
        self.fallingpill = []
        self.fallingpill.append(Pill())
        self.coloredField = []
        self.gamefield = [[0 for j in range(16)] for i in range(8)]
        #init virus
        r = 0
        x = y = 1
        while r < self.difficulty:
            
            x = random.randint(1, 8)
            y = random.randint(1, 13)

            while (self.gamefield[x-1][y-1] == 1):
              x = random.randint(1, 8)
              y = random.randint(1, 13) 

            self.gamefield[x-1][y-1] = 1
            Virus(x*5+25, y*5)
            r += 1
        stddraw.show(10)
        self.main_loop()


    def main_loop(self):
      while True:
       self.input()
       self.logic()
       self.draw()

    def input(self):
       is_key_pressed = pygame.key.get_pressed()
       if is_key_pressed[pygame.K_a]:
          self.fallingpill[0].move(-5)
       if is_key_pressed[pygame.K_d]:
          self.fallingpill[0].move(5)
       if is_key_pressed[pygame.K_SPACE]:
          self.fallingpill[0].rotate()
       

    def logic(self):
        #print(self.y_koordstogamefield(self.fallingpill[0].koords[1]))
        if (self.gamefield[self.x_koordstogamefield(self.fallingpill[0].koords[0])][self.y_koordstogamefield(self.fallingpill[0].koords[1])-1] == 1 or self.gamefield[int((self.fallingpill[0].koords[0]-20)/5)-1][self.y_koordstogamefield(self.fallingpill[0].koords[1])-1] == 1 or self.y_koordstogamefield(self.fallingpill[0].koords[1]) == 0):
         self.coloredField.append(ColoredField(self.fallingpill[0].rect1[0], self.fallingpill[0].rect1[1], self.fallingpill[0].color1))
         self.coloredField.append(ColoredField(self.fallingpill[0].rect2[0], self.fallingpill[0].rect2[1], self.fallingpill[0].color2))
         self.gamefield[self.x_koordstogamefield(self.coloredField[-1].koords[0])][self.y_koordstogamefield(self.coloredField[-1].koords[1])] = self.gamefield[self.x_koordstogamefield(self.coloredField[-2].koords[0])][self.y_koordstogamefield(self.coloredField[-2].koords[1])] = 1
         self.fallingpill.clear()

        if (not self.fallingpill and self.gamefield[3][15] != 1 and self.gamefield[4][15] != 1):
         self.fallingpill.append(Pill())        
        elif (self.gamefield[3][15] == 1 or self.gamefield[4][15] == 1):
           print("Game Over")
           quit()
        else:
         self.gamefield[self.x_koordstogamefield(self.fallingpill[0].koords[0])][self.y_koordstogamefield(self.fallingpill[0].koords[1])] = self.gamefield[int((self.fallingpill[0].koords[0]-20)/5)-1][self.y_koordstogamefield(self.fallingpill[0].koords[1])] = 0
         self.fallingpill[0].falling()
      
      #check collision


    def draw(self):
       stddraw.show(200)

    def x_koordstogamefield(self, x):
       return int((x-25)/5)-1
    
    def y_koordstogamefield(self, y):
       return int(y/5)-1
#Abfragen und dann beantworten
#Difficulty 0-20, Speed 1-3, Spieleranzahl 1-2
DrMario(sys.argv[1], sys.argv[2], sys.argv[3])