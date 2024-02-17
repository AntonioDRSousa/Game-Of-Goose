from random import randint
from tkinter import Tk, Canvas, Menu
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from Board import *
from Dice import *

class Goose:
    def __init__(self):

        self.win = Tk()
        self.win.title("Game Of The Goose")
        self.win.geometry("600x600")
        self.win.resizable(False,False)       
        
        self.win.config(menu=self.createMenu())

        self.canvas = Canvas(self.win, bg="green",highlightthickness=0)
        self.canvas.pack(fill='both',expand=True)

        self.win.bind("<KeyPress>", self.key)
        
        self.win.mainloop()
        
    def createMenu(self):
        def help(x):
            if x==0:
                showinfo("Objective","The objective of game is be the first to landing in 63.")
            elif x==1:
                showinfo("Go over 63", "If you go over 63, you must go back the remainder number that go over 63.")
            elif x==2:
                showinfo("Landing in same place", "If you landing in same place of another piece, then pieces swap of place.")
            elif x==3:
                showinfo("Start with Dice 4 and 5","If you start with Dice 4 and 5, then you go to 53.")
            elif x==4:    
                showinfo("Start with Dice 3 and 6","If you start with Dice 3 and 6, then you go to 26.")
            elif x==5:
                showinfo("Goose - 9,18,27,36,45,54","If you land in Goose square(9,18,27,36,45,54), then you advance by number rolled.")
            elif x==6:
                showinfo("Bridge - 6","If you land in Bridge, 6 square, go to 12.")
            elif x==7:
                showinfo('Hotel - 19', "If you landing in Hotel, 19 square, you must wait 1 turn for play again. ")
            elif x==8:
                showinfo('Well - 31', "If you landing in Well, 31 square, you must wait until another player landing there for play again. ")
            elif x==9:
                showinfo("Maze - 42","If you land in Maze, 42 square, go to 39.")
            elif x==10:
                showinfo('Prison - 52', "If you landing in Prison, 52 square, you must wait until another player landing there for play again. ")
            elif x==11:
                showinfo("Death - 58","If you land in Death, 58 square, go to 1.")
                
        menu = Menu(self.win)
        
        menu1 = Menu(menu, tearoff=0)
        menu1.add_command(label="New Game",command=self.newGame)
        menu1.add_command(label="Exit",command=self.win.destroy)
        menu.add_cascade(label="Game",menu=menu1)
        
        menu2 = Menu(menu, tearoff=0)
        menu2.add_command(label="Objective",command=lambda x=0 : help(x))
        menu2.add_command(label="Go over 63",command=lambda x=1 : help(x))
        menu2.add_command(label="Landing in same place",command=lambda x=2 : help(x))
        menu2.add_separator()
        menu2.add_command(label="Start with Dice 4 and 5",command=lambda x=3 : help(x))
        menu2.add_command(label="Start with Dice 3 and 6",command=lambda x=4 : help(x))
        menu2.add_separator()
        menu2.add_command(label="Goose - 9,18,27,36,45,54",command=lambda x=5 : help(x))
        menu2.add_separator()
        menu2.add_command(label="Bridge - 6",command=lambda x=6 : help(x))
        menu2.add_command(label='Hotel - 19',command=lambda x=7 : help(x))
        menu2.add_command(label='Well - 31',command=lambda x=8 : help(x))
        menu2.add_command(label="Maze - 42",command=lambda x=9 : help(x))
        menu2.add_command(label='Prison - 52',command=lambda x=10 : help(x))
        menu2.add_command(label="Death - 58",command=lambda x=11 : help(x))
        
        menu.add_cascade(label="Help",menu=menu2)
        return menu
        
    def newGame(self):
        self.canvas.delete('all')
        while True:
            try:
                self.nplayers = int(askstring(title='Type Game', prompt='Number of Players(max: 8) : ',initialvalue="2"))
                if ((self.nplayers<2) or (self.nplayers>8)):
                    raise
                break
            except:
                showinfo('Error', 'Invalid Number .....')

        self.players = [0]*self.nplayers
        self.wait = [0]*self.nplayers
        self.turn = 0

        self.initBoard()
        self.initDices()
        
        self.text = self.canvas.create_text(300,25,text='Player '+str(self.turn),fill=self.board.colors[self.turn],font="Times 14 bold")
        
        
    def initBoard(self):
        x0 = 50
        y0 = 50
        ssq = 50
        self.board = Board(self.canvas,x0,y0,ssq,self.nplayers)
        self.board.drawBoard()
        
    def initDices(self):
        size_dice = 32
        size_point = 2
        dice1_x , dice1_y = 200 , 500
        dice2_x , dice2_y = 275 , 500
        self.d1 = Dice(self.canvas,dice1_x,dice1_y) 
        self.d2 = Dice(self.canvas,dice2_x,dice2_y)

    def rolldice(self):
        if not ((self.players[self.turn]==52)or(self.players[self.turn]==31)or(self.wait[self.turn]==1)):
            
            v1 = self.d1.rollDice()
            v2 = self.d2.rollDice()
            sum = v1 + v2
            
            old = self.players[self.turn]
            
            if (sum==9)and(self.players[self.turn]==0):
                if ((v1==4) or (v1==5)):
                    showinfo('Dice 4 and 5', "Player "+str(self.turn)+" roll 4 and 5, go to 53 . ")
                    self.players[self.turn] = 53
                elif ((v1==3) or (v1==6)):
                    showinfo('Dice 3 and 6', "Player "+str(self.turn)+" roll 3 and 6, go to 26 . ")
                    self.players[self.turn] = 26
            else:
                self.players[self.turn] += sum
            
            while True:
                if self.players[self.turn]>63:
                    self.players[self.turn] = 126-self.players[self.turn]
                    showinfo('Over 63', "Player "+str(self.turn)+" go over 63 and moving back . ")
                    continue
                self.board.drawPieces(self.turn,self.players[self.turn],False)
                if self.players[self.turn]==63:
                    showinfo('End', "Player "+str(self.turn)+" win . ")
                    self.canvas.delete('all')
                    break
                elif (self.players[self.turn]%9)==0:
                    self.players[self.turn] += sum
                    showinfo('Goose', "Player "+str(self.turn)+" landing Goose, and advance by number rolled . ")
                    continue
                elif (self.players[self.turn]==6):
                    self.players[self.turn]=12
                    showinfo('Bridge', "Player "+str(self.turn)+" landing Bridge, and go to 12 . ")
                elif (self.players[self.turn]==42):
                    self.players[self.turn]=39
                    showinfo('Maze', "Player "+str(self.turn)+" landing Maze, and go to 39 . ")
                elif (self.players[self.turn]==58):
                    self.players[self.turn]=1
                    showinfo('Death', "Player "+str(self.turn)+" death, and go to 1 . ")
                elif (self.players[self.turn]==52):
                    showinfo('Prison', "Player "+str(self.turn)+" landing in Prison, you must wait until another player landing there. ")
                elif (self.players[self.turn]==31):
                    showinfo('Well', "Player "+str(self.turn)+" landing in Well, you must wait until another player landing there. ")
                elif (self.players[self.turn]==19):
                    self.wait[self.turn]=1
                    showinfo('Hotel', "Player "+str(self.turn)+" landing in Hotel, you must wait 1 turn. ")
                    for i in range(0,self.nplayers):
                        if((self.players[i]==19)and(i!=self.turn)):
                            self.wait[self.turn]=0
                    
                for i in range(0,self.nplayers):
                    if (self.players[self.turn] == self.players[i])and(self.turn!=i)and(self.players[i]!=0) :
                        showinfo('Swap', "Player "+str(self.turn)+" swap with "+"Player "+str(i)+" . ")
                        self.players[self.turn] , self.players[i] = self.players[i] , old
                        self.board.drawPieces(i,self.players[i],(self.players[i]==0))
                        break
                break
        elif (self.wait[self.turn]==1):
            self.wait[self.turn]-=1
            
        self.board.drawPieces(self.turn,self.players[self.turn],False)
        
        self.turn = (self.turn+1)%self.nplayers
        self.canvas.itemconfig(self.text, text='Player '+str(self.turn),fill=self.board.colors[self.turn])
        
                    
    def key(self,event):
        if (event.char).lower()=="q":
            self.win.destroy()
        elif (event.char).lower()=="d":
            self.rolldice()