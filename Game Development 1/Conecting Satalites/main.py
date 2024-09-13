import pgzrun
import random
from time import time

TITLE = "Space Game"
HEIGHT = 600
WIDTH = 600

#Global Variables
startTime = 0
endTime = 0
totalTime = 0
totalSat = 8
currentSat = 0
satelites = []
lines = []

def createSat():
    global totalSat, satelites, startTime
    for i in range (totalSat):
        satelite = Actor("satelite")
        x = random.randint(50,550)
        y = random.randint(50,550)
        satelite.pos = (x,y)
        satelites.append(satelite)
    startTime=time()
def draw():
    global totalTime, startTime
    screen.blit("background",(0,0))
    number = 1
    for sat in satelites:
        sat.draw()
        screen.draw.text(str(number),(sat.pos[0]+20,sat.pos[1]+20))
        number+=1  
    for line in lines:
        screen.draw.line(line[0],line[1],("white"))
    if currentSat < totalSat:
        # We are displaying the difference when the game has started and the current time
        totalTime = time() - startTime
        screen.draw.text(str(round(totalTime, 2)),(50,50))
def update():
    pass


#On mouse down is a predefined function to check if the mouse has been clicked.
#pos is the argument which stores the x and y positions of the mouse
def on_mouse_down(pos):
    global satelites, currentSat, lines, totalSat
    # Checks is currectSat is smaller then totalSat
    if currentSat < totalSat:
        #If mouse clicks on the currect Satelite
        if satelites[currentSat].collidepoint(pos):
            #To check if currect Satelite exists
            if currentSat:
                lines.append((satelites[currentSat-1].pos,satelites[currentSat].pos))
            currentSat+=1
        else:
            currentSat = 0
            lines = []    
            

createSat()
pgzrun.go()