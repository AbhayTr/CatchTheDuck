'''

Catch the Duck Hand Game

An AI Based Game in which the player can move the in-game hand by moving their actual hand in front of a camera, and then close their hand in front of the camera when their in-game hand is above the duck, to catch the duck and score a point.

© Abhay Tripathi

'''

import os
import sensor as sns
try:
    from tkinter import *
    from tkinter import messagebox
    import cv2
    import numpy as np
    import mediapipe as mp
    import tensorflow as tf
    from tensorflow.keras.models import load_model
    import threading
    import random
    import pygame
    import sys
    import time
except:
    plat = sys.platform
    try:
        os.system("pip install tk")
        os.system("pip install open-cv")
        os.system("pip install numpy")
        os.system("pip install mediapipe")
        os.system("pip install tensorflow")
        os.system("pip install pygame")
        if plat == "linux":
            os.system("clear")
        else:
            os.system("cls")   
    except:
        print()
        print("This game only works if pip is installed on the system.")
        print("Kindly install pip to play the game.")
        print()
        exit()

plat = sys.platform
colo = "#add8e6"
csco = 0
score = 0
prevx = 200
prevy = 200
tey = "assets/images/ducky.png"
x = 200
y = 200
user = ""
phs = "O"

def encrypt(s):
    return bin(int(s))

def decrypt(s):
    return int(s, 2)

if plat == "linux":
    os.system("clear")
else:
    os.system("cls")

try:
    tr = open("user.txt", "r").read()
    pos = tr.index("\n")
    for i in range(pos):
        user += tr[i]
    score = int(decrypt(tr.replace(user + "\n", "")))
    if plat == "linux":
        os.system("clear")
    else:
        os.system("cls")
except:
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print()
    print("Welcome To The Duck Game, made by Abhay Tripathi. Please Read The Game Instructions Below Then Kindly Enter Your Desired Username.")
    print()
    print("Game Instructions:")
    print()
    print("1. To Earn Points, Click On The Moving Duck. 1 Click = 1 Point.")
    print("2. When You Click The Duck, A Ping Sound Will Confirm Your Click And The Point Will Be Recorded.")
    print("3. High Score Of Every User Is Maintained.")
    print("4. Enjoy The Game!!!")
    print()
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print()
    wr = open("assets/score/user.txt", "w")
    user = input("Kindly Enter Your Desired Username: ")
    wr.write(user + "\n" + encrypt("0"))
    wr.close()

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def get_coordinates(x, y):
    ax = (int)((x / sns.fw) * screen_width)
    ay = (int)((y / sns.fh) * screen_height)
    if ax < 250:
        ax = 250
    if ax > screen_width - 250:
        ax = screen_width - 250
    if ay < 230:
        ay = 230
    if ay > screen_height - 230:
        ay = screen_height - 230
    return [ax, ay]

root.attributes("-fullscreen", True)
root.configure(background = colo)
f = Frame(root)
width = 178
height = 0
photon = PhotoImage(file = "assets/images/plant.png")
while width < screen_width:
    l = Label(root, image = photon, bg = colo)
    l.place(x = width, y = height)
    width += 178
else:
    height += 140
    width -= 178
    while height < screen_height:
        l = Label(root, image = photon, bg = colo)
        l.place(x = width, y = height)
        height += 140
    else:
        height -= 140
        while width > -20:
            l = Label(root, image = photon, bg = colo)
            l.place(x = width, y = height)
            width -= 178
        else:
            width += 178
            while height > 0:
                l = Label(root, image = photon, bg = colo)
                l.place(x = width, y = height)
                height -= 140
lkx = Label(root, text = user, font = "Helvetica 37 bold", bg = "yellow", fg = "blue")
lkx.place(x = 0, y = 0)
if score == 1:
    pts = "Point"
else:
    pts = "Points"

if csco == 1:
    ptsg = "Point"
else:
    ptsg = "Points"
