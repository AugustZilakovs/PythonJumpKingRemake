import time
import pygame
import levels
import Buttons as buttons
from pytmx.util_pygame import load_pygame

pygame.init()

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect=self.image.get_rect(topleft=pos)
        self.speed=2
    def update(self, x,y,z=False, ):
        if z:
            self.rect = self.rect.move(0,-4000)
        else:
            self.rect = self.rect.move(x*self.speed,y*self.speed)

background = pygame.image.load('WelcomeBackground.jpg')
background = pygame.transform.scale(background, (1600,900))
bg_rect = background.get_rect()

# characterImage = Welcome.characterImage_choice
characterImage_choice = 'option1'

screen = pygame.display.set_mode((960, 900))

# setting up options menu
optionsMenu = False
character1_image = pygame.image.load("KingAnimations/kingIdle.png")
character1_button = buttons.Button(380, 800, character1_image, 1)

character2_image = pygame.image.load("KingAnimations/king2Idle.png")
character2_button = buttons.Button(480, 800, character2_image, 1)

character3_image = pygame.image.load("testCharacter.png")
character3_button = buttons.Button(580, 800, character3_image, 1)

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

def levelLoader(background, terrain, forground, finish, backgroundGroup, terrainGroup, forgroundGroup,finishGroup):
    for i in background.tiles():
        pos = (i[0]*32, i[1]*32)
        Tile(pos=pos, surf=i[2], groups = backgroundGroup)
    for i in terrain.tiles(): #go through every tile in the layer   
        pos = (i[0]*32, i[1]*32)#calculated position of sprite. Every sprite is 32 bits wide and tall
        Tile(pos=pos, surf=i[2], groups = terrainGroup) #create tile object and place it
    print(terrain)
    for i in forground.tiles():  
        pos = (i[0]*32, i[1]*32)
        Tile(pos=pos, surf=i[2], groups = forgroundGroup)
    for i in finish.tiles():
        pos = (i[0]*32,i[1]*32)
        Tile(pos=pos, surf=i[2], groups=finishGroup)
    return backgroundGroup , terrainGroup, forgroundGroup, finishGroup



def levelSelector(level_num):
    background_group = pygame.sprite.Group() #NO COLLISION FOR THIS SPRITE GROUP
    sprite_group_Terrain = pygame.sprite.Group() #create sprite group for tiles ONLY CREATE COLLISION FOR THIS SPRITE GROUP
    backgroundProp_group = pygame.sprite.Group() #NO COLLISION FOR THIS SPRITE GROUP 
    finishGroup = pygame.sprite.Group() 
    if level_num == "1":
    # match level_num:
        # case "1":
            print("In level 1 load")
            tmx_data = load_pygame("Data//tmx//level1.tmx")
            # tmx_data = load_pygame("Data\\tmx\\level1.tmx")
            backgroundLayer = tmx_data.get_layer_by_name('background')
            terrianlayer = tmx_data.get_layer_by_name('Terrain')#get first ground level. As this is a test map this is the only layer.
            backgroundPropLayer = tmx_data.get_layer_by_name('BackgroundProps')
            finishLayer = tmx_data.get_layer_by_name('finish')
            groups = levelLoader(backgroundLayer,terrianlayer,backgroundPropLayer,finishLayer,background_group,sprite_group_Terrain,backgroundProp_group,finishGroup)
            level = levels.theLevels(groups[0],groups[1],groups[2],screen, characterImage_choice, groups[3])  
            print(characterImage_choice)  
            level.runLevel1() 
    elif level_num == "2":
        # case "2":
            tmx_data = load_pygame("Data//tmx//level2.tmx")
            # tmx_data = load_pygame("Data\\tmx\\level2.tmx")
            backgroundLayer = tmx_data.get_layer_by_name('background')
            terrianlayer = tmx_data.get_layer_by_name('Terrain')#get first ground level. As this is a test map this is the only layer.
            backgroundPropLayer = tmx_data.get_layer_by_name('BackgroundProps')
            finishLayer = tmx_data.get_layer_by_name('finish')
            groups = levelLoader(backgroundLayer,terrianlayer,backgroundPropLayer,finishLayer,background_group,sprite_group_Terrain,backgroundProp_group,finishGroup)
            level = levels.theLevels(groups[0],groups[1],groups[2],screen, characterImage_choice, groups[3])    
            level.runLevel2()
    elif level_num == "3":
        # case "3":
            tmx_data = load_pygame("Data//tmx//level3.tmx")
            # tmx_data = load_pygame("Data\\tmx\\level3.tmx")
            backgroundLayer = tmx_data.get_layer_by_name('background')
            terrianlayer = tmx_data.get_layer_by_name('Terrain')#get first ground level. As this is a test map this is the only layer.
            backgroundPropLayer = tmx_data.get_layer_by_name('BackgroundProps')
            finishLayer = tmx_data.get_layer_by_name('finish')
            groups = levelLoader(backgroundLayer,terrianlayer,backgroundPropLayer,finishLayer,background_group,sprite_group_Terrain,backgroundProp_group,finishGroup)
            level = levels.theLevels(groups[0],groups[1],groups[2],screen, characterImage_choice, groups[3])   
            level.runLevel3()
    else: 
        # case _:
            print("Shouldn't be possible")


