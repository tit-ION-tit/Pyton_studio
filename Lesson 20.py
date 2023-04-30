import random

import pygame
pygame.init()

W, H = 500, 500
win = pygame.display.set_mode((W, H))
FPS = 30
clock = pygame.time.Clock()

class Circle:
    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col
        self.dir = "right"
        self.vel = 10
        self.win = win

    def draw(self):
        pygame.draw.circle(self.win, self.col, (self.x, self.y), self.rad)

    def horizontal_movement(self):
        if self.dir == "right":
            self.x += self.vel
            if self.x > W:
                self.dir = "left"
        else:
            self.x -= self.vel
            if self.x < 0:
                self.dir = "right"

list_circle = []
for i in range(1000):
    list_circle.append(Circle(i * 10, i * 5, 35, random.choices(range(256), k=3)))
    list_circle.append(Circle(W -i * 10, H - i * 5, 35, random.choices(range(256), k=3)))
    list_circle.append(Circle(H -i * 10, W- i * 5, 35, random.choices(range(256), k=3)))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255, 255, 255))

    for one in list_circle:
        one.draw()
        one.horizontal_movement()

    pygame.display.update()

    clock.tick(FPS)