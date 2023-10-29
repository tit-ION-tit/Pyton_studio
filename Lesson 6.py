print('Привет мир')

import pygame
import random

pygame.init()

seconds_real = 0
time_real = 0
pygame.font.init()
m2_font = pygame.font.SysFont('Это база', 70)
m1_font = pygame.font.SysFont('Победа', 70)
text = m1_font.render("ТЫ ПОБЕДИЛ", False, (0, 0, 0))

brown = (75, 40, 3)
W, H = 1366, 715
win = pygame.display.set_mode((W, H))
buX = H//4
buY = W//6
FPS = 30
clock = pygame.time.Clock()


pygame.mixer.music.load("Sounds/dd64306330d98d5.mp3")
pygame.mixer.music.play(-1)
castle_hp = 10000
sand = pygame.image.load('pesochek.png')

swords_man = pygame.image.load('Knight/walk/knight walk 2.png').convert_alpha()
dark_knight = pygame.image.load('Knight/walk/knight walk 2.png').convert_alpha()
castle = pygame.image.load('Castle/Stena.png').convert_alpha()
castle = pygame.transform.scale(castle, (1100, 810))

class Swordsman:
    def __init__(self, win, x, y, vel, dam, hp):
        self.win = win
        self.x = x
        self.y = y
        self.vel = vel
        self.dam = 1
        self.hp = hp
        self.act = "walk"
        self.act2 = 'Attack'
        self.animations = {"walk": [], 'attack': [], 'idle': []}
        self.frame_index = 0
        self.animate_speed = 0.30
        self.animations['walk'] = [pygame.image.load('Knight/Walk/knight walk 1.png'),
                                   pygame.image.load('Knight/Walk/knight walk 2.png'),
                                   pygame.image.load('Knight/Walk/knight walk 3.png'),
                                   pygame.image.load('Knight/Walk/knight walk 4.png'),
                                   pygame.image.load('Knight/Walk/knight walk 5.png'),
                                   pygame.image.load('Knight/Walk/knight walk 6.png'),
                                   pygame.image.load('Knight/Walk/knight walk 7.png'),
                                   pygame.image.load('Knight/Walk/knight walk 8.png')]

        self.animations['Attack'] = [pygame.image.load('Knight/Attack/knight attack 1.png'),
                                     pygame.image.load('Knight/Attack/knight attack 2.png'),
                                     pygame.image.load('Knight/Attack/knight attack 3.png'),
                                     pygame.image.load('Knight/Attack/knight attack 4.png'),
                                     pygame.image.load('Knight/Attack/knight attack 5.png'),
                                     pygame.image.load('Knight/Attack/knight attack 6.png')]

        self.animations['idle'] = [pygame.image.load('Knight/Idle/knight idle 1.png'),
                                   pygame.image.load('Knight/Idle/knight idle 2.png'),
                                   pygame.image.load('Knight/Idle/knight idle 3.png'),
                                   pygame.image.load('Knight/Idle/knight idle 4.png'),
                                   pygame.image.load('Knight/Idle/knight idle 5.png')]

        for key in self.animations:
            for i in range(len(self.animations[key])):
                self.animations[key][i] = pygame.transform.scale(self.animations[key][i], (64, 64))

    def spawn(self):
        self.win.blit(self.animations[self.act][int(self.frame_index)], (self.x, self.y))

    def horizontal_movement(self):
        if self.act == "walk":
            if self.x < 1200:
                self.x += self.vel
                if self.x >= 1200:
                    self.act = self.act2
    def animate(self):
        if self.x <= 1999:
            self.frame_index += self.animate_speed
            if self.frame_index >= len(self.animations[self.act]) - 1:
                self.frame_index = 0

    def attack(self):
        global castle_hp
        if self.x >= 1200:
            if castle_hp <= 10000:
                castle_hp -= float(0.1)
                print(castle_hp)


list_swords_man = []

counter_swords_man = 0