lk = Label(root, text = "High Score: " + str(score) + " " + pts + "  " + "\n" + "Current Score: " + str(csco) + " " + ptsg + "  ", font = "Helvetica 11 bold", bg = "yellow", fg = "brown")
lk.place(x = 0, y = 60)
lks = Label(root, text = "Duck Game", font = "Helvetica 60 bold", bg = "#9ccd8e", fg = "red")
lks.place(x = (screen_width // 2.5), y = 0)
lksc = Label(root, text = "by\nAbhay Tripathi", font = "Helvetica 20 bold", bg = "#9ccd8e", fg = "blue", justify = CENTER)
lksc.place(x = (screen_width // 2.5) + 120, y = 80)
lksc = Label(root, text = "Catch The Duck By Clicking It. 1 Click = 1 Point.", font = "Helvetica 15 bold", bg = "#ffc0cb", fg = "#013220")
lksc.place(x = 0, y = screen_height - 25)
pygame.mixer.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound("assets/audio/Water.wav"), loops = -1)

def action():
    global csco
    global score
    pygame.mixer.init()
    pygame.mixer.Channel(2).play(pygame.mixer.Sound("assets/audio/button.wav"))
    csco += 1
    if csco > score:
        fw = open("assets/score/user.txt", "w")
        fw.write(user + "\n" + encrypt(str(csco)))
        fw.close()
        score = csco
    if score == 1:
        ptsx = "Point"
    else:
        ptsx = "Points"
    if csco == 1:
        ptsgx = "Point"
    else:
        ptsgx = "Points"
    lk.config(text = "High Score: " + str(score) + " " + ptsx + "  " + "\n" + "Current Score: " + str(csco) + " " + ptsgx + "  ")

photo = PhotoImage(file = "assets/images/ducky.png")
b = Button(root, image = photo, borderwidth = 0, highlightthickness = 0, bg = colo, command = action)
b.place(x = 200, y = 200)
b.config(activebackground = b.cget("background"))

photoh = PhotoImage(file = "assets/images/hand.png")
bh = Button(root, image = photoh, borderwidth = 0, highlightthickness = 0, bg = colo)
bh.place(x = 400, y = 400)
bh.config(activebackground = bh.cget("background"))

def position():
    global x
    global y
    global prevx
    global prevy
    if prevx != x:
        global tey
        if prevx > x:
            if tey != "assets/images/duckyr.png":
                tey = "assets/images/duckyr.png"
                photoxc = PhotoImage(file = tey)
                b.config(image = photoxc)
                b.image = photoxc
            if prevx - 9 < x:
                prevx -= prevx - x
            else:
                prevx -= 9
        elif prevx < x:
            if tey != "assets/images/ducky.png":
                tey = "assets/images/ducky.png"
                photox = PhotoImage(file = tey)
                b.config(image = photox)
                b.image = photox
            if prevx + 9 > x:
                prevx += x - prevx
            else:
                prevx += 9
    if prevy != y:
        if prevy > y:
            if prevy - 9 < y:
                prevy -= prevy - y
            else:
                prevy -= 9
        elif prevy < y:
            if prevy + 9 > y:
                prevy += y - prevy
            else:
                prevy += 9
    b.place(x = prevx, y = prevy)
    threading.Timer(0.0000001, position).start()
position()

def Quack():
    pygame.mixer.init()
    pygame.mixer.Channel(1).play(pygame.mixer.Sound("assets/audio/duck.wav"))
    threading.Timer(5, Quack).start()
Quack()

def motion(event):
    global x
    global y
    global prevx
    global prevy
    xco, yco = event.x, event.y
    if abs(y - yco) < 300:
        if abs(x - xco) < 300:
            x = random.randint(250, screen_width - 250)
            y = random.randint(230, screen_height - 230)

root.bind("<Motion>", motion)

def hand_motion():
    xe = sns.lmx
    ye = sns.lmy
    if xe == "X":
        os._exit(0)
    if xe != "I" and ye != "I":
        sco = get_coordinates(xe, ye)
        xa = sco[0]
        ya = sco[1]
        bh.place(x = xa, y = ya)
        global y
        if abs(y - ya) < 300:
            global x
            if abs(x - xa) < 300:
                x = random.randint(250, screen_width - 250)
                y = random.randint(230, screen_height - 230)
        a = sns.hs
        global phs
        if a == "C":
            phs = "C"
        elif a == "O":
            if phs == "C":
                pygame.mixer.init()
                pygame.mixer.Channel(3).play(pygame.mixer.Sound("assets/audio/button.wav"))
                phs = "O"
    threading.Timer(0.01, hand_motion).start()
hand_motion()

def on_closing():
    global plat
    if messagebox.askokcancel("Duck Game", "Do you want to quit?"):
        root.destroy()
        pygame.mixer.stop()
        if plat == "linux":
            os.system("clear")
        else:
            os.system("cls")
        print("Thank You For Playing! We hope you enjoyed playing the Duck Game!")
        os._exit(0)

eb = Button(root, text = "EXIT GAME", command = on_closing, font = "Helvetica 20 bold", bg = "#ffe5b4", fg = "purple", justify = CENTER)
eb.place(x = screen_width - 162, y = screen_height - 40)
root.protocol("WM_DELETE_WINDOW", on_closing)
f.pack()
f.mainloop()