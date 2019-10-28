import random
from pygame_functions import *

screenSize(1000, 600)

class Dog():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = makeSprite("dog1.jpg")
        showSprite(self.sprite)
        moveSprite(self.sprite, self.x, self.y)
        self.barksound = makeSound("bark1.wav")

    def bark(self):
        playSoundAndWait(self.barksound)

    def hide(self):
        hideSprite(self.sprite)

    def checkClicks(self):
        if spriteClicked(self.sprite):
            self.bark()
            dogs.append(SmallDog(self.x + random.randint(-100, 100), self.y + random.randint(-100, 100)))
            for i in range(20):
                dogs.append(Dog(random.randint(0, 1000), random.randint(0, 600)))




class SmallDog(Dog):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = makeSprite("dog2.jpg")
        showSprite(self.sprite)
        moveSprite(self.sprite, self.x, self.y)
        self.barksound = makeSound("bark2.wav")


dogs = []
for d in range(5):
    dogs.append(Dog(random.randint(0, 1000), random.randint(0, 600)))
    #dogs[-1].bark()

for d in range(5):
    dogs.append(SmallDog(random.randint(0, 1000), random.randint(0, 600)))
    #dogs[-1].bark()

while True:
    for dog in dogs:
        dog.checkClicks()
    pause(20)

endWait()