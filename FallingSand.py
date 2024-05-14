import sys, pygame, numpy as np
import sand

pygame.init()

#define graphics-related global variables
screenWidth = 750
screenHeight = 750
screenSize = screenWidth, screenHeight
black = 0,0,0
white = 255,255,255
screen = pygame.display.set_mode(screenSize)

#define the size of a piece of sand
sandWidthHeight = 5
boardWidth = screenWidth//sandWidthHeight
boardHeight = screenHeight//sandWidthHeight
board = np.full((boardHeight, boardWidth), False)

def start():
    #set up simulation
    starting = True
    global board
    screen.fill(black)
    clock = pygame.time.Clock()
    holdingMouseDown = False
    board.fill(False)
    currentSands = []
    
    while starting:
        timedelta = clock.tick(60)
        
        pygame.display.flip()
        screen.fill(black)
        
        #parse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_ESCAPE :
                    pygame.quit()
                    sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                holdingMouseDown = True
            elif event.type == pygame.MOUSEBUTTONUP:
                holdingMouseDown = False

        #update sand
        for sandEntity in currentSands:
                updateSand(sandEntity) 

        #spawn sand on mouse position
        if holdingMouseDown :
            mouseX, mouseY = pygame.mouse.get_pos()
            boardSandX = mouseX // sandWidthHeight
            boardSandY = mouseY // sandWidthHeight
            validMousePosition = boardSandX >= 0 and boardSandX < boardWidth and boardSandY >= 0 and boardSandY < boardHeight
            if validMousePosition :
                if  not board[boardSandY, boardSandX]: #if space is empty, spawn sand
                    tempSand = sand.Sand((boardSandX, boardSandY), sandWidthHeight, white)
                    currentSands.insert(len(currentSands), tempSand)
                    
                    board[boardSandY, boardSandX] = True

        currentSands.sort(key=lambda sand: sand.boardY, reverse=True) #sort sand so the lowest pieces of sand get updated first

        #render sand
        for sandEntity in currentSands :
            renderSand(sandEntity)

        pygame.display.update()  

#Helper Functions
def renderSand(sandEntity):
    screen.blit(sandEntity.body, sandEntity.screenCoords())

def updateSand(sandEntity) :
    global board
    sandEntity.drop(board)


if __name__ == '__main__':
    start()