import pygame
import pygame as pg
import random


FPS = 60
W, H = 500, 500

clock = pg.time.Clock()
pg.init()
win = pg.display.set_mode((W, H))
win.fill((255, 255, 255))
size = 200
flag = 5
object_to_draw = 'circle'

while True:
    for event in pg.event.get():
        if event.type == pygame.QUIT:
            pg.quit()
            exit()


    clock.tick(FPS)
    color = random.choices(range(256), k=3)

    pos = pg.mouse.get_pos()

    if object_to_draw == 'circle':
        pg.draw.circle(win, color, pos, size)
    elif object_to_draw == 'rect':
        pygame.draw.rect(win, color, (pos[0]  - size // 2, pos[1] - size // 2, size, size))

    keys = pg.key.get_pressed()
    if keys[pygame.K_e]:
        object_to_draw = 'rect'
    elif keys[pygame.K_q]:
        object_to_draw = 'circle'

    size += flag
    if size > 200:
        flag = flag * (-1)
    if size < 5:
        flag = flag * (-1)

    pg.display.update()