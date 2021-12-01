class TouchManager:
          def __init__(self, App):
                    self.app= App
          
          def getBallGridCoords(self):
                    column = int((self.app.ball.xc+ 4)//  (self.app.w+ self.app.gap ))
                    row = int((self.app.ball.yc +6)// (self.app.h + self.app.gap))
                    return row, column

          def checkNeighborsBrick(self):
                              bricks = []
                              TotalCom = ""
                              direction = self.app.ball.direction.copy()
                              row, column = self.getBallGridCoords()
                              #---------------- cas 1
                              nexRow = row + direction[1]
                              nexColumn = column + direction[0]
                              result = self.findBrickToBreak(nexRow, nexColumn)
                              if result != None :
                                        bricks = bricks + [result[0]]
                                        TotalCom = TotalCom + result[1]
                              #---------------- cas 3
                              nexRow = row 
                              nexColumn = column + direction[0]
                              result = self.findBrickToBreak(nexRow, nexColumn)
                              if result != None :
                                        bricks = bricks + [result[0]]
                                        TotalCom = TotalCom + result[1]
                              #---------------- cas 2
                              nexRow = row + direction[1]
                              nexColumn = column
                              result = self.findBrickToBreak(nexRow, nexColumn)
                              if result != None :
                                        bricks = bricks + [result[0]]
                                        TotalCom = TotalCom + result[1]
                              return bricks, TotalCom
                              
          def findBrickToBreak(self, nexRow, nexColumn):
                              index = nexRow *self.app.columns +  nexColumn
                              #print(nexRow, nexColumn)
                              if 0 <= index < len(self.app.bricks):
                                        brick = self.app.bricks[index]
                                        #print(brick)
                                        com = self.checkBreakingPossibility(brick)
                                        if com != "":
                                                  #self.app.moveOn = False
                                                  return [brick, com]

          def checkBreakingPossibility(self, brick):
                    com =""
                    if brick == 0:
                              return com
                    xball = self.app.ball.xc
                    yball = self.app.ball.yc
                    dx = self.app.dx
                    dy = self.app.dy
                    width = brick.width
                    height = brick.height
                    xCbrick = brick.x + width/2
                    yCbrick = brick.y + height/2
                    R = self.app.ball.ray
                    if abs(xball - xCbrick) < dx+ width/2 + R :
                              com = com + "y"
                    if abs(yball-yCbrick) < dy + height/2 + R :
                              com = com + "x"

                    return com

          def breakBrick(self, brick):
                    brick.removeDraw()
                    self.app.bricks[self.app.bricks.index(brick)] = 0
"""
                    if abs(xball - xCbrick) < dx+ width/2 + R and  (yCbrick - R  <= yball + dy <= yCbrick +  height +R or yCbrick - R  <= yball -dy <= yCbrick +  height +R ):
                              com = com + "x"
                    if abs(yball-yCbrick) < dy + height/2 + R and (xCbrick -R <= xball +dx <= xCbrick +  width +R or xCbrick -R <= xball -dx<= xCbrick +  width +R):
                              com = com + "y"
"""
