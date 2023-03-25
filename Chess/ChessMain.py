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
    loadImages() #only doing this once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
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
