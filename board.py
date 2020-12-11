# processing file
import pygame
import random
from constants import*

def count_neighbors(old_board,row,col):
    count=0
    for i in range(-1,2):
        for j in range(-1,2):
            new_row = (row + i + ROWS) % ROWS
            new_col = (col +j + COLS ) % COLS
            count+=old_board[new_row][new_col]
    count -= old_board[row][col]            
    return count

class Board:                                          # the state board
    def __init__(self,new_board):                     # constructor
        self.board =[]                                
        if new_board==[]:                             # if new_board is empty, init a random state board
            for i in range(ROWS):
                self.board.append([])           
                for j in range(COLS):
                    self.board[i].append(random.randrange(0, 2, 1) )   # 1 or 0

        else:                                       # else update the state board
            self.board = new_board       

        
    def draw_board(self,win):                  #draw the board function
        win.fill(WHITE)                        #start with white background
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 1:   # if state is live (1), color the square black
                    pygame.draw.rect(win, BLACK, (row * SQUARE_SIZE,col * SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE))
               
                pygame.draw.rect(win, BLACK, (row * SQUARE_SIZE,col * SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE),1)  # draw the net
                
    def update_board(self,new_board):           # update the board state function
        for i in range(ROWS):
            new_board.append([])
            for j in range(COLS):
                neighbor = count_neighbors(self.board,i,j)             

                if self.board[i][j]== 1 and (neighbor < 2 or neighbor > 3):    # 1st and 2nd rule      
                    new_board[i].append(0)                                     # die       

                elif self.board[i][j] == 0 and neighbor==3:                    # 4th rule                                                        
                    new_board[i].append(1)                                     # reproduction
                else:                                                          # 3rd rule
                    new_board[i].append(self.board[i][j])                      # keep the old state
    