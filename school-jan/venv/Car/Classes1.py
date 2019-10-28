from pygame_functions import *
from random import randint
colours = ["orange"]

class Vehicle():
    def __init__(self):
        self.colour = colours[randint(0,len(colours) - 1)]
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.width = 25
        self.height = 50
        self.speed = 10
        self.sprite = makeSprite(self.colour + ".png")
        showSprite(self.sprite)
        moveSprite(self.sprite, self.x, self.y)

screenSize(1500,750)

V1 = Vehicle()

endWait()