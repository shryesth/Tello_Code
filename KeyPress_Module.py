import pygame
# module used to create game
# using to detect key press (works in game window only)

def init():             
    pygame.init()   #initalinzing a window
    win = pygame.display.set_mode((400,400)) #window size

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame,'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey('LEFT'):
        print("Left key pressed")
    if getKey('RIGHT'):
        print("Right key pressed")


#when ever we are making a module we need to do this
if __name__ == '__main__':      #if i am running this file as main file, do this
    init()
    while True:
        main()