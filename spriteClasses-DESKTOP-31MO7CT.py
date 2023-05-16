import pygame as py


class Player(py.sprite.Sprite):
    #pos refers to where the player is positioned in the level. When the level loads should also load in the player position
    def __init__(self):
        print("in character select") 
        super().__init__()
        self.image = py.image.load("testCharacter.png")
        self.rect = self.image.get_rect()
        self.rect.center = (500,200)
        #movement
        #Using vector's to get the direction of movement, math.Vector2(x,y) 
        self.direction = py.math.Vector2(0,0) #Vector2 is a list that contains an x and y value
        self.speed = 2
        self.vel_y=0
        self.gravitys=0.05
        self.jumpSpeed = -2
        self.width=32
        self.height=32
        self.vel_x=0
        self.facingRight = True
        self.isFalling = False    
    
    def move(self, terrain):
        dx=0
        dy=0
        keys = py.key.get_pressed()
        if keys[py.K_RIGHT]:
            self.facingRight=True

        if keys[py.K_LEFT]:
            self.facingRight=False
        self.vel_y += self.gravitys
        dy +=self.vel_y
        dx +=self.vel_x

        if self.rect.left +dx <0:
            dx = -self.rect.left
        if self.rect.right + dx > 900:
            dx = 900-self.rect.right

        for platform in terrain:
            if platform.rect.colliderect(self.rect.x+dx,self.rect.y+dy,self.width,self.height):
                if self.rect.bottom >= platform.rect.top+10:
                    dy=0
                if self.rect.top >= platform.rect.bottom:
                    dy=1
                if self.rect.left <= platform.rect.centerx:
                    dx=0
                if self.rect.right >= platform.rect.centerx:
                    dx=0

        if dy!=0:
            self.isFalling = True
        else:
            self.isFalling = False
            self.vel_x =0
        self.rect.x +=dx
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

        