running = True
# gameloop
while running:
    if optionsMenu == True:
        if character1_button.draw(screen):
            characterImage_choice = 'option1'
        if character2_button.draw(screen):
            characterImage_choice = 'option2'
        if character3_button.draw(screen):
            characterImage_choice = 'option3'
        text = font.render('Select Character', True, white)
        screen.blit(text, (410, 750))
        if 380 <= mouse[0] <= 444 and 800 <= mouse[1] <= 864:
            pygame.draw.rect(screen,light,[380, 800, 64, 64])
        elif 480 <= mouse[0] <= 544 and 800 <= mouse[1] <= 864:
            pygame.draw.rect(screen,light,[480, 800, 64, 64]) 
        elif 580 <= mouse[0] <= 644 and 800 <= mouse[1] <= 864:
            pygame.draw.rect(screen,light,[580, 800, 64, 64]) 
    else:
        pass

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #rectangle0
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-20-50-50 <= mouse[1] <= height/2+20-50-50:
                action = 2  #options button (select character)
                optionsMenu = True

        #rectangle1
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-20-50 <= mouse[1] <= height/2+20-50:
                action = 4  #stage 1 button
                levelSelector("3") #Should be level 2
    
        #rectangle2
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20:
                action = 4  #stage 2 button
                levelSelector("2")
                
        #rectangle3
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-20+50 <= mouse[1] <= height/2+20+50:
                action = 4  #stage 3 button
                levelSelector("1")

        #rectangle4
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if width/2-70 <= mouse[0] <= width/2+70 and height/2-20+50+50 <= mouse[1] <= height/2+20+50+50:
                pygame.quit()

    pygame.init()
    mouse = pygame.mouse.get_pos()

    # if mouse hovers over button it changes to lighter shade 
    #rectangle0
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-70-50 <= mouse[1] <= height/2-30-50:
        pygame.draw.rect(screen,light,[width/2-70,height/2-70-50,140,40]) 
    else:
        pygame.draw.rect(screen,dark,[width/2-70,height/2-70-50,140,40])
    # superimposing the text onto our button
    text = font.render('Options', True, white)
    screen.blit(text, (width/2 - 45,height/2 - 18 - 50 - 50))

    #rectangle1
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-70 <= mouse[1] <= height/2-30:
        pygame.draw.rect(screen,light,[width/2-70,height/2-70,140,40]) 
    else:
        pygame.draw.rect(screen,dark,[width/2-70,height/2-70,140,40])
    # superimposing the text onto our button
    text = font.render('Stage 1', True, white)
    screen.blit(text, (width/2 - 25,height/2 - 18 - 50))

    #rectangle2
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-20 <= mouse[1] <= height/2+20:
        pygame.draw.rect(screen,light,[width/2-70,height/2-20,140,40]) 
    else:
        pygame.draw.rect(screen,dark,[width/2-70,height/2-20,140,40])
    # superimposing the text onto our button
    text = font.render('Stage 2', True, white)
    screen.blit(text, (width/2 - 45,height/2 - 18))

    #rectangle3
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-20+50 <= mouse[1] <= height/2+20+50:
        pygame.draw.rect(screen,light,[width/2-70,height/2-20+50,140,40]) 
    else:
        pygame.draw.rect(screen,dark,[width/2-70,height/2-20+50,140,40])
    # superimposing the text onto our button
    text = font.render('Stage 3', True, white)
    screen.blit(text, (width/2 - 25,height/2 - 18 + 50))

    #rectangle4
    if width/2-70 <= mouse[0] <= width/2+70 and height/2-20+50+50 <= mouse[1] <= height/2+20+50+50:
        pygame.draw.rect(screen,light,[width/2-70,height/2-20+50+50,140,40]) 
    else:
        pygame.draw.rect(screen,dark,[width/2-70,height/2-20+50+50,140,40])
    # superimposing the text onto our button
    text = font.render('Back', True, white)
    screen.blit(text, (width/2 - 25,height/2 - 18 + 50 + 50))

    pygame.display.flip()
    # render()
    time.sleep(0.05)

pygame.quit()