class Dark_knight:
    def __init__(self, win, x, y, vel, dam, hp):
        self.win = win
        self.x = x
        self.y = y
        self.vel = vel
        self.dam = dam
        self.hp = hp
        self.act2 = "Attack"
        self.act = "walk"
        self.animations = {"walk": [], 'attack': [], 'idle': []}
        self.frame_index = 0
        self.animate_speed = 0.30
        self.animations['walk'] = [pygame.image.load('Dark knight/walk/Dark walk 1.png'),
                                   pygame.image.load('Dark knight/walk/Dark walk 2.png'),
                                   pygame.image.load('Dark knight/walk/Dark walk 3.png'),
                                   pygame.image.load('Dark knight/walk/Dark walk 4.png'),
                                   pygame.image.load('Dark knight/walk/Dark walk 5.png'),
                                   pygame.image.load('Dark knight/walk/Dark walk 6.png'),
                                   pygame.image.load('Dark knight/walk/Dark walk 7.png'),
                                   pygame.image.load('Dark knight/walk/Dark walk 8.png'),]

        self.animations['Attack'] = [pygame.image.load('Dark knight/Attack/Attack 1.png'),
                                     pygame.image.load('Dark knight/Attack/Attack 2.png'),
                                     pygame.image.load('Dark knight/Attack/Attack 3.png'),
                                     pygame.image.load('Dark knight/Attack/Attack 4.png'),
                                     pygame.image.load('Dark knight/Attack/Attack 5.png'),
                                     pygame.image.load('Dark knight/Attack/Attack 6.png')]

        self.animations['idle'] = [pygame.image.load('Dark knight/Idle/Dark idle 1.png'),
                                   pygame.image.load('Dark knight/Idle/Dark idle 2.png'),
                                   pygame.image.load('Dark knight/Idle/Dark idle 3.png'),
                                   pygame.image.load('Dark knight/Idle/Dark idle 4.png'),
                                   pygame.image.load('Dark knight/Idle/Dark idle 5.png')]

        for key in self.animations:
            for i in range(len(self.animations[key])):
                self.animations[key][i] = pygame.transform.scale(self.animations[key][i], (64, 64))

    def spawn(self):
        self.win.blit(self.animations[self.act][int(self.frame_index)], (self.x, self.y))

    def horizontal_movement(self):
        if self.act == "walk":
            if self.x < 1200:
                self.x += self.vel
                if self.x >= 1200:
                    self.act = self.act2
    def animate(self):
        self.frame_index += self.animate_speed
        if self.frame_index >= len(self.animations[self.act]) - 1:
            self.frame_index = 0

    def attack(self):
        global castle_hp
        if self.x >= 1200:
            if castle_hp <= 10000:
                castle_hp -= float(0.3)
                print(castle_hp)

list_DARK = []

counter_Dark = 0

class Hero:
    def __init__(self, win, x, y, vel, dam, hp):
        self.win = win
        self.x = x
        self.y = y
        self.vel = vel
        self.dam = dam
        self.hp = hp
        self.act2 = 'Attack'
        self.act = "walk"
        self.animations = {"walk": [], 'attack': [], 'idle': []}
        self.frame_index = 0
        self.animate_speed = 0.35
        self.animations['walk'] = [pygame.image.load('Hero/Walk & Run/Walk1.png'),
                                   pygame.image.load('Hero/Walk & Run/Walk2.png'),
                                   pygame.image.load('Hero/Walk & Run/Walk3.png'),
                                   pygame.image.load('Hero/Walk & Run/Walk4.png'),
                                   pygame.image.load('Hero/Walk & Run/Walk5.png'),
                                   pygame.image.load('Hero/Walk & Run/Walk6.png')]

        self.animations['Attack'] = [pygame.image.load('Hero/Attack/Attack 1_1.png'),
                                     pygame.image.load('Hero/Attack/Attack 1_2.png'),
                                     pygame.image.load('Hero/Attack/Attack 1_3.png'),
                                     pygame.image.load('Hero/Attack/Attack 1_4.png'),
                                     pygame.image.load('Hero/Attack/Attack 1_5.png'),
                                     pygame.image.load('Hero/Attack/Attack 1_6.png'),
                                     pygame.image.load('Hero/Attack/Attack 1_7.png'),
                                     pygame.image.load('Hero/Attack/Attack 1_8.png'),
                                     pygame.image.load('Hero/Attack/Attack 1_9.png'),
                                     pygame.image.load('Hero/Attack/Attack 1_10.png'),]

        self.animations['idle'] = [pygame.image.load('Knight/Idle/knight idle 1.png'),
                                   pygame.image.load('Knight/Idle/knight idle 2.png'),
                                   pygame.image.load('Knight/Idle/knight idle 3.png'),
                                   pygame.image.load('Knight/Idle/knight idle 4.png'),
                                   pygame.image.load('Knight/Idle/knight idle 5.png')]

        for key in self.animations:
            for p in range(len(self.animations[key])):
                self.animations[key][p] = pygame.transform.scale(self.animations[key][p], (64, 64))

    def spawn(self):
        self.win.blit(self.animations[self.act][int(self.frame_index)], (self.x, self.y))

    def horizontal_movement(self):
        if self.act == "walk":
            if self.x < 1200:
                self.x += self.vel
                if self.x >= 1200:
                    self.act = self.act2
    def animate(self):
        self.frame_index += self.animate_speed
        if self.frame_index >= len(self.animations[self.act]) - 1:
            self.frame_index = 0

    def attack(self):
        global castle_hp
        if self.x >= 1200:
            if castle_hp <= 10000:
                castle_hp -= float(0.5)
                print(castle_hp)

