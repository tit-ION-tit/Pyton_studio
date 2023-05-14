import pygame

pygame.init()

FPS = 30
clock = pygame.time.Clock()

win = pygame.display.set_mode((500, 500))

x = 250
y = 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(FPS)
    win.fill((126, 223, 247))
    pygame.draw.rect(win, (200, 100, 62), (0, 400 , 500, 200))

    pygame.draw.circle(win, (255, 200, 0), (x, y), 20)

    if y < 380:
        y = y + 10

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= 5
    elif keys[pygame.K_d]:
        x += 5
    elif keys[pygame.K_SPACE]:
        y -= 20
