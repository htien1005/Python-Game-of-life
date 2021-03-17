               
                    # this is a simple game that simulating Conway's Game of life
            # basically, this is a board consists of squares ( cells) that look like a 2D dimension
        # the cells's state: live(1) or dead(2). the cells will interact with their neighbors (closed cells)
               # the first state board of the system will be random, all the following will be changed 

                                 # the change will be decided by 4 rules:
            # 1.Any live cell with fewer than two live neighbors dies, as if by underpopulation.
            # 2.Any live cell with two or three live neighbors lives on to the next generation.
            # 3.Any live cell with more than three live neighbors dies, as if by overpopulation.
            # 4.Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

import pygame
from constants import WIDTH, HEIGHT
from board import Board

# pylint: disable=no-member            
FPS =20           

WIN = pygame.display.set_mode((WIDTH,HEIGHT))           # display the window with width and height 
pygame.display.set_caption('Game of Life')              # the name of the window

def main():
    run = True
    clock = pygame.time.Clock()     
    new_board=[]
    
    while run:
        clock.tick(FPS)                     # time delay when using loops
        current_board = Board(new_board)    # init or update the board state
        new_board=[]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False         # exit the loop
        
        pygame.display.update()     # update the old window         
        current_board.draw_board(WIN)        # draw the board to the window 
        current_board.update_board(new_board)  #update the board state 
       
    pygame.quit()               # quit the program 

main()
