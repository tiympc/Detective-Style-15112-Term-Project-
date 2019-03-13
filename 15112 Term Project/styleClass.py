import random
from setup import *
from randomStyle import *

# the main class for the individual style
class Style(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, currDifficulty):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 0.2
        strAndGood = generatesString(currDifficulty)
        self.string = strAndGood[0]
        self.goodString = strAndGood[1]

    def draw(self):
        screen.blit(pygame.font.SysFont("monospace", 13).render(self.string, True, (0, 0, 0)),
        (self.x, self.y))
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 2, self.y, 3 + 12 * len(self.string) * (2/3), 13), 2)

    def moveOutside(self):
        if self.x < self.width / 2 - 13:
            self.x -= self.speed
        if self.x > self.width / 2 - 13:
            self.x += self.speed
        if self.y < self.height / 2 - 13:
            self.y -= self.speed
        if self.y > self.height / 2 - 13:
            self.y += self.speed
    def moveTowardsCenter(self):
        distanceX = abs(self.x - 400)
        distanceY = abs(self.y - 300)
        if self.x < self.width / 2 - 13:
            self.x += self.speed * (distanceX + 1) / 50
        if self.x > self.width / 2 - 13:
            self.x -= self.speed * (distanceX + 1) / 50
        if self.y < self.height / 2 - 13:
            self.y += self.speed * (distanceY + 1) / 50
        if self.y > self.height / 2 - 13:
            self.y -= self.speed * (distanceY + 1) / 50

    def moveTowardsOrb(self, orb):
        distanceX = abs(self.x - 400)
        distanceY = abs(self.y - 300)
        if self.x < orb[0] - 13:
            self.x += self.speed * (distanceX + 1) / 50
        if self.x > orb[0] - 13:
            self.x -= self.speed * (distanceX + 1) / 50
        if self.y < orb[1] - 13:
            self.y += self.speed * (distanceY + 1) / 50
        if self.y > orb[1] - 13:
            self.y -= self.speed * (distanceY + 1) / 50

    def getFirstXCoordinates(self):
        return self.x

    def getSecondXCoordinates(self):
        return self.x + 3 + 12 * len(self.string) * (2/3)

    def getFirstYCoordinates(self):
        return self.y

    def getSecondYCoordinates(self):
        return self.y + 3 + 12 * len(self.string) * (2/3)
