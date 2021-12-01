"""
#
#
#
#
"""
class Racket:
          def __init__(self ,parent, xc ,yc , length, thickness):
                    self.xc = xc
                    self.yc = yc
                    self.parent = parent
                    self.thickness = thickness
                    self.length = length
                    self.item = 0
                    self.dx = 20
          def draw(self):
                    self.item = self.parent.create_rectangle(self.xc, self.yc, self.xc+ self.length , self.yc + self.thickness, fill="#79B4B7", width=0)

          def removeDraw(self):
                    if(self.item != 0):
                              self.parent.delete(self.item)
                              
          def move(self, direction, xRLimit, xLLimit):
                    if direction == "Left":
                              direction = -1
                    if direction == "Right":
                              direction = 1
                    if direction == 1 or direction == -1 :
                              if xLLimit - self.dx  <  self.xc + self.dx * direction and self.xc  +  self.dx * direction + self.length < xRLimit + self.dx  :
                                        self.xc =  self.xc + self.dx * direction
                                        self.parent.move(self.item, self.dx * direction, 0)
                    else:
                              raise Exception('An error occurred, direction must to be right or  left ')
                    


if __name__ == "__main__":
          from tkinter import*
          page = Tk()
          page.geometry("710x410")
          #page.resizable(0,0)
          xc = 100
          h = 400
          thickness = 10
          yc = h-thickness
          l = 700
          canvas = Canvas(page, bg="#2D2424", width=l, height=h)
          racket = Racket(canvas, xc, yc, 120, thickness)
          racket.draw()
          page.bind("<Left>", lambda event: racket.move("Left",l,0))
          page.bind("<Right>", lambda event: racket.move("Right",l,0))
         
          canvas.grid(padx=5, pady=5)
          page.mainloop()
