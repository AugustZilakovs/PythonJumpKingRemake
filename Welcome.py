import time
import pygame
from subprocess import call

pygame.init()

background = pygame.image.load('WelcomeBackground.jpg')
background = pygame.transform.scale(background, (1600,900))
bg_rect = background.get_rect()

screen = pygame.display.set_mode((960, 900))

width = screen.get_width()
height = screen.get_height()
mouse = pygame.mouse.get_pos()

#colours
light = (170,170,170)
dark = (100,100,100)
white = (255,255,255)

#load font
font = pygame.font.Font('CaviarDreams.ttf',26)
text = font.render('Quit', True, white)

def render():
    screen.blit(background,bg_rect)

    # pygame.draw.rect(screen,dark,[width/2-70,height/2-20,140,40])
    # screen.blit(text, (width/2 - 25,height/2 - 18))
    
    pygame.display.flip()
render()

running = True
# gameloop
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
        #rectangle1
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20:
                call(["python","LevelSelector.py"])
                # action = 1  #play button
                # levelSelector("1")
                
        #rectangle2
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-20+50 <= mouse[1] <= height/2+20+50:
                pygame.quit()

    pygame.init()
    mouse = pygame.mouse.get_pos()

    #rectangle1
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20:
        pygame.draw.rect(screen,light,[width/2-70,height/2-20,140,40]) 
    else:
        pygame.draw.rect(screen,dark,[width/2-70,height/2-20,140,40])
    # superimposing the text onto our button
    text = font.render('Play', True, white)
    screen.blit(text, (width/2 - 25,height/2 - 18))

    #rectangle2
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-20+50 <= mouse[1] <= height/2+20+50:
        pygame.draw.rect(screen,light,[width/2-70,height/2-20+50,140,40]) 
    else:
        pygame.draw.rect(screen,dark,[width/2-70,height/2-20+50,140,40])
    # superimposing the text onto our button
    text = font.render('Quit', True, white)
    screen.blit(text, (width/2 - 25,height/2 - 18 + 50))

    pygame.display.flip()
    # render()
    time.sleep(0.05)

pygame.quit()
