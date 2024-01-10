
from tkinter import *
import keyboard as keyb
import pygame
from PIL import ImageTk
from arguments import *
root = Tk()
root.geometry('1900x950+5+50')
root.title('...')
imag = ImageTk.PhotoImage(file='C:/Users/nikas/OneDrive/Desktop/game/photo/RUS.png')
imag1 = ImageTk.PhotoImage(file='C:/Users/nikas/OneDrive/Desktop/game/photo/ENG.png')
img =  ImageTk.PhotoImage(file='C:/Users/nikas/OneDrive/Desktop/game/photo/opt.png')
img1 = ImageTk.PhotoImage(file='C:/Users/nikas/OneDrive/Desktop/game/photo/LEN.png')
img2 = ImageTk.PhotoImage(file='C:/Users/nikas/OneDrive/Desktop/game/photo/back.png')
def play():
    global yess,yel,yess2, Eng_count, Rus_count
    
    if yer < 1:
        
        
        for i in range(101):
            
            yess2 += 100
            
        root.destroy()
    if yel > 1:
        
        for i in range(101):
            
            
            yess += 100
        root.destroy()
    if yer == 1 and yel == 1:
        for i in range(100):
            
            global cikl
            yess += 100
            
        root.destroy()
        

def option():
    pass
    
def len():
    
    len.place(y='1001200')
    option.place(y='100000')
    play.place(y='100000')
    def eng():
        global yer, Eng_count, Rus_count,root
        
        for _ in range(5):
            yer -= 2
        
    def rus():
        global yer,yel, Eng_count, Rus_count,root
        
        
        for _ in range(5):
            yel += 2
    def back():
        len.place(y='180')
        option.place(y='90')
        play.place(y='0')
        rus.place(y='10010101')
        eng.place(y='1201010')
        back.place(y='10000')    
    rus = Button(root,  command=rus, image=imag, font='10', height='90', width='1899')
    rus.pack()
    rus.place(y='0')
    
    eng = Button(root, text='ENG', command=eng, font='10', image=imag1, height='90', width='1899')
    eng.pack()
    eng.place(y='90')
    
    back = Button(root, text='BACK', command=back, font='10', image=img2, height='80', width='648')
    back.pack()
    back.place(x='0', y='840')
root.config(background='black')
imgt1 = ImageTk.PhotoImage(file='C:/Users/nikas/OneDrive/Desktop/game/photo/play.png')

play = Button(root, text='Play', command=play, image=imgt1, font='10', height='90', width='1900', fg='white', bg='gray')
play.pack()
play.place(y='0')
option = Button(root, text='Option', command=option, image=img, font='10', height='90', width='1900', fg='white', bg='gray')
option.pack()
option.place(y='90')
len = Button(root, text='leanguage', command=len, image=img1, font='10', height='90', width='1900', fg='white', bg='gray')
len.pack()
len.place(y='180')













root.overrideredirect(1)

root.mainloop()