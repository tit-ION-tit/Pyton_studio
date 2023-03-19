print("Привет мир")
import tkinter
import random
from tkinter import PhotoImage


def prepare_and_start():
    global player


    canvas.delete("all")
    player_pos = (random.randint(1, N_X - 1) * step, random.randint(1, N_Y - 1) * step)
    player = canvas.create_image((player_pos[0],player_pos[1]),image = player_pic, anchor="nw")
    label.config(text='Сбеги нафиг!')
    master.bind("<KeyPress>", key_pressed)


def move_warp(obj, move_x, move_y):
    xy = canvas.coords(obj)
    canvas.move(obj, move_x, move_y)
    print(xy)
    if xy [0] <= 0 :
        canvas.move(obj, WIDTH, 0)
    if xy [1] >= WIDTH:
        canvas.move(obj, -WIDTH, 0)
    if xy [1] <= 0:
        canvas.move(obj, HEIGHT, 0)
    if xy [1] >= HEIGHT:
        canvas.move(obj, -HEIGHT, 0)


def key_pressed(event):
    if event.keysym == "Up":
        move_warp(player, 0, -step)
    elif event.keysym == "Down":
         move_warp(player, 0, step)
    elif event.keysym == "Right":
         move_warp(player, step, 0)
    elif event.keysym == "Left":
         move_warp(player, -step, 0)


master = tkinter.Tk()
step = 32
N_X = 20
N_Y = 20
WIDTH = step * N_X
HEIGHT = step * N_Y
a = False
player_pic = PhotoImage(file = "image/Ion.png")

canvas = tkinter.Canvas(master, bg = '#40E0D0', width=WIDTH, height=HEIGHT)

player_pos = (random.randint(0, N_X - 1) * step, random.randint(0, N_Y - 1) * step)
print(player_pos)
label = tkinter.Label(master, text='Начать заного')
restart = tkinter.Button(master, text="Начать Заного", command=prepare_and_start)
restart.pack()
canvas.pack()
prepare_and_start()
master.bind("<KeyPress>", key_pressed)
master.mainloop()