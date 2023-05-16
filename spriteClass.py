import pygame

class Sprite():
    def __init__(self, randx, randy, images) -> None:
        self.x = randx
        self.y = randy
        self.images = images #array of images containing each animation frame
        self.index = 0 #index used to iterate through each frame of the animation
        self.image = images[self.index]
        self.rect = self.image.get_rect()

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


class Player(Sprite):
    def __init__(self, x, y, images) -> None:
        super().__init__(x, y, images)