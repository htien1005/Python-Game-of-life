# file xử lý 
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

class Board:
    def __init__(self,new_board):                     # constructor
        self.board =[]                                # bảng trạng thái
        if new_board==[]:                             # nếu new_board chưa có, nghĩa là khởi tạo mẫu ban đầu
            for i in range(ROWS):
                self.board.append([])           
                for j in range(COLS):
                    self.board[i].append(random.randrange(0, 2, 1) )   # 0 hoặc 1

        else:                               # update lại 
            self.board = new_board       
    

    
    def draw_board(self,win):                  #vẽ bảng lên window
        win.fill(WHITE)                        #background màu trắng
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 1:   #nếu giá trị 1 thì vẽ ô màu đen
                    pygame.draw.rect(win, BLACK, (row * SQUARE_SIZE,col * SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE))
               
                pygame.draw.rect(win, BLACK, (row * SQUARE_SIZE,col * SQUARE_SIZE, SQUARE_SIZE,SQUARE_SIZE),1)  # vẽ lưới
                
    def update_board(self,new_board):           # hàm để lấy trạng thái mới và ghi vào new_board
        for i in range(ROWS):
            new_board.append([])
            for j in range(COLS):
                neighbor = count_neighbors(self.board,i,j)               # đếm hàng xóm

                if self.board[i][j]== 1 and (neighbor < 2 or neighbor > 3):    # quy tắc 1 và 2      
                    new_board[i].append(0)                                     # chết       

                elif self.board[i][j] == 0 and neighbor==3:                    # quy tắc 4                                                        
                    new_board[i].append(1)                                     # sinh sản
                else:                                                          # quy tắc 3
                    new_board[i].append(self.board[i][j])                      # giữ nguyên trạng thái
    