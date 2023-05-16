import time
import pygame
import spriteClasses
import enemies

class theLevels():
    def __init__(self, background, terrain, forground, screen, characterImage, finishGroup):
        self.background_group=background
        self.sprite_group_Terrain=terrain
        self.backgroundProp_group=forground
        self.finishGroup = finishGroup
        self.screen = screen
        self.characterImage = characterImage
        self.font = pygame.font.Font('CaviarDreams.ttf',26)
        self.numOfJumpsTotal = 0
        self.jumped = False
        self.starting = True

  
    def runLevel1(self):
        #GROUND LEVEL
        player = spriteClasses.Player(self.characterImage)
        #enemy = enemies.bird(self.enemyImage)
        startingGame=True

        self.background_group.update(0,0, startingGame)
        self.sprite_group_Terrain.update(0,0, startingGame)
        self.backgroundProp_group.update(0,0, startingGame)
        self.finishGroup.update(0,0,startingGame)
        # player_group.update(startingGame)
        print(self.sprite_group_Terrain)
    


        # background_group.add(bg)
        #Game loop
        while(True):
            self.jumped = False

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
                            self.jumped=True
                            end=time.time()
                            if(end-start >1):
                                player.rect.centery = player.rect.centery - 16
                                player.jump(1, player.facingRight) 
                            else:
                                player.rect.centery = player.rect.centery - 16
                                player.jump(end-start,player.facingRight)
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and player.getPlayerY() <= 800:
            
                self.sprite_group_Terrain.update(0,1)
                self.backgroundProp_group.update(0,1)
                self.finishGroup.update(0,1)
                player.movePlayerScroller(1)

            if key[pygame.K_s] and player.getPlayerY() >= 100:
            
                self.sprite_group_Terrain.update(0,-1)
                self.backgroundProp_group.update(0,-1)
                self.finishGroup.update(0,-1)
                player.movePlayerScroller(-1)
            
            player.move(self.sprite_group_Terrain, self.finishGroup)

            if player.facingRight == True:
                player.image = player.idleImage
            else:
                player.image = pygame.transform.flip(player.idleImage, True, False)

            if self.jumped == True:
                player.numberOfJumps = player.numberOfJumps +1
            self.numOfJumpsTotal = player.numberOfJumps
            text = self.font.render(str(self.numOfJumpsTotal), True, (0,0,0))

            if player.finished == True:
                fText = self.font.render("Why would the princess be here? SHES IN ANOTHER GAME!", True, (255,255,255))
                self.screen.blit(fText, (player.rect.centerx - 150, player.rect.centery - 64))
                pygame.display.update()
                time.sleep(2)
                break

            self.screen.fill('black')
            self.background_group.draw(self.screen)
            self.sprite_group_Terrain.draw(self.screen)
            self.backgroundProp_group.draw(self.screen)
            self.finishGroup.draw(self.screen)
            self.screen.blit(player.image,player.rect)
            self.screen.blit(text, (800,50))
            if(self.starting and not player.isFalling):
                fText = self.font.render("Woah, that high? Time to get climbing!", True, (255,255,255))
                self.screen.blit(fText, (player.rect.centerx - 150, player.rect.centery - 64))
                pygame.display.update()
                time.sleep(2)
                self.starting = False
            pygame.display.update()

    def runLevel2(self):
        print("SEWERS")
        #SEWERS LEVEL
        player = spriteClasses.Player(self.characterImage)  
        startingGame=True

        self.background_group.update(0,0, startingGame)
        self.sprite_group_Terrain.update(0,0, startingGame)
        self.backgroundProp_group.update(0,0, startingGame)
        self.finishGroup.update(0,0,startingGame)
        # player_group.update(startingGame)
        print(self.sprite_group_Terrain)


        # background_group.add(bg)
        #Game loop
        while(True):
            self.jumped = False
            player.move(self.sprite_group_Terrain, self.finishGroup)

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
                            self.jumped = True
                            if(end-start >1):
                                player.rect.centery = player.rect.centery - 16
                                player.jump(1, player.facingRight) 

                            else:
                                player.rect.centery = player.rect.centery - 16
                                player.jump(end-start,player.facingRight)
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and player.getPlayerY() <= 800:
            
                self.sprite_group_Terrain.update(0,1)
                self.backgroundProp_group.update(0,1)
                self.finishGroup.update(0,1)
                player.movePlayerScroller(1)

            if key[pygame.K_s] and player.getPlayerY() >= 100:
            
                self.sprite_group_Terrain.update(0,-1)
                self.backgroundProp_group.update(0,-1)
                self.finishGroup.update(0,-1)
                player.movePlayerScroller(-1)

            if player.finished == True:
                fText = self.font.render("Why would the princess be in the sewers, I guess ill search else where", True, (255,255,255))
                self.screen.blit(fText, (player.rect.centerx - 150, player.rect.centery - 64))
                pygame.display.update()
                time.sleep(2)
                break

            if player.facingRight == True:
                player.image = player.idleImage
            else:
                player.image = pygame.transform.flip(player.idleImage, True, False)
            if self.jumped == True:
                player.numberOfJumps = player.numberOfJumps + 1
            self.numOfJumpsTotal = player.numberOfJumps
            text = self.font.render(str(self.numOfJumpsTotal), True, (255,255,255))

            self.screen.fill('black')
            self.background_group.draw(self.screen)
            self.sprite_group_Terrain.draw(self.screen)
            self.backgroundProp_group.draw(self.screen)
            self.finishGroup.draw(self.screen)
            self.screen.blit(player.image,player.rect)
            self.screen.blit(text, (800,50))
            if(self.starting and not player.isFalling):
                fText = self.font.render("Ewww, what a nasty part of the castle!", True, (255,255,255))
                self.screen.blit(fText, (player.rect.centerx - 150, player.rect.centery - 64))
                pygame.display.update()
                time.sleep(2)
                self.starting = False
            pygame.display.update()
    def runLevel3(self):
        #CASTLE LEVEL
        player = spriteClasses.Player(self.characterImage)  
        startingGame=True

        self.background_group.update(0,0, startingGame)
        self.sprite_group_Terrain.update(0,0, startingGame)
        self.backgroundProp_group.update(0,0, startingGame)
        self.finishGroup.update(0,0,startingGame)
        # player_group.update(startingGame)
        print(self.sprite_group_Terrain)


        # background_group.add(bg)
        #Game loop
        while(True):
            self.jumped = False
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
                            self.jumped = True
                            if(end-start >1):
                                player.rect.centery = player.rect.centery - 16
                                player.jump(1, player.facingRight) 
                            else:
                                player.rect.centery = player.rect.centery - 16
                                player.jump(end-start,player.facingRight)
            key = pygame.key.get_pressed()
            if key[pygame.K_w] and player.getPlayerY() <= 800:
            
                self.sprite_group_Terrain.update(0,1)
                self.backgroundProp_group.update(0,1)
                self.finishGroup.update(0,1)
                player.movePlayerScroller(1)

            if key[pygame.K_s] and player.getPlayerY() >= 100:
            
                self.sprite_group_Terrain.update(0,-1)
                self.backgroundProp_group.update(0,-1)
                self.finishGroup.update(0,-1)
                player.movePlayerScroller(-1)
            
            player.move(self.sprite_group_Terrain, self.finishGroup)
            if player.facingRight == True:
                player.image = player.idleImage
            else:
                player.image = pygame.transform.flip(player.idleImage, True, False)
            if self.jumped == True:
                player.numberOfJumps = player.numberOfJumps +1
            self.numOfJumpsTotal = player.numberOfJumps
            text = self.font.render(str(self.numOfJumpsTotal), True, (255,250,255))
          
            if player.finished == True:
                fText = self.font.render("The princess is in another castle, HUH!?", True, (255,255,255))
                self.screen.blit(fText, (player.rect.centerx - 150, player.rect.centery - 64))
                pygame.display.update()
                time.sleep(2)
                break

            self.screen.fill('black')
            self.background_group.draw(self.screen)
            self.sprite_group_Terrain.draw(self.screen)
            self.backgroundProp_group.draw(self.screen)
            self.finishGroup.draw(self.screen)
            self.screen.blit(player.image,player.rect)
            self.screen.blit(text, (800,50))
            if(self.starting and not player.isFalling):
                fText = self.font.render("What a pretty castle! The princess must be just as pretty!", True, (255,255,255))
                self.screen.blit(fText, (player.rect.centerx - 300, player.rect.centery - 64))
                pygame.display.update()
                time.sleep(2)
                self.starting = False
        
            pygame.display.update()