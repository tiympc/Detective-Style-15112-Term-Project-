import pygame

# i didn't finishthis part. was supposed to make hiscores but would always draw the same
# score for every user
def readFile(path): #from 15112 lecture notes
    with open(path, "rt") as f:
        return f.read()

# https://stackoverflow.com/questions/50829786/python-record-score-user-and-display-top-10
# all credit goes to 'cosmic_inquiry'
def makeHiscoreList(screen, name, totalGraceDays):
    # Writing high scores to file
    file = open('hiscoresGD.txt','a')
    file.write(name + " " + str(totalGraceDays) + "\n")
    file.close()

    # Reading/Printing the output
    file = open('hiscoresGD.txt').readlines()
    scores_tuples = []
    for line in file:
        name, totalGraceDays = line.split()[0], float(line.split()[1])
        scores_tuples.append((name,totalGraceDays))
    scores_tuples.sort(key=lambda t: t[1], reverse=True)
    titleFont = pygame.font.SysFont("Verdana", 20).\
    render("TOTAL GRACEDAYS COLLECTED", True, (0,0,0))
    screen.blit(titleFont, (200,200))
    starting = 0
    for i, (name, score) in enumerate(scores_tuples[:10]):
        if (name, score) not in file:
            indivFont = pygame.font.SysFont("Verdana", 15).\
            render("{}. Score:{} - Player:{} ".format(i+1, totalGraceDays, name), True, (0,0,0))
            screen.blit(indivFont, (200, 240 + starting))
            starting += 20
