import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512 #400 us another option
DIMENSION = 8 #dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animations later on
IMAGES = {}

'''
Initialize a global dictionary of images. This will be called exactly once in the main
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ','bp', 'bR', 'bN', 'bB', 'bK','bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Chess/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    # Note: we can acess an image by saying 'IMAGES['wp']'

'''
The main driver for our code, this will handle user input and updating the graphics
'''
def main():
    
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False #flas variable for when a move is made

    loadImages() #only doing this once, before the while loop
    running = True
    sqSelected = () #no sq is selected initiatlly, keeps track of the last click of the user (tuple: (row,col))
    playerClicks = [] #keep track of player clicks (two tuples: [(6,4), (4,4)])



    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            #mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x,y) location of mouse
                col = location[0] // SQ_SIZE
                row = location[1] //SQ_SIZE
                if sqSelected == (row, col): #the user clicked the same square twice
                    sqSelected = () #deselect
                    playerClicks = [] #clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) #append for both 1st and 2nd clicks
                if len(playerClicks) == 2: #after the second click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)                    
                    print(move.getChessNotation())
                    for i in range(len(validMoves)):
                        if move == validMoves[i]:
                            gs.makeMove(validMoves[i])
                            moveMade = True       
                            sqSelected = () #reset user clicks
                            playerClicks = []
                    if not moveMade: 
                        playerClicks = [sqSelected]

            #key handler:
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: #undo when 'z' is pressed
                    gs.undoMove() 
                    moveMade = True

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False
        drawGameStat(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all the graphics within a current game state.
'''

def drawGameStat(screen, gs):
    drawBoard(screen) #draw the squares on the board
    #add in piece highlighting pr move suggestions (later)
    drawPieces(screen, gs.board) #draw pieces on top of those squares.

'''
Draw the square on the board. The top left is always light.
'''

def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Draw the pieces on the board using the current GameState.board
'''

def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION): 
            piece = board[row][col]
            if piece != "--": #not empty square
                screen.blit(IMAGES[piece],p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
