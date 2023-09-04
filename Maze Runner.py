from tkinter import *
from tkinter import messagebox
import tkinter as tk
import pygame.mixer
from mazeTurtle import startGame, rank_list

w = Tk()
w.title('미로게임')
w.geometry('450x475')
w.configure(bg="black")


file_img4= PhotoImage(file="img\\title.png")

lt = Label(w, text='미로게임', font='돋움 20 bold')
lt.place(x=157, y=35)

canvas = Canvas(w, width = 450, height = 475, bg = 'black')
canvas.place(x = 0, y = 0)
canvas.create_image(225,50, image=file_img4)
img = PhotoImage(file='img\\maze2.png')
canvas.create_image(225,200, image=img)
img2 = PhotoImage(file='img\\img2.png')
canvas.create_image(225,420, image=img2)
rtitle = PhotoImage(file='img\\ranktitle.png')

def rankcheck() :
    nw = tk.Toplevel(w)
    nw.title("랭킹")
    nw.geometry("500x700")
    rcanvas = Canvas(nw, width = 500, height = 700, bg = 'black')
    rcanvas.place(x = 0, y = 0)
    rcanvas.create_image(250,40, image=rtitle)
    
    ##################3
    print(rank_list)
    
    for i in range(len(rank_list)):
        rl = Label(rcanvas, text=f"{i+1}. {rank_list[i][1]}: {rank_list[i][0]} \n", font='돋움 20 bold', fg = 'white',bg = 'black')
        rl.place(x=50, y=80 + 40*i)
    
        
def play_music(file_path,repeat=True):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1 if repeat else 0)

file_path = "img\\The Maze Runner Soundtrack  - 01. The Maze Runner.mp3"

play_music(file_path)
    
def 게임종료():
    pygame.mixer.music.stop()
    w.destroy()

def stop_music():
    pygame.mixer.music.stop()
    

    
def 게임시작():
    if pygame.mixer.music.get_busy():
        stop_music()
    file_path = "img\\테일즈위버 OST - Reminiscence.mp3"  
    play_music(file_path)
    w.destroy()
    startGame()

file_img1= PhotoImage(file="img\\start.png")
file_img2= PhotoImage(file="img\\rank.png")
file_img3= PhotoImage(file="img\\quit.png")



s = Button(w,  command=게임시작,image=file_img1)
s.place(x=38, y=325)

d = Button(w,  command=rankcheck,image=file_img2)
d.place(x=162, y=325)

k = Button(w, command=게임종료,image=file_img3)
k.place(x=287, y=325)

w.mainloop()

