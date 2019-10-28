import random
from pygame_functions import *

screenSize(1200, 600)
setAutoUpdate(False)
setBackgroundImage("cottage.jpg")

class Snowflake():
    def __init__(self, x, distance):
        self.x = x
        self.y = 0
        self.distance = distance
        self.size = distance / 100 * 10
        self.yspeed = 1 + distance / 100 * 10

    def draw(self):
        drawEllipse(self.x, self.y, self.size, self.size, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))

    def move(self):
        self.y += self.yspeed
        self.x += (mouseX() - 450) / 450 * 5

flakes = []

while True:
    for x in range(1000):
        flakes.append(Snowflake(random.randint(-500,1700), random.randint(1,100)))

    clearShapes()

    for flake in flakes:
        flake.move()
        if flake.y > 900:
            flakes.remove(flake)
        else:
            flake.draw()

    updateDisplay()
    tick(30)

endWait()