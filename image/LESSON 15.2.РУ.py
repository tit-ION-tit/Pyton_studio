
import pygame

size = input('Напишите два числа через пробел: ')

size = size.split()

W, H, = int(size[0]), int(size[1])

print(W, H)

pygame.init()
win = pygame.display.set_mode((W, H))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (0, 0, 0)
    win.fill(color)
    pygame.draw.line(win, (255,255,255),(0, 0), (W, H), 50)
    pygame.draw.line(win, (0, 255, 255), (W,0), (0, H), 50)
    pygame.display.set_caption("ЭТО КРЕСТ")
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (200, 255, 200)
