from random import randint

class Dice:
    # size_dice must have value multiple of 4
    def __init__(self,canvas,dice_x,dice_y,size_dice=32,size_point=2):
        d1 = \
            [
            [0,0,0],
            [0,1,0],
            [0,0,0]
            ]

        d2 = \
            [
            [1,0,0],
            [0,0,0],
            [0,0,1]
            ]

        d3 = \
            [
            [1,0,0],
            [0,1,0],
            [0,0,1]
            ]

        d4 = \
            [
            [1,0,1],
            [0,0,0],
            [1,0,1]
            ]

        d5 = \
            [
            [1,0,1],
            [0,1,0],
            [1,0,1]
            ]

        d6 = \
            [
            [1,1,1],
            [0,0,0],
            [1,1,1]
            ]
            
        self.dd = { 1:d1 , 2:d2 , 3:d3 , 4:d4 , 5:d5 , 6:d6 }
        
        self.dice_x = dice_x
        self.dice_y = dice_y
        self.size_dice = size_dice
        self.size_point = size_point
        
        self.canvas = canvas
        
        self.rect = None
        
        self.value = self.rollDice()
        
        
        
    def rollDice(self):
        self.value = randint(1,6)
        self.drawDice()
        return self.value
        
    def drawDice(self):
        def calcPoint(ppos,k):
            return ppos+(k+1)*(self.size_dice//4)-self.size_point
        x , y = self.dice_x , self.dice_y
        X , Y = x+self.size_dice , y+self.size_dice
        self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(x,y,X,Y,fill="white")
        for i in range(0,3):
            for j in range(0,3):
                if (self.dd[self.value])[i][j]==1:
                    x , y = calcPoint(self.dice_x,i) , calcPoint(self.dice_y,j)
                    X , Y = x+2*self.size_point , y+2*self.size_point
                    self.canvas.create_rectangle(x,y,X,Y,fill="black") 