"""
#
#
#
#
"""

class Ball:
          def __init__(self ,parent, xc ,yc , ray):
                    self.xc = xc
                    self.yc = yc
                    self.ray = ray
                    self.parent = parent
                    self.item = 0
                    self.direction = [-1, -1]
          def draw(self):
                    R =  self.ray
                    self.item = self.parent.create_oval(self.xc-R, self.yc+R, self.xc+R, self.yc-R, fill="#79B4B7", width=0)

          def removeDraw(self):
                    if(self.item != 0):
                              self.parent.delete(self.item)
                              
          def switchXDirection(self):
                    self.direction[0] =  self.direction[0] * (-1)
                    
          def switchYDirection(self):
                    self.direction[1] =  self.direction[1] * (-1)
                    
          def move(self, dx, dy):
                    self.xc =  self.xc + self.direction[0] * dx
                    self.yc =  self.yc + self.direction[1] * dy
                    self.parent.move(self.item, self.direction[0]*dx, self.direction[1]*dy)
                    


if __name__ == "__main__":
          from tkinter import*
          page = Tk()
          page.geometry("710x410")
          #page.resizable(0,0)
          xc = 100
          yc = 100
          R = 5
          l = 700
          h = 400
          canvas = Canvas(page, bg="#2D2424", width=l, height=h)
          ball = Ball(canvas, xc, yc, R)
          ball.draw()
          def check_hit_border_in_the_next_step(ball, R,l,h,d):
                    com = ""
                    xc = ball.xc
                    yc = ball.yc
                    if xc+R+d > l or xc-R-d < 0:
                              com = com+ "x"
                    if yc+R+d > h or yc-R-d < 0 :
                              com = com + "y"
                    return com
          def changeDirection(ball, R,l,h,d):
                    step = check_hit_border_in_the_next_step(ball, R,l,h,d)
                    if  "x" in step:
                              ball.switchXDirection()
                    if  "y" in step:
                              ball.switchYDirection()

          def move(ball, l, h):
                    d = 3
                    changeDirection(ball, R, l, h, d)
                    ball.move(d, d)
                    page.after(25, lambda : move(ball, l, h))
                    
          canvas.grid(padx=5, pady=5)
          move(ball, l, h)
          page.mainloop()
