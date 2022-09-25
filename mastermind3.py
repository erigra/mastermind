from pickle import GLOBAL
from tkinter.tix import INTEGER
import pygame
import random

# Things to do/figure out
# 



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
BOARD_BG= (139,69,19) # Brown board background
BOARD_PEGHOLES= (102,51,0)   # Darker brown for unused pegholes

WHITE= (255,255,255)
BLACK = (0, 0, 0)
RED = (128, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 255)
YELLOW = (255,255,0)

COLORS = [BOARD_BG, BOARD_PEGHOLES, WHITE, BLACK, RED, GREEN, BLUE, PURPLE, YELLOW]


# Global variables ::::::::::::::::::::::::::::::::::::::::::::

# Brikke størrelse
PEG_SIZE = (40,40)

# Screen størrelse
WIDTH, HEIGHT = 400, 800


 

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
        solution.change_field_color(i, COLORS[random.randint(2,8)])
    return solution

# Tegn opp brettet sin state
def draw_board_state(SCREEN, board):
        
    # Bakgrunn og hull
    SCREEN.fill(BOARD_BG)
    for i in range(10):
        board[i].draw(SCREEN, i)


    
def draw_solution(SCREEN, solution):
     
     for i in range(4):
            solution_peg = pygame.Rect((60*i+20, HEIGHT-80), PEG_SIZE )
            pygame.draw.rect(SCREEN, solution.return_color(i), solution_peg, width = 0, border_radius=15)


def check_click(row):
    pegs= [0,0,0,0]
    for i in range(4):
        pegs[i]= pygame.Rect(((60*i)+20 , (60*row) +20), PEG_SIZE )
        mouse_pos = pygame.mouse.get_pos()
        if pegs[i].collidepoint(mouse_pos):
            print(f"treff! {i}")





# Main program starts here :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mastermind")
    clock = pygame.time.Clock()
  
    # Den raden som spilleren er på
    current_row = 0

    board = game_setup()
    solution = solution_setup()        

    run = True
    

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()  

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    current_row += 1

            # Legge inn her at dersom an trykker ENTER så sjekkes current_row mot løsning, 
            #  man får tilbakemeldin og current row avanseres med en



        draw_board_state(SCREEN, board)
        
        check_click(current_row)

        # Setter hvit ramme rundt current_row og fjerner på forrige
        board[current_row].has_border = True            
        if current_row > 0:                             
            board[current_row-1].has_border = False
        board[current_row].draw(SCREEN, current_row)    

        pygame.display.flip() 


if __name__=="__main__":
    main()



