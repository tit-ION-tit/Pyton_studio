import pygame
import pygame as pg
import random

GRAY = [70] * 3
BLACK = [0] * 3
color = (255, 255, 255)
W, H = 500, 500

pg.init()
win = pg.display.set_mode((W, H))

while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        color = random.choices(range(256), k=3)

    for i in range(10):
        pg.draw.circle(win, GRAY,
                       (random.randint(0, W), random.randint(0,H)),1)

    pressed = pg.mouse.get_pressed()
    if pressed[0]:
        pos = pg.mouse.get_pos()
        pg.draw.circle(win, color, pos, 5)
    pg.display.update()

    pg.time.delay(20)