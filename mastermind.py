import pygame
import random

# Colors
WHITE= (255,255,255)
RED = (128, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255,255,0)

# Board setup
WIDTH, HEIGHT = 400, 800
BOARD = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind")



def draw_board():
    BOARD.fill(BLACK)
    pygame.display.update()





# Main program starts here :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def main():
    clock = pygame.time.Clock()

    run = True 
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print (mouse_pos)
        
            


        draw_board()




if __name__=="__main__":
    main()



