# main file to run

'''
pygamegame.py
created by Lukas Peraza
 for 15-112 F15 Pygame Optional Lecture, 11/11/15
use this code in your term project if you want
- CITE IT
- you can modify it to your liking
  - BUT STILL CITE IT
- you should remove the print calls from any function you aren't using
- you might want to move the pygame.display.flip() to your redrawAll function,
    in case you don't need to update the entire display every frame (then you
    should use pygame.display.update(Rect) instead)
'''
import csv
import pygame
import pygame.mixer
import time
import random
from setup import *
from styleClass import *
from styleClickedOn import *
from randomPoints import *
from randomStyle import *
from trackvar import *
from dynamicGameDifficultyAI import *


# uses the starter code template from Lukas Peraza

class PygameGame(object):

    def init(self):
        pygame.font.init()
        self.totalGraceDays = 0 # statistic 1
        self.timeTakenList = [] # sum(self.timeTakenList) statistic 2
        self.numTimeTaken = 0
        self.state = "homeScreen"
        self.wave = True
        self.mouseX = 0
        self.mouseY = 0
        self.usern = ""
        self.level = 1
        self.boosts = []
        self.toDrawUserName = []
        self.brainBool = False
        self.bkg = bkg
        self.drawOrb = []
        self.graceDays = 0
        self.health = 100
        self.THENAME = ""
        self.toDraw = dict()
        self.clicked = None
        self.styleList = list()
        self.currDifficulty = 0.1
        self.initialTime = 0
        self.initialDifficulty = self.currDifficulty
        for i in range(int(self.level / 3 * 2) + 4):
            self.styleList.append(Style(randomPoints()[0], randomPoints()[1], self.width, self.height,
            self.currDifficulty))

    def mousePressed(self, x, y):
        self.playAgain = False
        if self.state == "upgrade":
            if 40 < x < 60 and 40 < y < 63:
                while len(self.styleList) < int(self.level / 3 * 2) + 4:
                    self.bkg = loadScreen
                    self.toDraw[loadScreen] = (loadScreen, (0, 0))
                    screen.blit(self.bkg, (0,0))
                    for i in range(int(self.level / 3 * 2) + 4):
                        self.styleList.append(Style(randomPoints()[0], randomPoints()[1], self.width, self.height,
                        self.currDifficulty))
                        for element in self.styleList:
                            element.string = generatesString(self.currDifficulty)[0]
                self.state = "play"
                self.bkg = gamebkg
                self.toDraw[gamebkg] = (gamebkg, (0,0))
                screen.blit(self.bkg, (0,0))
                self.initialTime = time.time()
            pygame.draw.rect(screen, (137,104,205), (120, 185, 250, 158))
            pygame.draw.rect(screen, (171,130,255), (120, 365, 250, 158))
            pygame.draw.rect(screen, (137,121,238), (420, 185, 250, 158))
            pygame.draw.rect(screen, (100, 71, 205), (420, 365, 250, 158))
            if 120 < x < 370 and 185 < y < 343 and self.graceDays >= 20:
                self.graceDays -= 20
                self.boosts.append("slowmotion")
            if 120 < x < 370 and 365 < y < 523 and self.graceDays >= 20:
                self.graceDays -= 20
                self.boosts.append("forceorb")
            if 420 < x < 670 and 185 < y < 343 and self.graceDays >= 40:
                self.graceDays -= 40
                self.boosts.append("tactical")
            if 420 < x < 670 and 365 < y < 523 and self.graceDays >= 20:
                self.graceDays -= 20
                self.boosts.append("brain")
            if 120 < x < 370 and 185 < y < 343 and self.graceDays < 20:
                self.state = "error"
            if 120 < x < 370 and 365 < y < 523 and self.graceDays < 20:
                self.state = "error"
            if 420 < x < 670 and 185 < y < 343 and self.graceDays < 40:
                self.state = "error"
            if 420 < x < 670 and 365 < y < 523 and self.graceDays < 20:
                self.state = "error"
        elif self.state == "error":
            if 359 < x < 431 and 275 < y < 288:
                self.state = "upgrade"
        elif self.state == "endBanner":
            self.bkg = endBanner
            self.toDraw[endBanner] = (self.bkg,(0,0))
            screen.blit(endBanner, (0,0))
            if 25 < x < 155 and 493 < y < 560:
                self.state == "homeScreen"
                self.bkg = bkg
            if  212 < x < 597 and 471 < y < 560:
                main()
        elif self.state == "victory":
            self.bkg = victoryBanner
            self.toDraw[victoryBanner] = (self.bkg,(0,0))
            screen.blit(victoryBanner, (0,0))
            if 25 < x < 155 and 493 < y < 560:
                self.state == "homeScreen"
                self.bkg = bkg
            if  212 < x < 597 and 471 < y < 560:
                main()
        elif self.state == "homeScreen":
            if 260 < x < 530 and 320 < y < 460:
                self.state = "username"
                self.THENAME = self.toDrawUserName
                self.bkg = userbkg
            if 209 < x < 581 and 489 < y < 551:
                self.state = "instructions"
                self.bkg = instructbkg
        elif self.state == "username":
            if 25 < x < 155 and 493 < y < 560:
                self.state = "homeScreen"
            if 521 < x < 775 and 490 < y < 564:
                self.initialTime = time.time()
                self.bkg = gamebkg
                self.state = "play"
        elif self.state == "instructions":
            if 30 < x < 154 and 495 < y < 558:
                self.state = "homeScreen"
                self.bkg = bkg

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        self.mouseX = x
        self.mouseY = y


    # wrote this during hack112
    def mouseDrag(self, x, y):
        if self.clicked == None:
            self.clicked = styleClickedOn(None, None, self.styleList, self.dragOption)
            if self.clicked == None:
                return  # no string clicked on
        self.toDraw[self.clicked] = (self.clicked.string, (x, y))

    def keyPressed(self, keyCode, modifier, screen):
        if self.state == "play" and keyCode == pygame.K_s and "slowmotion" in self.boosts:
            self.boosts.remove("slowmotion")
            for specific in self.styleList:
                specific.speed = specific.speed / 2
        if self.state == "play" and keyCode == pygame.K_f and "forceorb" in self.boosts:
            self.boosts.remove("forceorb")
            self.drawOrb.append((self.mouseX, self.mouseY))
        if self.state == "play" and keyCode == pygame.K_t and "tactical" in self.boosts:
            self.boosts.remove("tactical")
            self.styleList = []
            self.level += 1
            if self.level == 20:
                self.state = "victory"
                self.bkg = victoryBanner
                self.toDraw[victoryBanner] = (victoryBanner,(0,0))
                screen.blit(self.bkg, (0,0))
            else:
                self.state = "upgrade"
        if self.state == "play" and keyCode == pygame.K_b and "brain" in self.boosts:
            self.brainBool = True
            self.boosts.remove("brain")
        elif self.state == "username":
            for key in self._keys.copy():
                if key != 8 or key != 32 or key not in range(97,123):
                    self._keys.remove(key)
                if 97 <= key <= 122:
                    self.usern = self.usern + chr(key)
                if key == 8:
                    self.usern = ""
                if key == 32:
                    self.usern += " "
            self.toDrawUserName = self.usern[-self.numTimes::]
            track = self.usern[-self.numTimes::]
            keepTrackOfMe1(track)

