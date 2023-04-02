import pygame
pygame.init()
win = pygame.display.set_mode((500,500))

x = 100
y = 50
a = 150
b = 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    x = x + 1

    b = b + 2
    if x > 500:
        x = 0
        y = y + 7

    if b > 500:
        b = 0
        a = a + 10
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255,0), (x, y, 100, 150,))
    pygame.draw.circle(win, (0,255, 255), (a, b), 50)
    pygame.display.update()

    pygame.time.delay(10)