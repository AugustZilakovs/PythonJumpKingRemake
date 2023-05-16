import pygame


class Player(pygame.sprite.Sprite):
    #pos refers to where the player is positioned in the level. When the level loads should also load in the player position
    
    def __init__(self, characterImage):
        match characterImage:
            case 'option1':
                self.image = pygame.image.load("KingAnimations/kingIdle.png")
                self.idleImage = pygame.image.load("KingAnimations/kingIdle.png")
                self.jumpImage = pygame.image.load("KingAnimations/kingJumpStart.png")
            case 'option2':
                self.image = pygame.image.load("KingAnimations/king2Idle.png")
                self.idleImage = pygame.image.load("KingAnimations/king2Idle.png")
                self.jumpImage = pygame.image.load("KingAnimations/kingJumpStart.png")
            case 'option3':
                self.image = pygame.image.load("testCharacter.png")
                self.idleImage = pygame.image.load("testCharacter.png")
                self.jumpImage = pygame.image.load("testCharacter.png")

        print("in character select") 
        super().__init__()
        self.rect = self.image.get_rect()

        self.rect.center = (500,300)
        #Using vector's to get the direction of movement, math.Vector2(x,y) 
        self.direction = pygame.math.Vector2(0,0) #Vector2 is a list that contains an x and y value
        self.speed = 2
        self.vel_y=0
        self.gravitys=0.05
        self.jumpSpeed = -2
        self.width=32
        self.height=32
        self.vel_x=0
        self.facingRight = True
        self.isFalling = False 
        self.ignoreCollsion = False 
        self.numberOfJumps = 0  
        self.finished = False
    
    def move(self, terrain, finish):
        dx=0
        dy=0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.facingRight=True
        if keys[pygame.K_LEFT]:
            self.facingRight=False
        self.vel_y += self.gravitys
        dy +=self.vel_y
        
        if self.facingRight ==False:
            self.image = pygame.transform.flip(self.idleImage, True, False)
        else:
            self.image = self.idleImage
    

        for platform in finish:
            if platform.rect.colliderect(self.rect):
                self.finished=True

        for platform in terrain:
            if platform.rect.colliderect(self.rect):
                if self.rect.bottom> platform.rect.top:
                    dy=0
                    if(self.isFalling):
                        if self.rect.right>= platform.rect.left and self.rect.bottom > platform.rect.top:
                            print("in collision x")
                            self.rect.centerx = self.rect.centerx+16
                            dx=1
                        if self.rect.left <= platform.rect.right and self.rect.bottom > platform.rect.top:
                            self.rect.centerx = self.rect.centerx - 16
                            dx=-1
                    else:
                        if self.rect.right>= platform.rect.left and self.rect.bottom > platform.rect.bottom:
                            print("in collision x")
                            self.rect.centerx = self.rect.centerx+16
                            dy=1
                            dx=1
                        if self.rect.left <= platform.rect.right and self.rect.bottom > platform.rect.bottom:
                            self.rect.centerx = self.rect.centerx - 16
                            dy=1
                            dx=-1
                                      
                if self.rect.top >= platform.rect.top:
                    dy=1

        if dy!=0:
            self.isFalling = True
        else:
            self.isFalling = False
            self.image =self.idleImage
            self.vel_x = 0
        if self.rect.left +dx <20:
            dx = 2
        if self.rect.right + dx > 920:
            dx = -2

        
        self.rect.x +=dx+self.vel_x
        self.rect.y +=dy

    def jump(self, t, facing):
        if facing:
            self.vel_y = t*-5
            self.vel_x =2
        else:
            self.vel_y = t*-5
            self.vel_x =-1.8
        print("Scale is: ",t)
        
        
    def getPlayerY(self):
        return self.rect.y
    def movePlayerScroller(self, y):
        self.rect = self.rect.move(0,y*2) 
        

