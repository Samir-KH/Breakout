#!/usr/bin/env python

from tkinter import *
from brick import Brick
from Racket import Racket
from Ball import Ball
from TouchManager import TouchManager
from tkinter import messagebox

class App():
        def __init__(self,rows,columns):
                self.root=Tk()
                self.rows=rows
                self.columns=columns
                self.root.minsize(760,500)
                self.root.resizable(0,0)
                #*********************TouchManager***************#
                self.touchManager = TouchManager(self)
                #**********************Canvas*********************#
                self.parentW=745
                self.parentH=500        
                self.parent=Canvas(self.root,width=self.parentW,height=self.parentH,bg="#1d2424")
                self.parent.pack(padx=5,pady=5)
                self.w=34
                self.h=20
                self.gap=3
                #self.bricks=[0]*(self.rows*self.columns)
                self.bricks=[]
                #******************racket*********************#
                self.racketLength=120
                self.rxc=self.parentW//2-self.racketLength//2
                self.thickness=10
                self.ryc=self.parentH-self.thickness
                self.racket=Racket(self.parent,self.rxc,self.ryc,self.racketLength,self.thickness)
                #***************************ball******************************#
                self.dx = 3
                self.dy=2
                ray=4
                self.moveOn = True
                xball=self.parentW/2
                yball=self.parentH-ray-self.thickness-3
                self.ball= Ball(self.parent,xball,yball,ray)
                #*************************************************************#
        def createBrick(self,row,column):
                #brick1= Brick(self.parent,30,10,50,50)
                #brick1.draw()
                brick = Brick(self.parent,self.w,self.h,column*(self.w+self.gap)+4,row*(self.h+self.gap)+6)
                #self.bricks[row*self.columns+column]=brick
                self.bricks.append(brick)
                brick.draw()
        
        def removeBrick(self,row,column):
                self.parent(self.bricks[row*self.columns+column])
        
                
        def setLRButtonHandler(self):
          self.root.bind("<Left>", lambda event: self.racket.move("Left",self.parentW,0))
          self.root.bind("<Right>", lambda event: self.racket.move("Right",self.parentW,0))

        def check_hit_racket(self,d):
          xball = self.ball.xc
          yball = self.ball.yc
          ray = self.ball.ray
          x1= self.racket.xc
          x2 = self.racket.xc + self.racketLength

          if  yball +ray+ d > self.parentH - self.thickness :
                    if  x1 - ray <= xball <= x2 + ray:
                              return True
          return False

        def check_hit_border_in_the_next_step(self,width,height,dx, dy):
                        com = ""
                        xc = self.ball.xc
                        yc = self.ball.yc
                        ray = self.ball.ray
                        if xc+ray+dx > width or xc-ray-dx < 0:
                                com = com+ "x"
                        if  self.check_hit_racket(dy) or yc-ray-dy < 0 :
                                                com = com + "y"
                        if yc+ray+dy > height :
                                                com = "lose"
                                                messagebox.showinfo("break out messgae", "you lost")
                                                self.moveOn = False
                                                
                        return com
        def changeDirection(self,step):
                        
                        if  "x" in step:
                                                self.ball.switchXDirection()
                        if  "y" in step:
                                                self.ball.switchYDirection()

        def move(self):
                        step = self.check_hit_border_in_the_next_step(self.parentW, self.parentH,self.dx, self.dy)
                        self.changeDirection(step)
                        bricksToBreak, step = self.touchManager.checkNeighborsBrick()
                        self.changeDirection(step)
                        #for i in bricksToBreak:
                        if len(bricksToBreak) != 0:
                                self.touchManager.breakBrick(bricksToBreak[0])
                        self.ball.move(self.dx, self.dy)
                        if  self.moveOn :
                                self.parent.after(18, lambda : self.move())
                        else:
                                self.root.destroy()

        """def breakBrick(self,row, column):
          index = row * self.columns + column
          brick = self.bricks[index]
          brick.removeDraw()
          self.bricks[index] = 0"""

        def breakBrick(self, brick):
                brick.removeDraw()
                self.bricks.remove(brick)

        def start(self):
                self.racket.draw()
                self.setLRButtonHandler()
                self.ball.draw()
                self.move()
                for i in range(200):
                        self.createBrick(i//20,i%20)
                self.root.mainloop()

        def reset():
                pass

#******************************************************************************#
app=App(10,20)
app.start()
