import sys
import stddraw
import random
from gameobjects import Virus, Pill, ColoredField
import pygame.key
from utils import *
from pygame import mixer

class DrMario:
    def __init__(self, difficulty, speed, player):
        stddraw.setCanvasSize(900,900)
        stddraw.setXscale(0,100)
        stddraw.setYscale(0,100)
        self.difficulty = int(difficulty)*4+4
        self.speed = int(speed)*100+100
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
        stddraw.filledRectangle(75, 10, 20, 20)
        stddraw.setPenColor(stddraw.CYAN)
        stddraw.rectangle(29,4,42,82)
        stddraw.line(45,86,45,95)
        stddraw.line(55,86,55,95)
        stddraw.line(45,95,55,95)
        
        stddraw.setFontFamily("Courier")
        stddraw.setFontSize(30)
        stddraw.text(85, 15, "Speed " + str(speed))
        stddraw.text(85, 20, "Level " + str(difficulty))
        stddraw.text(85, 25, "Player " + str(player))

        self.color_1 = getrandomColor()
        self.color_2 = getrandomColor()
        self.fallingpill = []
        self.fallingpill.append(Pill(self.color_1, self.color_2))
        self.color_1 = getrandomColor()
        self.color_2 = getrandomColor()
        self.coloredField = []
        self.virus = []
        self.gamefield = [[0 for j in range(16)] for i in range(8)]
        #init virus
        r = 0
        x = y = 1
        while r < self.difficulty:
            
            x = random.randint(0, 7)
            y = random.randint(0, 12)

            while (self.gamefield[x][y] > 0):
              x = random.randint(0,7)
              y = random.randint(0,12) 

            self.virus.append(Virus(x,y))
            #ToDo Wahrscheinlich Virus Liste, wenn entfernt Viren löschen, wenn Liste leer -> Spiel gewonnen
            self.gamefield[x][y] = self.virus[-1].getColor()
            
            r += 1
        stddraw.show(10)

        #Hintergrundmusik initialisieren
        mixer.init()
        mixer.music.load('assets/background.mp3')
        mixer.music.play()

        self.main_loop()


    def main_loop(self):
      while True:
       self.input()
       self.logic()
       self.draw()

    def input(self):
       is_key_pressed = pygame.key.get_pressed()
       if is_key_pressed[pygame.K_a]:
          #Wenn nicht außerhalb des Spielfeldes (kleinergleich -1) und das Feld noch nicht belegt ist, wo die Pille hin will
          if (self.fallingpill[0].rect1[0]-1 > -1 and self.fallingpill[0].rect2[0]-1 > -1 and self.gamefield[self.fallingpill[0].rect1[0]-1][self.fallingpill[0].rect1[1]] == 0 and self.gamefield[self.fallingpill[0].rect2[0]-1][self.fallingpill[0].rect2[1]] == 0):
           self.fallingpill[0].move(-1)
       if is_key_pressed[pygame.K_d]:
          #Wenn nicht außerhalb des Spielfeldes (größergleich 8) und das Feld noch nicht belegt ist, wo die Pille hin will
          if (self.fallingpill[0].rect1[0]+1 < 8 and self.fallingpill[0].rect2[0]+1 < 8 and self.gamefield[self.fallingpill[0].rect1[0]+1][self.fallingpill[0].rect1[1]] == 0 and self.gamefield[self.fallingpill[0].rect2[0]+1][self.fallingpill[0].rect2[1]] == 0):
           self.fallingpill[0].move(1)
       if is_key_pressed[pygame.K_SPACE]:
          #Wenn es durch das rotieren nicht außerhalb des Spielfelds ist, rotiere
          if((self.fallingpill[0].rotation == 3 and self.fallingpill[0].rect2[0] > 0) or (self.fallingpill[0].rotation == 1 and self.fallingpill[0].rect2[0] < 7) or self.fallingpill[0].rotation == 2 or self.fallingpill[0].rotation == 0):
           self.fallingpill[0].rotate()
       

    def logic(self):
        #Logik für aktuelle Pille 1. Kollisionscheck: Wenn die Pille landet mache sie zu zwei farbigen Feldern
        if (self.gamefield[self.fallingpill[0].rect1[0]][(self.fallingpill[0].rect1[1])-1] > 0 or self.gamefield[self.fallingpill[0].rect2[0]][(self.fallingpill[0].rect2[1])-1] > 0 or self.fallingpill[0].koords[1] == 0):
         self.coloredField.append(ColoredField(self.fallingpill[0].rect1[0], self.fallingpill[0].rect1[1], self.fallingpill[0].color1))
         self.coloredField.append(ColoredField(self.fallingpill[0].rect2[0], self.fallingpill[0].rect2[1], self.fallingpill[0].color2))
         self.gamefield[self.coloredField[-1].x][self.coloredField[-1].y] = self.coloredField[-1].getColor()
         self.gamefield[self.coloredField[-2].x][self.coloredField[-2].y] = self.coloredField[-2].getColor()
         self.fallingpill.clear()
        #Wenn somit keine Pille mehr existiert und die Felder, welche für Spielende sorgen nicht belegt sind: Erstelle neue Pille
        if (not self.fallingpill and self.gamefield[3][15] == 0 and self.gamefield[4][15] == 0):
         self.fallingpill.append(Pill(self.color_1, self.color_2))
         self.color_1 = getrandomColor()
         self.color_2 = getrandomColor()
        #Wenn Felder wo neue Pille eigentlich entsteht belegt sind -> beende Spiel
        elif (self.gamefield[3][15] > 0 or self.gamefield[4][15] > 0):
           stddraw.setPenColor(stddraw.RED)
           stddraw.filledRectangle(0,0,100,100)
           stddraw.setPenColor(stddraw.YELLOW)
           #L
           stddraw.filledRectangle(10,40,5,40)
           stddraw.filledRectangle(15,40,10,5)
           #O
           stddraw.filledRectangle(30,45,5,30)
           stddraw.filledRectangle(35,40,10,5)
           stddraw.filledRectangle(35,75,10,5)
           stddraw.filledRectangle(45,45,5,30)
           #S
           stddraw.filledRectangle(60, 75, 15, 5)
           stddraw.filledRectangle(55, 65, 5, 10)
           stddraw.filledRectangle(60, 60, 10, 5)
           stddraw.filledRectangle(70, 45, 5, 15)
           stddraw.filledRectangle(55, 40, 15, 5)
           #E
           stddraw.filledRectangle(80, 40, 5, 40)
           stddraw.filledRectangle(85, 75, 10, 5)
           stddraw.filledRectangle(85, 60, 10, 5)
           stddraw.filledRectangle(85, 40, 10, 5)
           stddraw.text(50, 20, "SCORE")
           stddraw.show()
           while True:
              pass
        #Wenn das nicht der Fall ist, lasse die aktuelle Pille weiter fallen
        else:
         self.fallingpill[0].falling()
      
        #Gefärbte Felder löschen, wenn in sich in Zeilen vier oder mehr Farben aneinander gleichen
        old_value = count = 0
        for i in range(8):
         old_value = self.gamefield[i][0]
         count = 0
         for j in range(16):
            new_value = self.gamefield[i][j]
            if (new_value == old_value and new_value != 0 and j != 0):
               count += 1
            elif (count >= 3):
             stddraw.setPenColor(stddraw.BLACK)
             self.gamefield[i][j-(count+1)] = 0
             stddraw.filledRectangle(gamefield_to_x_koords(i), gamefield_to_y_koords(j-(count+1)), 5,5)
             while (count > 0):
                  self.gamefield[i][j-count] = 0
                  stddraw.filledRectangle(gamefield_to_x_koords(i), gamefield_to_y_koords(j-count), 5,5)                  

                  for field in self.coloredField:
                     if (field.x == i and field.y == j-count):
                        self.coloredField.remove(field)
                  count -= 1

             count = 0
            elif (new_value != old_value):
               count = 0 
            old_value = new_value
        
        #Überprüfung, ob Steine (keine Viren!) fallen. Das passiert wenn kein Stein mehr im Umkreis (mit Liste usw.)
        for field in self.coloredField:
           try:
            if (self.gamefield[field.x+1][field.y] == 0 and self.gamefield[field.x-1][field.y] == 0 and self.gamefield[field.x][field.y-1] == 0):
               while (field.y > 0 and self.gamefield[field.x][field.y-1] == 0):
                  self.gamefield[field.x][field.y] = 0
                  field.falling()
               self.gamefield[field.x][field.y] = field.getColor()
           except IndexError:
              pass
           
      
         #Überprüfung, ob Virus entfernt. Wenn alle entfernt -> gewonnen
        if not self.virus:
           stddraw.setPenColor(stddraw.DARK_GREEN)
           stddraw.filledRectangle(0,0,100,100)
           stddraw.setPenColor(stddraw.YELLOW)
           #W
           stddraw.filledRectangle(40, 55,5,30)
           stddraw.filledRectangle(10, 55,5,30)
           stddraw.filledRectangle(15, 50,5,5)
           stddraw.filledRectangle(35, 50,5,5)
           stddraw.filledRectangle(20, 55,5,5)
           stddraw.filledRectangle(30, 55,5,5)
           stddraw.filledRectangle(25, 55, 5,15)
           #I
           stddraw.filledRectangle(50,50,5,35)
           #N
           stddraw.filledRectangle(60,50,5,35)
           stddraw.filledRectangle(65,70,5,5)
           stddraw.filledRectangle(70, 65,5,5)
           stddraw.filledRectangle(75, 60,5,5)
           stddraw.filledRectangle(80,50,5,35)
           stddraw.text(50, 20, "SCORE")
           stddraw.show()
           while True:
              pass
        for v in self.virus:
           if(self.gamefield[v.x][v.y] == 0):
              self.virus.remove(v)


    def draw(self):
       setColor(self.color_1)
       stddraw.filledRectangle(80, 67.5, 5, 5)
       setColor(self.color_2)
       stddraw.filledRectangle(85, 67.5, 5,5)
       stddraw.show(self.speed)


#Abfragen und dann beantworten
#Difficulty 0-20, Speed 1-3, Spieleranzahl 1-2
DrMario(sys.argv[1], sys.argv[2], sys.argv[3])