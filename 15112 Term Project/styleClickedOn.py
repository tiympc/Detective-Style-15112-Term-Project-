from styleClass import *

# changes the style's position when clicked on
def styleClickedOn(event, data, list, drag):
    if drag == True:
        for element in list:
            if element.getFirstXCoordinates() < pygame.mouse.get_pos()[0] < \
            element.getSecondXCoordinates() and element.getFirstYCoordinates() - 6.5\
            < pygame.mouse.get_pos()[1] < element.getFirstYCoordinates() + 19.5:
                element.x = pygame.mouse.get_pos()[0] - (13 * len(element.string) / 3.5)
                element.y = pygame.mouse.get_pos()[1] - 6.5
    else:
        for element in list:
            initialSpeed = element.speed
            if element.getFirstXCoordinates() < pygame.mouse.get_pos()[0] < \
            element.getSecondXCoordinates() and element.getFirstYCoordinates() - 6.5\
            < pygame.mouse.get_pos()[1] < element.getSecondYCoordinates() + 19.5:
                element.speed = 0
                element.x = pygame.mouse.get_pos()[0] - (13 * len(element.string) / 3.5)
                element.y = pygame.mouse.get_pos()[1] - 6.5
            element.speed = initialSpeed
