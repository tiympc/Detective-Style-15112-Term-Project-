import pygame

#setup for files to call
screen = pygame.display.set_mode((800, 600))
bkg = pygame.image.load('bkg.png')
bkg = pygame.transform.scale(bkg, (800, 600))
gamebkg = pygame.image.load('playbkg.png')
gamebkg = pygame.transform.scale(gamebkg, (800, 600))
instructbkg = pygame.image.load('instructbkg.png')
instructbkg = pygame.transform.scale(instructbkg, (800, 600))
endBanner = pygame.image.load('defeatbkg.png')
endBanner = pygame.transform.scale(endBanner, (800, 600))
victoryBanner = pygame.image.load('victory.png')
victoryBanner = pygame.transform.scale(victoryBanner, (800, 600))
upgradeScreen = pygame.image.load('upgradebkg.png')
upgradeScreen = pygame.transform.scale(upgradeScreen, (800, 600))
pointerImg = pygame.image.load('trash.png')
pointerImg = pygame.transform.scale(pointerImg, (30, 30))
prison = pygame.image.load('prison.png')
prison = pygame.transform.scale(prison, (100, 100))
forceOrbImg = pygame.image.load('forceorb.png').convert_alpha()
forceOrbImg = pygame.transform.scale(forceOrbImg, (30, 30))
hiscorebkg = pygame.image.load('hiscorebkg.png')
hiscorebkg = pygame.transform.scale(hiscorebkg, (800, 600))
loadScreen = pygame.image.load('loadscreen.png')
loadScreen = pygame.transform.scale(loadScreen, (800, 600))
black1 = pygame.image.load('black1.png')
black1 = pygame.transform.scale(black1, (149, 135))
black2 = pygame.image.load('black2.png')
black2 = pygame.transform.scale(black2, (149, 135))
black3 = pygame.image.load('black3.png')
black3 = pygame.transform.scale(black3, (149, 135))
black4 = pygame.image.load('black4.png')
black4 = pygame.transform.scale(black4, (149, 135))
black5 = pygame.image.load('black5.png')
black5 = pygame.transform.scale(black5, (149, 135))
black6 = pygame.image.load('black6.png')
black6 = pygame.transform.scale(black6, (149, 135))
userbkg = pygame.image.load('username.png')
userbkg = pygame.transform.scale(userbkg, (800, 600))
