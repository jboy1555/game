
from tkinter import *
import keyboard as keyb
import pygame
from PIL import ImageTk

from time import *
from image import *


from arguments import *

from timeone import *
from start import *




for i in range(1):
    print(yess)
    print(yer)
    print(yel)
    print(yess2)

if yess > 1:
    from main import *

    

if yess2 > 0:    
    Eng_count = True
    pygame.init()
    win = pygame.display.set_mode((1900, 950))
    pygame.display.set_caption('game')
    pygame.display.set_icon(icon)
    print(v)
    test = 0
    
    
    

    while cikl == 1:
        
            
        
        pygame.time.delay(15)
        # Этот код заставляет игру не закрыватся
        keys = pygame.key.get_pressed() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cikl += 1
            
                        
        
        while money < 0:
            money += 1
            
        # Это магазин здесь написано что мы берем из глобала деньги и  к = деньгам = деньги минус сломаны меч и если к будет менше чем сломманы меч или меньше чем 1 то к = 0
        
        if keys[pygame.K_p] :
            
            
            
                
            
                    
            
            
                if playerx + speed > -15 and playerx + speed < 100:
                    if money >= 0:    
                        def buy():
                            
                            global breakswords
                            global money
                            breakswords = breakswords = 2        
                            money -= breaksword
                            
                            if money <= Move_Number:
                                for i in range(15):    
                                    root = Toplevel()
                                    root.geometry('250x250+100+100')
                                    root.title(money)
                                    
                                    root.config(bg='black')
                                    g = Label(root, text='YOU DONT HAVE MONEY',  height='5', width='25', bg='black', fg='yellow', font='10')
                                    g.pack()
                                    g.place()
                                    root.overrideredirect(1)
                                    root.mainloop()
                                    
                                    
                            if money < breaksword or money < 1:
                                money = 0
                    
                    
                    
                            
                        root = Tk()
                    
                        root.geometry('1000x500+500+250')
                        root.config(bg='black')
                        root.title(f'shop, {money}')
                        imgsword = ImageTk.PhotoImage(file='C:/Users/SoaPisGirseb/Desktop/gagaGame/photo/sword1.png')
                        btn = Button(root,  height='150', width='200', bg='gold',  command = buy, image=imgsword, compound=BOTTOM,  text='BreakSword',)
                        btn.pack()
                        btn.place(x='1')
                        talk = True
                        
                        root.mainloop()       
                    
                    
        
                        
            
        
        
        if keys[pygame.K_ESCAPE]:
            root = Tk()
            root.geometry('1900x950+5+50')
            root.title('...')
            imag = ImageTk.PhotoImage(file='C:/Users/nikas/OneDrive/Desktop/game/photo/RUS.png')
            imag1 = ImageTk.PhotoImage(file='C:/Users/nikas/OneDrive/Desktop/game/photo/ENG.png')
            img =  ImageTk.PhotoImage(file='C:/Users/nikas/OneDrive/Desktop/game/photo/opt.png')
            img1 = ImageTk.PhotoImage(file='C:/Users/nikas/OneDrive/Desktop/game/photo/LEN.png')
            img2 = ImageTk.PhotoImage(file='C:/Users/nikas/OneDrive/Desktop/game/photo/back.png')
        

            def option():
                pass
                
            def len():
                
                len.place(y='1001200')
                option.place(y='100000')
                
                def eng():
                    global cikl,Eng_count,root,yess2,yess,Rus_count
                    
                    Eng_count = True
                    Rus_count = False
                    yess -= 111
                    yess2 += 111
                    
                    root.destroy()
                    
                def rus():
                    global cikl,Eng_count,root,yess2,yess, Rus_count
                    Eng_count = False
                    Rus_count = True
                    yess += 111
                    yess2 -= 111
                    root.destroy()
                def back():
                    len.place(y='90')
                    option.place(y='0')
                
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

            
            option = Button(root, text='Option', command=option, image=img, font='10', height='90', width='1900', fg='white', bg='gray')
            option.pack()
            option.place(y='0')
            len = Button(root, text='leanguage', command=len, image=img1, font='10', height='90', width='1900', fg='white', bg='gray')
            len.pack()
            len.place(y='90')













            root.overrideredirect(1)

            root.mainloop()
            
                
            
        

            

                        
            
            

            

        # здесь написано что если игрок нажмет на букву р то откроются характеристки предметов я рекоминдую самому себе научится масиву и тогда этот код улучится потому что не будет засарено текст лаебалом
        if keys[pygame.K_r]:
            root = Tk()
            root.geometry('900x900+500+500')
            root.title('lol')
            
            text = Label(text = ' breaksword characters: \n Dmg = 15 \n forge = 60 \n sell = 100', bg='yellow', fg='black')
            text.pack()
            text.place(x='1')
        
            root.mainloop()  
            
        # Здесь написано что если игрок нажмет на букву м тооно покажет денги и если к будет меньше чем ноль то к будет равнятся нулю

        
        
                
        if keys[pygame.K_o]:
            def money2():
                pass
                
                
                


        
            root = Tk()
            root.geometry('500x50+25+75')
            root.title(money)
            root.config(bg='black')
            money1 = Button(root, text=f'Это Денги {money}', font='10', bg='black', width='20', height='20', fg='yellow', command=money2)
            money1.pack()
            
            root.mainloop()    
            
                
                
            
                    
            
        if keys[pygame.K_1] and breakswords == Sword_number:
            leveltop1 = playersword
            leveltop2 = playersword2
        # Это код движение персонажа и код анимаций если х будет  добовлятся скорость игрока и если будет добовлятся то лефт = ложь д райт = истына и здесь написано что если игрок будет нажимать на а то х будет добовлятся скорость игрока
        

        if keys[pygame.K_d] and moved == 2:
            playerx += speed
            right = True
            left = False 
            
        
        
        if playerx + speed > 1300:
            playerx = 1300
        # Это код движение персонажа и код анимаций если х будет  отбовлятс скорость игрока и если будет отбовлятся  то лефт = истына а райт = ложь и здесь написано что если игрок будет нажимать на а то х будет отбовлятся скорость игрока
        if keys[pygame.K_a] and movea == 2:
            playerx -= speed
            left = True
            right = False
            
        
            
        
        # Это граница мира
        if playerx - speed < -15:
            playerx = -15
        # Это анимация если лефт будет истына то оно будет рисовать анимацию
        
        if left == True:
            
            if v >= 21 and v <= 50:
            
                win.blit(fon2, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop2 == player3:    
                    win.blit(leveltop2, (playerx, (playery-left1)))
                elif leveltop2 == playersword2:
                    win.blit(leveltop2, (playerx, (playery-left2)))
                if breakswords == Sword_number and money >= Move_Number:
                    
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                    
                pygame.display.update() 
            if v >= 10 and v <=20:
                
                win.blit(fon1, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop2 == player3:    
                    win.blit(leveltop2, (playerx, (playery-left1)))
                elif leveltop2 == playersword2:
                    win.blit(leveltop2, (playerx, (playery-left2)))
                if breakswords == Sword_number and money >= Move_Number:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                        
                        

                pygame.display.update() 
                
    
                
            if v > 50 or v < 10:
            
                win.blit(fon, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop2 == player3:    
                    win.blit(leveltop2, (playerx, (playery-left1)))
                elif leveltop2 == playersword2:
                    win.blit(leveltop2, (playerx, (playery-left2)))
                if breakswords == Sword_number and money > Move_Number:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                
                            
                pygame.display.update()        
            
        # Это анимация если райт будет истына  то будет рисовать анимацию
        
        if right == True:
            
            
            
            if v >= 10 and v <=20:
                
                win.blit(fon1, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop1 == player2:    
                    win.blit(leveltop1, (playerx, (playery-right1)))
                elif leveltop1 == playersword:
                    win.blit(leveltop1, (playerx, (playery-right2)))
                if breakswords == Sword_number and money >= Move_Number:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                            
                pygame.display.update()    
            
            
            if v >= 21 and v <= 50:
                
                
                win.blit(fon2, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop1 == player2:    
                    win.blit(leveltop1, (playerx, (playery-right1)))
                elif leveltop1 == playersword:
                    win.blit(leveltop1, (playerx, (playery-right2)))
                if breakswords == Sword_number and money >= Move_Number:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                pygame.display.update()

            if v > 50 or v < 10:
                    
                
                win.blit(fon, (0, 0))
                win.blit(magic, (1500, 725))
                if leveltop1 == player2:    
                    win.blit(leveltop1, (playerx, (playery-right1)))
                elif leveltop1 == playersword:
                    win.blit(leveltop1, (playerx, (playery-right2)))
                if breakswords == Sword_number and money >= Move_Number:
                    
                    backpack1 = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                pygame.display.update()            
                
        # Это анимация если персонаж не будет двигатся ту лефт и райт = фолс и он не будет делать анимацию
        
        if right == False and left == False:
            
            if v >= 21 and v <= 50:
                
                
                win.blit(fon2, (0, 0))
                win.blit(magic, (1500, 725))
                win.blit(leveltop1, (playerx, playery))
                if breakswords == Sword_number and money >= Move_Number:
                    
                    backpack =  2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                pygame.display.update() 
            
            if v >= 10 and v <=20:
            
                
                win.blit(fon1, (0, 0))
                win.blit(magic, (1500, 725))
                win.blit(leveltop1, (playerx, (playery - 10)))
                if breakswords == Sword_number and money >= 150:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                        
                            
                pygame.display.update() 
            
            
            if right == False and left == False and v > 50 or v < 10:
                
                
                win.blit(fon, (0, 0))
                win.blit(magic, (1500, 725))
                win.blit(leveltop1, (playerx, playery))
                if breakswords == Sword_number and money >= 150:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                pygame.display.update() 
                
            
            if right == False and left == False and v >20 and v <=40:
            
                
                win.blit(fon2, (0, 0))
                win.blit(magic, (1500, 725))
                win.blit(leveltop1, (playerx, playery))
                if breakswords == Sword_number and money >= Move_Number:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                pygame.display.update() 
            

            if right == False and left == False and v >= 10 and v <=20:    
                
                win.blit(fon1, (0, 0))
                win.blit(magic, (1500, 725))
                win.blit(leveltop1, (playerx, (playery - 10)))
                if breakswords == Sword_number and money >= Move_Number:
                    
                    backpack = 2
                    win.blit(sword, (-25, -50))
                    pygame.display.update()
                    
                    

                pygame.display.update()            
            
        if shop1 == 2 or playerx + speed > 150: 
            movea = movea = 2
        
        if shop1 == 1 and playerx + speed < 150:
            movea = movea = 1
        
        
    

            
    # Это Диалог с волшебником у тебя здесь написано если игрок нажмет на т в конкретных кординатах то тогда и будет роботат твой скрыпт если нет то он не будет включатся
        if keys[pygame.K_t] and playerx + speed > 1300 :
           
           if Eng_count == True:
               from talkENG import *
               Rus_count = False
           if Rus_count == True:
               from talk import *
               Eng_count = False
           if Eng_count == False and Rus_count == True:
               from talk import *
               Eng_count = False
               Rus_count = True
        # Это прижок сдесь исползовоно физика кинетичаская энергя E = mV**2/2 где "M" это *масса* а "V" это *скорость обекта* 
        if jump == False:
            if keys[pygame.K_SPACE]:
                jump = True
                

        else:
            if jumppower >= -10:
                if jumppower < 0:
                    playery += (jumppower ** 2) / 2
                else: 
                    playery -= (jumppower ** 2) / 2
                jumppower -= 1
                
                
                    
            else:
                jump = False
                jumppower = 10
        pygame.display.update()

                