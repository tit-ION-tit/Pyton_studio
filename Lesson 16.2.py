import pygame
pygame.init()
win = pygame.display.set_mode((500,500))


a = 250
b = 0
dir_c = -1

x = 0
y = 200
dir_r = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if dir_c == -1:
        b += 1
    else:
        b -= 1

    if b > 500:
        dir_c = 1
    if b < 0:
        dir_c = -1



    if dir_r == -1:
        x += 1
    else:
        x -= 1

    if x > 500:
        dir_r = 1
    if x < 0:
        dir_r = -1

    win.fill((255, 100, 0))
    pygame.draw.rect(win, (0, 0,0), (x, y, 100, 100,))
    pygame.draw.circle(win, (0,255, 255), (a, b), 50)
    pygame.draw.circle(win, (0, 200, 255), (a, b), 30)
    pygame.display.update()