list_hero = []

counter_hero = 0

start_ticks = pygame.time.get_ticks()  # starter tick

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
    if seconds > 1:
        start_ticks = pygame.time.get_ticks()  # starter tick
        seconds_real += 1
        if seconds_real > 60:
            time_real += 1
            seconds_real = 0


    win.blit(sand, (0, 0))
    sec = m2_font.render(str(time_real) + ":" + str(seconds_real), False, (0, 0, 0))
    win.blit(sec, (1100, 15))



    if castle_hp > 9999:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 700, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 9999 >= castle_hp > 9000:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 693, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 9000 >= castle_hp > 8000:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 630, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 8000 >= castle_hp > 7000:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 560, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 7000 >= castle_hp > 6000:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 490, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 6000 >= castle_hp > 5000:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 420, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 5000 >= castle_hp > 4000:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 350, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 4000 >= castle_hp > 3000:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 280, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 3000 >= castle_hp > 2500:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 210, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 2500 >= castle_hp > 2000:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 175, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 2000 >= castle_hp > 1000:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 140, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 1000 >= castle_hp > 500:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 70, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 500 >= castle_hp > 100:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 35, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif 100 >= castle_hp > 1:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 7, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)

    elif castle_hp <= 0:
        cHP_lineRed = pygame.draw.rect(win, (237, 5, 5), (300, 10, 700, 50))
        cHP_line = pygame.draw.rect(win, (48, 255, 69), (300, 10, 0, 50))
        ramaHp = pygame.draw.rect(win, (0, 0, 0), (300, 10, 700, 50), width=2)
        win.blit(text, (500, 400))

    Castle = pygame.draw.rect(win, (135, 123, 61), (1245,0, 1200, 710))

    win.blit(castle, (1250, -100))

    button1 = pygame.draw.rect(win, (brown), (10, 10, buX-10, buY-10), width=2)
    button2 = pygame.draw.rect(win, (brown), (10, buY + 10, buX - 10, buY - 10), width=2)
    button3 = pygame.draw.rect(win, (brown), (10, 2 * buY + 10, buX - 10, buY - 10), width=2)

    for i in list_swords_man:
        i.spawn()
        i.horizontal_movement()
        i.animate()
        i.attack()
    for t in list_DARK:
        t.spawn()
        t.horizontal_movement()
        t.animate()
        t.attack()
    for p in list_hero:
        p.spawn()
        p.horizontal_movement()
        p.animate()
        p.attack()
    m_x, m_y = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    if pressed[0]:
        if button1.x < m_x and button1.x + buX - 10 > m_x and button1.y < m_y and button1.y + buY - 10 > m_y:
            counter_swords_man += 1
            if counter_swords_man >= 30:
                counter_swords_man = 0
                list_swords_man.append(Swordsman(win, random.randint(50, 150), random.randint(100, 600), 5, 1, 10))

        if button2.x < m_x and button2.x + buX - 10 > m_x and button2.y < m_y and button2.y + buY - 10 > m_y:
            counter_Dark += 1
            if counter_Dark >= 45:
                counter_Dark = 0
                list_DARK.append(Dark_knight(win, random.randint(50, 150), random.randint(100, 600), 5, 5, 20))
        if button3.x < m_x and button3.x + buX - 10 > m_x and button3.y < m_y and button3.y + buY - 10 > m_y:
            counter_hero += 1
            if counter_hero >= 60:
                counter_hero = 0
                list_hero.append(Hero(win, random.randint(50, 150), random.randint(100, 600), 5, 10, 30))
        #print(m_x, m_y)
        if Castle.x < m_x and Castle.x + buX - 10 > m_x and Castle.y < m_y and Castle.y + buY - 10 > m_y:
            print ('Это база')

    pygame.display.update()
    clock.tick(FPS)
