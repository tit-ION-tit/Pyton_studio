import random

import pygame
import pygame as pg

W = 1000
H = 650

class Ion(pg.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)
        self.image = pg.image.load('image/ботинок-старый-21407337.jpg')
        self.image = pg.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W)
        self.rect.y = random.randrange(H)

    def update(self):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) -1)


a_s = pg.sprite.Group()
for i in range(50):
    Ion(a_s)

win = pygame.display.set_mode((W, H))
image = pg.image.load("image/Без названия.jfif")
image = pg.transform.scale(image, (1000, 700))
rect = image.get_rect()
while True:
    for i in  pg.event.get():
        if i.type == pg.QUIT:
            exit()

    a_s.update()
    win.fill((0, 150, 255))
    win.blit(image, (0, 0))
    a_s.draw(win)
    pg.display.update()