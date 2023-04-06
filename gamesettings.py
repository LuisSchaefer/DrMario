from os import path
from operator import itemgetter
import json

class Highscore:
    
    #lade Datei im JSON Format oder falls nicht vorhanden erstelle diese mit Wert "none", 0
    def __init__(self, file) -> None:
        self.data = file
        self.dir = path.dirname(__file__)
      
        with open (path.join(file), 'r') as f:
            try:
                self.highscore = json.load(f)

            except:
                self.highscore = [
                    ('none', 0)
                ]
    
    #Prüfe, ob der neue Score besser als einer der gespeicherten Highscores ist, wenn ja speichere ihn
    def checkScore (self, name, score):
       if score > self.highscore:
            self.setNewHighScore(name, score)
            return True
       else:
           return False
    
    #Füge einen neuen Highscore der Liste (maximal fünf Einträge) hinzu und schreibe diese in die Datei
    def setNewHighScore(self, name, score):
        self.highscore.append((name, score))
        self.highscore = sorted(self.highscore, key = itemgetter(1), reverse= True)[:1]
        with open(self.data, 'w') as f:
            json.dump(self.highscore, f)

    #Gebe den höchsten Score aller Zeiten aus
    def getHighScore (self):
        return str(self.highscore[0][1])
    def getName(self):
        return str(self.highscore[0][0])
