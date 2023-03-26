
import pygame

size = input('Напишите два числа через пробел: ')

size = size.split()
n,a = int(size[0]), int(size[1])
rect = n // a
W, H, = int(size[0]), int(size[1])

print(W, H)

pygame.init()
win = pygame.display.set_mode((W, H))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (255, 255, 255)
    win.fill(color)
    for i in range(a):
        for j in range(a):
            if (i + j) % 2 == 0:
                pygame.draw.rect(win,(0,0,0),(i * rect,j* rect,(i+1) * rect, (j+1)* rect))
    pygame.display.set_caption("ЭТО ШАХМАТЫ")
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    color = (200, 255, 200)
