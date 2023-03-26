    win.fill(color)
    pygame.draw.rect()import pygame
pygame.init()
win = pygame.display.set_mode((1350, 700))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (200, 255, 200)

    pygame.display.update()