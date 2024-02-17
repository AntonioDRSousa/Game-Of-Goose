from random import randint

class Board:
    def __init__(self,canvas,x0,y0,ssq,nplayers):
        self.board = \
        [
        [15,16,17,18,19,20,21,22],
        [14,39,40,41,42,43,44,23],
        [13,38,55,56,57,58,45,24],
        [12,37,54,63,63,59,46,25],
        [11,36,53,62,61,60,47,26],
        [10,35,52,51,50,49,48,27],
        [ 9,34,33,32,31,30,29,28],
        [ 8, 7, 6, 5, 4, 3, 2, 1]
        ]
        
        self.coord = dict()
        
        self.nplayers = nplayers
        self.pieces = [None]*nplayers
        
        # for pieces
        self.colors = ['red','blue','green1','cyan','yellow','orange','magenta','purple']
        self.size_p = 15
        
        self.canvas = canvas
        self.x0 = x0
        self.y0 = y0
        self.ssq = ssq

    def drawBoard(self):
        
        for i in range(0,8):
            for j in range(0,8):
                t = str(self.board[j][i])
                r , s = self.ssq , (self.ssq//2)
                x , y = self.x0+i*r , self.y0+j*r
                X , Y = x+r , y+r
                x1 , y1 = x+s , y+s
                x2 , y2 = X+r , Y+r
                x3 , y3 = X , y+s
                color = "black"
                f="Times 14 bold"
                
                self.coord[self.board[j][i]] = (x,y,X,Y)
                
                if((self.board[j][i]%9)==0):
                    color = "blue"
                elif ( (self.board[j][i]==26) or (self.board[j][i]==53) ):
                    color = "yellow"
                elif (self.board[j][i] in [19,31,42,52,58]):
                    color = "red"
                elif (self.board[j][i] == 6):
                    color = "cyan"
                if (self.board[j][i] == 63):
                    color = "green1"
                    
                if (self.board[j][i]!=63):
                    self.canvas.create_rectangle(x,y,X,Y,fill="white")
                    self.canvas.create_text(x1,y1,text=t,fill=color,font=f)
                elif ((i,j)==(3,3)):
                    self.canvas.create_rectangle(x,y,x2,y2,fill="white")
                    self.canvas.create_text(x3,y3,text=t,fill=color,font=f)
                    
        l = [(0,8),(1,6),(2,4),(3,2),(4,1),(3,3),(2,5),(1,7),(0,8)]
        c = [(0,8),(1,6),(2,4),(3,2),None,(3,1),(2,3),(1,5),(0,8)]
        w = 3
        for i in range(0,9):
            x , y = self.x0+l[i][0]*self.ssq - w , self.y0+i*self.ssq
            X , Y = x+l[i][1]*self.ssq + 2*w, y
            self.canvas.create_line(x,y,X,Y,width=5)
            if c[i]!=None:
                y , x = self.y0+c[i][0]*self.ssq , self.x0+i*self.ssq
                Y , X = y+c[i][1]*self.ssq , x
                self.canvas.create_line(x,y,X,Y,width=2*w)

        for i in range(0,2*self.nplayers,2):
            self.drawPieces(i,0,False)
        
    def drawPieces(self,player,square,flag):
        if square == 0:
            if flag:
                self.canvas.delete(self.pieces[player])
                player=2*player
            py = 470
            x0 , y0 = (player+1)*self.size_p , py
            x1 , y1 = (player+2)*self.size_p , py+self.size_p
            z = player//2
        else:
            t = self.coord[square]
            self.canvas.delete(self.pieces[player])
            s_p = 5
            x0 , y0 = t[0]+s_p , t[1]+s_p
            x1 , y1 = x0+self.size_p , y0+self.size_p
            z = player
        self.pieces[z] = self.canvas.create_oval(x0,y0,x1,y1,fill=self.colors[z])