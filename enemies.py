# import pygame
# import random

# class enemies (pygame.sprite.Sprite):
#     def __init__(self, *groups: Group, randx, randy, images) -> None:
#         super().__init__(*groups)
#         self.startImage = pygame.image.load(images[0])
#         self.rect = images [0]
#         self.randx = randx
#         self.randy = randy
#         self.rect.center = (randx, randy)

#     def update(self):
#         self.rect = self.rect.move(self.speedx, self.speedy)

# class bird(enemies):
#     def __init__(self, *groups: Group, randx, randy, images, levelHeight, screen_rect) -> None:
#         super().__init__(*groups, randx, randy, images)
#         randx = random.randint(0,screen_rect.width)
#         randy = random.randint(0, levelHeight)
#         self.speed = 5
#         self.pointProvided = 100

# class walker(enemies):
#     def __init__(self, *groups: Group, randx, randy, images, levelHeight, screen_rect) -> None:
#         super().__init__(*groups, randx, randy, images)
#         randx= random.randint(0,screen_rect.width)
#         randy= random.randint(0,levelHeight)