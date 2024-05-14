import pygame, numpy as np, random
class Sand:
    def __init__(self, coords, widthHeight, color) :
        self.boardX, self.boardY = coords
        self.widthHeight = widthHeight
        self.color = color

        self.body = pygame.Surface((widthHeight, widthHeight))
        self.body.fill(color)

    def drop(self, board : np.array) :
        boardHeight, boardWidth = board.shape
        if self.boardY + 1 < boardHeight: 
            
            canDown = not board[self.boardY + 1, self.boardX]
            canDownLeft = self.boardX - 1 >= 0 and not board[self.boardY + 1, self.boardX - 1]
            canDownRight = self.boardX + 1 < boardWidth and not board[self.boardY + 1, self.boardX + 1]
            
            xModifier = 0
            yModifier = 0
            
            if canDown:
                xModifier = 0
                yModifier = 1
            
            elif canDownLeft and not canDownRight:
                xModifier = -1
                yModifier = 1
            
            elif canDownRight and not canDownLeft:
                xModifier = 1
                yModifier = 1

            elif canDownRight and canDownLeft:
                xModifier = random.choice([-1,1])
                yModifier = 1

            #Change this sand's position on the board
            board[self.boardY, self.boardX] = False
            self.boardY = self.boardY + yModifier
            self.boardX = self.boardX + xModifier
            board[self.boardY, self.boardX] = True
        
    def boardCoords(self) :
        return (self.boardX, self.boardY)
    
    def screenCoords(self) :
        return (self.boardX * self.widthHeight , self.boardY * self.widthHeight)
            
