# Import required modules
import pygame as pg
from pygame.locals import *
from pygame import image
import time

XO = 'x'                                    # Create variable for players' turn
winner = None                               # Create variable for winner
draw = False                                # Create variable for draw
width, height = 400, 400                    # Create variables for game screen size
white, black = (255, 255, 255), (0, 0, 0)   # Create variables for colors to use

TTT = [[None]*3, [None]*3, [None]*3]        # Create variable for Tic Tac Toe grid

pg.init()                                                   # Initialize Pygame
fps = 30                                                    # Create variable for frame per second
CLOCK = pg.time.Clock()                                     # Create variable for Pygame Clock
screen = pg.display.set_mode((width, height + 100), 0, 32)  # Create variable for screen to display
pg.display.set_caption("Tic Tac Toe")                       # Set the title of the game

# Create variables for images to use
opening = pg.image.load('Images/tic tac opening.png')
x_img = pg.image.load('Images/x.png')
y_img = pg.image.load('Images/y.png')

# Resize the images
opening = pg.transform.scale(opening, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
y_img = pg.transform.scale(y_img, (80, 80))

# To diplay message
def draw_status():
    global winner, draw
    
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won!"
    if draw:
        message = 'Game Draw!'
        
    font = pg.font.Font(None, 30)
    text = font.render(message, 1, white)
    
    screen.fill(black, (0, 400, 500, 100))
    text_rect = text.get_rect(center =(width/2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()

# To open game
def game_opening():
    screen.blit(opening, (0, 0))
    pg.display.update()
    time.sleep(2)
    pg.display.flip()
    screen.fill(white)
    pg.draw.line(screen, black, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, black, (width/3*2, 0), (width/3*2, height), 7)

    pg.draw.line(screen, black, (0, height/3), (width, height/3), 7)
    pg.draw.line(screen, black, (0, height/3*2), (width, height/3*2), 7)
    
    draw_status()

# To check whether a player won or not
def check_win():
    global TTT, winner, draw
    
    for row in range (0, 3):
        if ((TTT [row][0] == TTT[row][1] == TTT[row][2]) and (TTT [row][0] is not None)):
            winner = TTT[row][0]
            
            pg.draw.line(screen, (250, 0, 0), (0, (row + 1)*height/3 - height/6),\
                (width, (row + 1)*height/3 - height/6), 4)
            break
        
    for col in range (0, 3):
        if ((TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None)):
            winner = TTT[0][col]
            
            pg.draw.line(screen, (250, 0, 0), ((col + 1)*width/3 - width/6, 0),\
                (((col + 1)*width/3 - width/6), height), 4)
            break
        
    if ((TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None)):
        winner = TTT[0][0]
            
        pg.draw.line(screen, (250, 70, 70), (50, 50), (350, 350), 4)
            
    if ((TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None)):
        winner = TTT[0][2]
            
        pg.draw.line(screen, (250, 70, 70), (350, 50), (50, 350), 4)
            
    if (all([all(row) for row in TTT]) and winner is None ):
        draw = True
        
    draw_status()

# To draw X and O symbols
def drawXO(row, col):
    global TTT, XO
    if row == 1:
        posx = 30
    if row == 2:
        posx = width/3 + 30
    if row == 3:
        posx = width/3*2 + 30
        
    if col == 1:
        posy = 30
    if col == 2:
        posy = height/3 + 30
    if col == 3:
        posy = height/3*2 + 30
    
    TTT[row-1][col-1] = XO
    if (XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO ='o'
    else:
        screen.blit(y_img, (posy, posx))
        XO = 'x'
    
    pg.display.update()

# To get user click location
def userClick():
    x,y = pg.mouse.get_pos()
    
    if (x<width/3):
        col = 1
    elif (x<width/3*2):
        col = 2
    elif (x<width):
        col = 3
    else:
        col = None
    
    if (y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif (y<height):
        row = 3
    else:
        row = None
    
    if (row and col and TTT[row-1][col-1] is None):
        global XO
        
        drawXO(row, col)
        check_win()

# To reset game to play again
def reset_game():
    global TTT, winner,XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    winner = None
    TTT = [[None]*3, [None]*3, [None]*3]
    game_opening()

# Call game_opening()
game_opening()

while (True):
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type is MOUSEBUTTONDOWN:
            userClick()
            if (winner or draw):
                reset_game()
    
    pg.display.update()
    CLOCK.tick(fps)
