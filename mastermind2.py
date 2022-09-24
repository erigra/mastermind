import pygame
import random



class Grid_Row():
    def __init__(self):
        self.fields = [COLORS[0],COLORS[0],COLORS[0],COLORS[0]]
        self.feedback = (0,0,0,0)

    def change_field_color(self, fieldnr, color):
        self.fields[fieldnr] = color

    def return_color(self, field_nr):
        return self.fields[field_nr]


# Colors
WHITE= (255,255,255)
BLACK = (0, 0, 0)
RED = (128, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 255)
YELLOW = (255,255,0)

COLORS = [BLACK, RED, GREEN, BLUE, PURPLE, YELLOW]

# Global variables
PEG_SIZE = (30,30)






# Functions ::::::::::::::::::::::::::::::::::::::::::::::::::::

def game_setup():
    # Board setup
    board = []
    for i in range(10):
        grid_row = Grid_Row()
        board.append(grid_row)
    return board
    
def solution_setup():
    solution = Grid_Row()
    for i in range(4):
        solution.change_field_color(i, COLORS[random.randint(1,5)])
    return solution


# Main program starts here :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def main():
    pygame.init()

    # Screen setup
    WIDTH, HEIGHT = 400, 800
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mastermind")
    clock = pygame.time.Clock()   
     

    board = game_setup()
    solution = solution_setup()        

    for i in range(4):
        peg = pygame.Rect((10 + PEG_SIZE[0]*i, 10), PEG_SIZE )
        pygame.draw.rect(SCREEN, solution.return_color(i), peg)

    
   
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()       
        
        pygame.display.flip() 


if __name__=="__main__":
    main()



