import time
import pygame
import spriteClasses

class theLevels():
    def __init__(self, background, terrain, forground, screen):
        self.background_group=background
        self.sprite_group_Terrain=terrain
        self.backgroundProp_group=forground
        self.screen = screen

  
    def runLevel1(self):
        #GROUND LEVEL
        player = spriteClasses.Player()  
        startingGame=True

        self.background_group.update(0,0, startingGame)
        self.sprite_group_Terrain.update(0,0, startingGame)
        self.backgroundProp_group.update(0,0, startingGame)
        # player_group.update(startingGame)
        print(self.sprite_group_Terrain)


        # background_group.add(bg)
        #Game loop
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if player.isFalling == False:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            start=time.time()     
                if player.isFalling == False:        
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            end=time.time()
                            if(end-start >1):
                                player.jump(1, player.facingRight) 
                            else:
                                player.jump(end-start,player.facingRight)
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and player.getPlayerY() <= 800:
            
                self.sprite_group_Terrain.update(0,1)
                self.backgroundProp_group.update(0,1)
                player.movePlayerScroller(1)

            if key[pygame.K_s] and player.getPlayerY() >= 100:
            
                self.sprite_group_Terrain.update(0,-1)
                self.backgroundProp_group.update(0,-1)
                player.movePlayerScroller(-1)
            
            player.move(self.sprite_group_Terrain)

            self.screen.fill('black')
            self.background_group.draw(self.screen)
            self.sprite_group_Terrain.draw(self.screen)
            self.backgroundProp_group.draw(self.screen)
            self.screen.blit(player.image,player.rect)
            
            pygame.display.update()
    def runLevel2(self):
        #SEWERS LEVEL
        player = spriteClasses.Player()  
        startingGame=True

        self.background_group.update(0,0, startingGame)
        self.sprite_group_Terrain.update(0,0, startingGame)
        self.backgroundProp_group.update(0,0, startingGame)
        # player_group.update(startingGame)
        print(self.sprite_group_Terrain)


        # background_group.add(bg)
        #Game loop
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if player.isFalling == False:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            start=time.time()     
                if player.isFalling == False:        
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            end=time.time()
                            if(end-start >1):
                                player.jump(1, player.facingRight) 
                            else:
                                player.jump(end-start,player.facingRight)
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and player.getPlayerY() <= 800:
            
                self.sprite_group_Terrain.update(0,1)
                self.backgroundProp_group.update(0,1)
                player.movePlayerScroller(1)

            if key[pygame.K_s] and player.getPlayerY() >= 100:
            
                self.sprite_group_Terrain.update(0,-1)
                self.backgroundProp_group.update(0,-1)
                player.movePlayerScroller(-1)
            
            player.move(self.sprite_group_Terrain)

            self.screen.fill('black')
            self.background_group.draw(self.screen)
            self.sprite_group_Terrain.draw(self.screen)
            self.backgroundProp_group.draw(self.screen)
            self.screen.blit(player.image,player.rect)
            
            pygame.display.update()
    def runLevel3(self):
        #CASTLE LEVEL
        player = spriteClasses.Player()  
        startingGame=True

        self.background_group.update(0,0, startingGame)
        self.sprite_group_Terrain.update(0,0, startingGame)
        self.backgroundProp_group.update(0,0, startingGame)
        # player_group.update(startingGame)
        print(self.sprite_group_Terrain)


        # background_group.add(bg)
        #Game loop
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if player.isFalling == False:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            start=time.time()     
                if player.isFalling == False:        
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            end=time.time()
                            if(end-start >1):
                                player.jump(1, player.facingRight) 
                            else:
                                player.jump(end-start,player.facingRight)
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and player.getPlayerY() <= 800:
            
                self.sprite_group_Terrain.update(0,1)
                self.backgroundProp_group.update(0,1)
                player.movePlayerScroller(1)

            if key[pygame.K_s] and player.getPlayerY() >= 100:
            
                self.sprite_group_Terrain.update(0,-1)
                self.backgroundProp_group.update(0,-1)
                player.movePlayerScroller(-1)
            
            player.move(self.sprite_group_Terrain)

            self.screen.fill('black')
            self.background_group.draw(self.screen)
            self.sprite_group_Terrain.draw(self.screen)
            self.backgroundProp_group.draw(self.screen)
            self.screen.blit(player.image,player.rect)
            
            pygame.display.update()