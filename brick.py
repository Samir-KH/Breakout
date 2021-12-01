#!/usr/bin/env python
from time import sleep
from tkinter import *
class Brick():
	def __init__(self,parent,w,h,x,y):
		self.parent=parent
		self.width=w
		self.item=0
		self.height=h
		self.x=x
		self.y=y
	def draw(self):
		self.item= self.parent.create_rectangle(self.x,self.y,self.x+self.width,self.y+self.height,fill="#7E2811",width=2)
	def removeDraw(self):
		self.parent.delete(self.item)

if __name__=="__main__":
	root = Tk()
	root.minsize(760,400)
	root.maxsize(760,400)
	can = Canvas(root,width=500,height=300,bg="#123")
	can.pack(padx=5,pady=5)
	for i in range(0,800,20):
		for j in range(0,800,20):
			brick1= Brick(can,30,10,i,j)
			brick1.draw()
	root.mainloop()
