import pygame
pygame.init()
win = pygame.display.set_mode((500,500))

class circle:
    def __init__(self, x, y, rad, col):
        self.x = x
        self.y = y
        self.rad = rad
        self.col = col

    def draw(self, win):
        pygame.draw.circle(win, self.col, (self.x, self.y), self.rad)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 1
        elif keys[pygame.K_d]:
            self.x += 1
        elif keys[pygame.K_w]:
            self.y -= 1
        elif keys[pygame.K_s]:
            self.y += 1
            #if self.x > 250:
               #self.x -= 1
            #elif self.x < 250:
                #self.x += 1
            #if self.y > 250:
                #self.y -= 1
            #elif self.y < 250:
                #self.y += 1


my_circle = circle(250, 250, 30, (0, 0, 250))
circle1 = circle(230, 250,40,(0,255,0))
circle2 = circle(270, 250,40,(0,255,0))
circle3 = circle(250, 240,40,(0,200,255))
circle4 = circle(230, 235,10,(0,0,255))
circle5 = circle(270, 235,10,(0,0,255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255, 150, 0))
    my_circle.draw(win)
    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)
    circle4.draw(win)
    circle5.draw(win)
    circle5.move_by_keys()
    circle4.move_by_keys()
    my_circle.move_by_keys()
    circle1.move_by_keys()
    circle2.move_by_keys()
    circle3.move_by_keys()
    pygame.time.delay(2)
    pygame.display.update()