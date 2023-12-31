import pygame


def init():
    # Initialize pygame library
    pygame.init()
    """Window Game creation"""
    # Set Control Display as 400x400 pixel
    win = pygame.display.set_mode((400, 400))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans
