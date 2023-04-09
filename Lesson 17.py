import pygame
pygame.init()
win = pygame.display.set_mode((500,500))

x = 250
y = 250
w = 2
r = 255
g = 255
b = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= w
    elif keys[pygame.K_RIGHT]:
        x += w
    elif keys[pygame.K_UP]:
        y -= w
    elif keys[pygame.K_DOWN]:
        y += w
    else:
        if x > 250:
            x -= 1
        elif x < 250:
            x += 1
        if y > 250:
            y -= 1
        elif y < 250:
            y += 1
        if y < 100:
            r = 255
            g = 0
            b = 0
        elif y > 400:
            r = 255
            g = 0
            b = 0

        elif x < 100:
            r = 255
            g = 0
            b = 0
        elif x > 400:
            r = 255
            g = 0
            b = 0
        else:
            r = 255
            g = 255
            b = 0

    win.fill((20, 10, 200))

    pygame.draw.circle(win, (0, 0, 85), (250, 250), 45)
    pygame.draw.circle(win, (0, 0, 70), (250, 250), 42)
    pygame.draw.circle(win, (0, 0, 60), (250, 250), 40)
    pygame.draw.circle(win, (0, 0, 40), (250, 250), 38)
    pygame.draw.circle(win, (0, 0, 20), (250, 250), 36)
    pygame.draw.circle(win, (r, g, b), (x, y), 20)
    pygame.draw.circle(win, (0, 0, 0), (250, 250), 34)
    pygame.display.update()
    pygame.time.delay(10)