# event.type == pygame.KEYDOWN:
#     self._keys[event.key] = True
#     self.keyPressed(event.key, event.mod, screen)

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def redrawAll(self, screen):
        grayColor = (50, 50, 50)
        screen.fill(grayColor)
        screen.blit(self.bkg, (0, 0))
        if not pygame.font.get_init():
            pygame.font.init()
        if self.state == "homeScreen":
            termProjectFontLineOne = pygame.font.SysFont("Helvetica", 20).\
            render("Alex Sahinidis", True, (0, 0, 0))
            termProjectFontLineTwo = pygame.font.SysFont("Helvetica", 20).\
            render("Fall 2018", True, (0, 0, 0))
            termProjectFontLineThree = pygame.font.SysFont("Helvetica", 20).\
            render("15-112 Term Project", True, (0, 0, 0))
            screen.blit(termProjectFontLineOne, (600, 490))
            screen.blit(termProjectFontLineTwo, (600, 515))
            screen.blit(termProjectFontLineThree, (600, 540))
            self.bkg = bkg
            self.toDraw[bkg] = (bkg, (0, 0))

        if self.state == "play":
            if self.level > 20:
                self.state = "victory"
                self.bkg = victoryBanner
            if len(self.timeTakenList) > 1:
                self.currDifficulty = dynamicDifficulty(sum(self.timeTakenList) / (len(self.timeTakenList) - 1), self.level,
                len(self.boosts), whatAmI2(), self.initialDifficulty)
            currLevel = pygame.font.SysFont("Helvetica", 25).\
            render("Wave " + str(self.level) + " / 20", True, (0, 50, 0))
            screen.blit(currLevel, (330, 50))
            slowFont = pygame.font.SysFont("Helvetica", 20).\
            render('Slow Motions ("s") Left: ' + str(self.boosts.count("slowmotion")), True, (0, 40, 0))
            forceFont = pygame.font.SysFont("Helvetica", 20).\
            render('Force Orbs ("f") Left: ' + str(self.boosts.count("forceorb")), True, (0, 40, 0))
            tacticalFont = pygame.font.SysFont("Helvetica", 20).\
            render('Tactical Nukes ("t") Left: ' + str(self.boosts.count("tactical")), True, (0, 40, 0))
            brainFont = pygame.font.SysFont("Helvetica", 20).\
            render('Brain Freezes ("b") Left: ' + str(self.boosts.count("brain")), True, (0, 40, 0))
            screen.blit(slowFont, (535, 40))
            screen.blit(forceFont, (556, 62))
            screen.blit(prison, (355, 470))
            screen.blit(tacticalFont, (531, 84))
            screen.blit(brainFont, (530, 106))
            prisonFontLineOne = pygame.font.SysFont("Helvetica", 15).\
            render("Prison", True, (255, 1, 1))
            prisonFontLineTwo = pygame.font.SysFont("Helvetica", 15).\
            render("of", True, (255, 1, 1))
            prisonFontLineThree = pygame.font.SysFont("Helvetica", 15).\
            render("Debugging", True, (255, 1, 1))
            screen.blit(prisonFontLineOne, (384, 485))
            screen.blit(prisonFontLineTwo, (401, 500))
            screen.blit(prisonFontLineThree, (371, 515))
            grayColor = (71, 71, 71)
            for element in self.styleList:
                if self.brainBool == True:
                    t1 = time.time()
                    t2 = time.time()
                    while t2 - t1 < 3:
                        element.moveOutside()
                        t2 = time.time()
                    self.brainBool = False
                else:
                    element.moveTowardsCenter()
                element.draw()
            graceDayText = pygame.font.SysFont("Helvetica", 20).\
            render(str(self.graceDays) + " Grace Days", True, (0, 40, 0))
            screen.blit(graceDayText, (45, 45))
            healthText = pygame.font.SysFont("Helvetica", 30).\
            render(str(self.health), True, (150, 0,0))
            screen.blit(healthText, (self.width / 2 - 15, self.height / 2 - 15))
            if self.wave == True:
                if len(self.styleList) == 0:
                    self.drawOrb = []
                for specific in self.styleList.copy():
                    for orb in self.drawOrb:
                        if orb[0] - 100 < specific.x < orb[0] + 100 and orb[1] - 100 < specific.y < orb[1] + 100:
                            specific.moveTowardsOrb(orb)
                    if (specific.getFirstXCoordinates() - 20) < (self.width / 2) < (specific.getSecondXCoordinates() + 20) and \
                    (specific.getFirstYCoordinates() - 20) < (self.height / 2) < (specific.getFirstYCoordinates() + 20) and specific.goodString == False:
                        self.health -= 5
                        self.styleList.remove(specific)
                        if self.health <= 0:
                            self.bkg = endBanner
                            self.toDraw[endBanner] = (endBanner, (0, 0))
                            grayColor = (50, 50, 50)
                            screen.fill(grayColor)
                            screen.blit(self.bkg, (0, 0))
                            self.state = "endBanner"
                            break
                        if len(self.styleList) == 0:
                            t2 = time.time()
                            self.timeTakenList.append(t2 - self.initialTime)
                            self.drawOrb = []
                            self.level += 1
                            self.state = "upgrade"
                    if (specific.getFirstXCoordinates() - 20) < (self.width / 2) < (specific.getSecondXCoordinates() + 20) and \
                    (specific.getFirstYCoordinates() - 20) < (self.height / 2) < (specific.getFirstYCoordinates() + 20) and specific.goodString == True:
                        self.styleList.remove(specific)
                        if len(self.styleList) == 0:
                            t2 = time.time()
                            self.timeTakenList.append(t2 - self.initialTime)
                            self.level += 1
                            self.drawOrb = []
                            self.state = "upgrade"
                            break
                    xMidpoint = (specific.getFirstXCoordinates() + specific.getSecondXCoordinates()) / 2
                    yMidpoint = specific.getFirstYCoordinates()
                    if 355 < xMidpoint < 470 and 475 < yMidpoint < 570:
                        if specific.goodString == False:
                            self.graceDays += 1
                            self.totalGraceDays += 1
                            v = self.totalGraceDays
                            keepTrackOfMe2(v)
                        if specific.goodString == True:
                            self.health -= 5
                            if self.health <= 0:
                                self.state = "endBanner"
                                self.bkg = endBanner
                                self.toDraw[endBanner] = (endBanner, (0, 0))
                                grayColor = (50, 50, 50)
                                screen.fill(grayColor)
                                screen.blit(self.bkg, (0, 0))
                                self.state = "endBanner"
                        self.styleList.remove(specific)
                        if len(self.styleList) == 0:
                            t2 = time.time()
                            self.timeTakenList.append(t2 - self.initialTime)
                            self.level += 1
                            self.drawOrb = []
                            self.state = "upgrade"
                            break
            for orb in self.drawOrb:
                screen.blit(forceOrbImg, orb)
            if self.level > 20:
                self.state = "victory"
                self.bkg = victoryBanner
        elif self.state == "upgrade":
            self.bkg = upgradeScreen
            self.toDraw[upgradeScreen] = (self.bkg, (0,0))
            screen.blit(upgradeScreen, (0,0))
            xFont = pygame.font.SysFont("Helvetica", 25).\
            render("X", True, (0, 0, 0))
            screen.blit(xFont, (42,38))
            pygame.draw.rect(screen, (0, 0, 0), (40, 40, 20, 23), 1)
            upgradeInstructions = pygame.font.SysFont("Helvetica", 20).\
            render("Press the key that corresponds to the upgrade to use (click to buy).", True, (0,0,0))
            firstUpgradeFontLineOne = pygame.font.SysFont("Verdana", 25).\
            render('Slow Motion ("s")', True, (0,50,0))
            firstUpgradeFontLineTwo = pygame.font.SysFont("Verdana", 22).\
            render("the strings move", True, (0,0,0))
            firstUpgradeFontLineThree = pygame.font.SysFont("Verdana", 22).\
            render("at half their", True, (0,0,0))
            firstUpgradeFontLineFour = pygame.font.SysFont("Verdana", 22).\
            render("normal speed", True, (0,0,0))
            firstUpgradeFontLineFive = pygame.font.SysFont("Verdana", 22).\
            render("Cost: 20 Grace Days", True, (0,0,0))
            graceDaysRem = pygame.font.SysFont("Verdana", 20).\
            render("Grace Days: " + str(self.graceDays), True, (0,40,0))
            forceOrbInstructOne = pygame.font.SysFont("Verdana", 25).\
            render('Force Orb ("f")', True, (0,0,50))
            forceOrbInstructTwo = pygame.font.SysFont("Verdana", 22).\
            render("drop a force orb on", True, (0,0,0))
            forceOrbInstructThree = pygame.font.SysFont("Verdana", 22).\
            render("your cursur's location", True, (0,0,0))
            forceOrbInstructFour = pygame.font.SysFont("Verdana", 22).\
            render("to attract the strings", True, (0,0,0))
            forceOrbInstructFive = pygame.font.SysFont("Verdana", 22).\
            render("Cost: 20 Grace Days", True, (0,0,0))
            nukeInstructOne = pygame.font.SysFont("Verdana", 25).\
            render('Tactical Nuke ("t")', True, (50,0,0))
            nukeInstructTwo = pygame.font.SysFont("Verdana", 22).\
            render("wipes out every", True, (0,0,0))
            nukeInstructThree = pygame.font.SysFont("Verdana", 22).\
            render("string and advances", True, (0,0,0))
            nukeInstructFour = pygame.font.SysFont("Verdana", 22).\
            render("to the next level", True, (0,0,0))
            nukeInstructFive = pygame.font.SysFont("Verdana", 22).\
            render("Cost: 40 Grace Days", True, (0,0,0))
            opposOne = pygame.font.SysFont("Verdana", 25).\
            render('Brain Freeze ("b")', True, (0,0,0))
            opposTwo = pygame.font.SysFont("Verdana", 22).\
            render('Freeze the strings', True, (0,0,0))
            opposThree = pygame.font.SysFont("Verdana", 22).\
            render('in place for 3 seconds', True, (0,0,0))
            opposFour = pygame.font.SysFont("Verdana", 22).\
            render("Cost: 20 Grace Days", True, (0,0,0))
            pygame.draw.rect(screen, (137,104,205), (120, 185, 250, 158))
            pygame.draw.rect(screen, (171,130,255), (120, 365, 250, 158))
            pygame.draw.rect(screen, (137,121,238), (420, 185, 250, 158))
            pygame.draw.rect(screen, (100, 71, 205), (420, 365, 250, 158))
            screen.blit(forceOrbInstructOne, (152, 370))
            screen.blit(forceOrbInstructTwo, (137, 400))
            screen.blit(forceOrbInstructThree, (127, 420))
            screen.blit(forceOrbInstructFour, (130, 440))
            screen.blit(forceOrbInstructFive, (130, 480))
            screen.blit(upgradeInstructions, (105,140))
            screen.blit(firstUpgradeFontLineOne, (136, 190))
            screen.blit(firstUpgradeFontLineTwo, (152, 220))
            screen.blit(firstUpgradeFontLineThree, (175, 240))
            screen.blit(firstUpgradeFontLineFour, (165, 260))
            screen.blit(firstUpgradeFontLineFive, (130, 300))
            screen.blit(nukeInstructOne, (428, 190))
            screen.blit(nukeInstructTwo, (455, 220))
            screen.blit(nukeInstructThree, (433, 240))
            screen.blit(nukeInstructFour, (453, 260))
            screen.blit(nukeInstructFive, (430, 300))
            screen.blit(opposOne, (433, 370))
            screen.blit(opposTwo, (446, 400))
            screen.blit(opposThree, (425, 420))
            screen.blit(opposFour, (430, 480))
            screen.blit(graceDaysRem, (80, 40))
        elif self.state == "instructions":
            self.toDraw[instructbkg] = (self.bkg, (0, 0))
            screen.blit(black1, (174, 195))
            screen.blit(black2, (363, 195))
            screen.blit(black3, (552, 195))
            screen.blit(black4, (174, 410))
            screen.blit(black5, (363, 410))
            screen.blit(black6, (552, 410))
        elif self.state == "username":
            starting = 360
            for key in self.toDrawUserName:
                userFontName = pygame.font.SysFont("monospace", 40).\
                render(key, True, (0,0,0))
                screen.blit(userFontName, (starting, 270))
                starting += 25
        elif self.state == "error":
            self.bkg = upgradeScreen
            self.toDraw[upgradeScreen] = (self.bkg, (0,0))
            screen.blit(upgradeScreen, (0,0))
            xFont = pygame.font.SysFont("Helvetica", 25).\
            render("X", True, (0, 0, 0))
            screen.blit(xFont, (42,38))
            pygame.draw.rect(screen, (0, 0, 0), (40, 40, 20, 23), 1)
            upgradeInstructions = pygame.font.SysFont("Helvetica", 20).\
            render("Press the key that corresponds to the upgrade to use (click to buy).", True, (0,0,0))
            firstUpgradeFontLineOne = pygame.font.SysFont("Verdana", 25).\
            render('Slow Motion ("s")', True, (0,50,0))
            firstUpgradeFontLineTwo = pygame.font.SysFont("Verdana", 22).\
            render("the strings move", True, (0,0,0))
            firstUpgradeFontLineThree = pygame.font.SysFont("Verdana", 22).\
            render("at half their", True, (0,0,0))
            firstUpgradeFontLineFour = pygame.font.SysFont("Verdana", 22).\
            render("normal speed", True, (0,0,0))
            firstUpgradeFontLineFive = pygame.font.SysFont("Verdana", 22).\
            render("Cost: 20 Grace Days", True, (0,0,0))
            graceDaysRem = pygame.font.SysFont("Verdana", 20).\
            render("Grace Days: " + str(self.graceDays), True, (0,40,0))
            forceOrbInstructOne = pygame.font.SysFont("Verdana", 25).\
            render('Force Orb ("f")', True, (0,0,50))
            forceOrbInstructTwo = pygame.font.SysFont("Verdana", 22).\
            render("drop a force orb on", True, (0,0,0))
            forceOrbInstructThree = pygame.font.SysFont("Verdana", 22).\
            render("your cursur's location", True, (0,0,0))
            forceOrbInstructFour = pygame.font.SysFont("Verdana", 22).\
            render("to attract the strings", True, (0,0,0))
            forceOrbInstructFive = pygame.font.SysFont("Verdana", 22).\
            render("Cost: 20 Grace Days", True, (0,0,0))
            nukeInstructOne = pygame.font.SysFont("Verdana", 25).\
            render('Tactical Nuke ("t")', True, (50,0,0))
            nukeInstructTwo = pygame.font.SysFont("Verdana", 22).\
            render("wipes out every", True, (0,0,0))
            nukeInstructThree = pygame.font.SysFont("Verdana", 22).\
            render("string and advances", True, (0,0,0))
            nukeInstructFour = pygame.font.SysFont("Verdana", 22).\
            render("to the next level", True, (0,0,0))
            nukeInstructFive = pygame.font.SysFont("Verdana", 22).\
            render("Cost: 40 Grace Days", True, (0,0,0))
            opposOne = pygame.font.SysFont("Verdana", 25).\
            render('Brain Freeze ("b")', True, (0,0,0))
            opposTwo = pygame.font.SysFont("Verdana", 22).\
            render('Freeze the strings', True, (0,0,0))
            opposThree = pygame.font.SysFont("Verdana", 22).\
            render('in place for 3 seconds', True, (0,0,0))
            opposFour = pygame.font.SysFont("Verdana", 22).\
            render("Cost: 20 Grace Days", True, (0,0,0))
            pygame.draw.rect(screen, (137,104,205), (120, 185, 250, 158))
            pygame.draw.rect(screen, (171,130,255), (120, 365, 250, 158))
            pygame.draw.rect(screen, (137,121,238), (420, 185, 250, 158))
            pygame.draw.rect(screen, (100, 71, 205), (420, 365, 250, 158))
            screen.blit(forceOrbInstructOne, (152, 370))
            screen.blit(forceOrbInstructTwo, (137, 400))
            screen.blit(forceOrbInstructThree, (127, 420))
            screen.blit(forceOrbInstructFour, (130, 440))
            screen.blit(forceOrbInstructFive, (130, 480))
            screen.blit(upgradeInstructions, (105,140))
            screen.blit(firstUpgradeFontLineOne, (136, 190))
            screen.blit(firstUpgradeFontLineTwo, (152, 220))
            screen.blit(firstUpgradeFontLineThree, (175, 240))
            screen.blit(firstUpgradeFontLineFour, (165, 260))
            screen.blit(firstUpgradeFontLineFive, (130, 300))
            screen.blit(nukeInstructOne, (428, 190))
            screen.blit(nukeInstructTwo, (455, 220))
            screen.blit(nukeInstructThree, (433, 240))
            screen.blit(nukeInstructFour, (453, 260))
            screen.blit(nukeInstructFive, (430, 300))
            screen.blit(opposOne, (433, 370))
            screen.blit(opposTwo, (446, 400))
            screen.blit(opposThree, (425, 420))
            screen.blit(opposFour, (430, 480))
            screen.blit(graceDaysRem, (80, 40))
            xFont2 = pygame.font.SysFont("Helvetica", 10).\
            render("close message", True, (100, 0, 0))
            errorLine = pygame.font.SysFont("Helvetica", 25).\
            render("Not enough Grace Days!", True, (100,0,0))
            pygame.draw.rect(screen, (255,255,255), (200, 250, 400, 100), 0)
            screen.blit(xFont2, (360,275))
            pygame.draw.rect(screen, (0,0,0), (359, 275, 72, 13), 1)
            screen.blit(errorLine, (267, 290))
            pygame.draw.rect(screen, (200,0,0), (230, 270, 340, 60), 3)
        elif self.state == "victory":
            congratsText = pygame.font.SysFont("Helvetica", 26).\
            render("Congratulations, " + whatAmI1() + "," + " you deserve this accomplishment.", True, (0,0,0))
            screen.blit(congratsText, (80, 300))
    def isKeyPressed(self, key):
        pass

    def __init__(self, width=800, height=600, fps=120, title="Detective Style", dragOption = False):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        self.dragOption = dragOption
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)
        # stores all the keys currently being held down
        self._keys = list()
        self.numTimes = 0
        # call game-specific initialization
        self.init()
        playing = True
        while playing:
    # why the frick does this not work
            # pointerPoints = pygame.mouse.get_pos()
            # screen.blit(pointerImg, pointerPoints)
            # pygame.mouse.set_visible(False)
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.dragOption = False
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                    event.buttons == (0, 0, 0)):
                    self.dragOption = True
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self.numTimes += 1
                    self._keys.append(event.key)
                    self.keyPressed(event.key, event.mod, screen)
                elif event.type == pygame.KEYUP:
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()
        pygame.quit()

def main():
    pygame.mixer.init()
    song = pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(5)
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()
