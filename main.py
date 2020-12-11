               
                # Đây là một con game đơn giản mô phỏng lại của Conway's Game of life
      # Về cơ bản thì đây là một mạng lưới các ô (tế bào) tạo nên một không gian hai chiều
      # Trạng thái của ô: sống(1) hoặc chết(0). Mỗi tế bào sẽ tương tác với tám hàng xóm (tế bào liền kề)
        # Từ mẫu ban đầu của hệ thống, các trạng thái tiếp theo của các thế hệ sau sẽ thay đổi

                            # Sự thay đổi được quyết định theo 4 quy tắc:
              # 1. Ô đang sống mà có ít hơn hai hàng xóm đang sống sẽ chết (quá ít dân)
              # 2. Ô đang sống mà có nhiều hơn 3 hàng xóm đang sống sẽ chết (quá đông dân)
              # 3. Ô đang sống mà có 2 hoặc 3 hàng xóm đang sống sẽ tiếp tục sống (tồn tại)
              # 4. Ô chết mà có đúng 3 hàng xóm đang sống sẽ chuyển thành ô sống (sinh sản)

import pygame
from constants import WIDTH, HEIGHT
from board import Board

# pylint: disable=no-member            
FPS =200           

WIN = pygame.display.set_mode((WIDTH,HEIGHT))           # hiển thị màn hình 
pygame.display.set_caption('Game of Life')              # tên của màn hình

def main():
    run = True
    clock = pygame.time.Clock()     
    new_board=[]
    
    while run:
        clock.tick(FPS)             # độ trễ thời gian
        board = Board(new_board)    # khởi tạo hoặc cập nhật bảng trạng thái
        new_board=[]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()     # update lại để vẽ đè lên         
        board.draw_board(WIN)        # vẽ bảng trạng thái   
        board.update_board(new_board)  #update bảng trạng thái 
       
    pygame.quit()

main()
