import pygame
import random

# Things to do/figure out


# Find excact position of rects  (manually or? ) ,



# Grid radene er hovedobjektene  i spilllet, spilleren vil interagere med en slik gjennom spillets gang...
class Grid_Row():
    def __init__(self):
        self.fields = [COLORS[1],COLORS[1],COLORS[1],COLORS[1]]
        self.feedback = (0,0,0,0)
        self.has_border= False
        self.fill = False

    def change_field_color(self, fieldnr, color):
        self.fields[fieldnr] = color

    def return_color(self, field_nr):
        return self.fields[field_nr]

    def draw(self, SCREEN, row):
        for i in range(4):
            if self.fill:
                peg = pygame.Rect(((60*i)+20 , (60*row) +20), PEG_SIZE )
                pygame.draw.rect(SCREEN, self.return_color(i), peg, width = 0, border_radius=15)
            else:
                peg = pygame.Rect(((60*i)+20 , (60*row) +20), PEG_SIZE )
                pygame.draw.rect(SCREEN, self.return_color(i), peg, width = 2, border_radius=15)
        
        if self.has_border:
            border= pygame.Rect(10,(60*row)+10,240,60)
            pygame.draw.rect(SCREEN, WHITE, border, width = 1)



# Colors
BOARD_COLOR1= (139,69,19) # Brown board background
BOARD_COLOR2= (102,51,0)   # Darker brown for unused pegholes

WHITE= (255,255,255)
BLACK = (0, 0, 0)
RED = (128, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 255)
YELLOW = (255,255,0)

COLORS = [BOARD_COLOR1, BOARD_COLOR2, WHITE, BLACK, RED, GREEN, BLUE, PURPLE, YELLOW]


# Global variables
PEG_SIZE = (40,40)


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

    board[4].change_field_color(2, GREEN)
    board[7].change_field_color(1, PURPLE)



    SCREEN.fill(BOARD_COLOR1)


    for i in range(10):
        if i == 5: board[i].has_border = True
        if i == 2: board[i].fill = True
        board[i].draw(SCREEN, i)

    
   
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



