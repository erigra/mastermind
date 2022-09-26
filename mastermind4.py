import pygame
import random
import time

# Grid radene er hovedobjektene  i spilllet, spilleren vil interagere med en slik gjennom spillets gang...
class Grid_Row():
    def __init__(self):
        self.fields = [COLORS[1],COLORS[1],COLORS[1],COLORS[1]]
        self.feedback = []
        self.has_border= False
        self.fill = False
        self.counted = [False, False, False, False]

    def change_field_color(self, fieldnr, color):
        self.fields[fieldnr] = color

    def return_color(self, field_nr):
        return self.fields[field_nr]

    def draw(self, SCREEN, row):         
        for i in range(4):                              # Tegner opp pegs
            if self.fill:
                peg = pygame.Rect(((60*i)+20 , (60*row) +75), PEG_SIZE )
                pygame.draw.rect(SCREEN, self.return_color(i), peg, width = 0, border_radius=15)
            else:
                peg = pygame.Rect(((60*i)+20 , (60*row) +75), PEG_SIZE )
                pygame.draw.rect(SCREEN, self.return_color(i), peg, width = 2, border_radius=15)
        
        for i in range(len(self.feedback)):             # Tegner opp fedback pegs basert på om den finnes
            if self.feedback[i] == 1:
                feedback_peg = pygame.Rect((275+(30*i), row*60+85), FEEDBACK_PEG_SIZE)
                pygame.draw.rect(SCREEN, BLACK, feedback_peg, border_radius=10)
            if self.feedback[i] == 2:
                feedback_peg = pygame.Rect((275+(30*i), row*60+85), FEEDBACK_PEG_SIZE)
                pygame.draw.rect(SCREEN, WHITE, feedback_peg, border_radius=10)

        if self.has_border:                             # Tegner opp hvit ramme rundt current_row
            border= pygame.Rect(10,(60*row)+65,240,60)
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

# Text stuff
pygame.font.init()
TITLE_FONT = pygame.font.SysFont("Helvetica", 44)
GAME_RULES_FONT = pygame.font.SysFont ("Helvetica", 12)


# Global variables ::::::::::::::::::::::::::::::::::::::::::::

# Brikke størrelse
PEG_SIZE = (40,40)
FEEDBACK_PEG_SIZE = (20,20)

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
    print(solution.fields)
    return solution

# Tegn opp brettet sin state
def draw_board_state(SCREEN, board):
    SCREEN.fill(BOARD_BG)               #Bakgrunnsfarge
    for i in range(10):
        board[i].draw(SCREEN, i)        #Hullene/brikkene i brettet   
    title = TITLE_FONT.render("MASTER MIND", 1, BLACK)              # Titteltekst
    SCREEN.blit(title, ((WIDTH//2 - title.get_width()//2) ,10))
    hide_solution = pygame.Rect((10, HEIGHT-130), (240, 60))        # Løsningsboks
    pygame.draw.rect(SCREEN, BOARD_PEGHOLES,hide_solution)
    rules = GAME_RULES_FONT.render("Find the hidden color combination!", 1, BLACK)          # Reglertekst
    SCREEN.blit(rules,(10,HEIGHT-63))
    rules_2 = GAME_RULES_FONT.render("Change the colors in the white square by clicking the circles", 1, BLACK)
    SCREEN.blit(rules_2,(10,HEIGHT-48))
    rules_3 = GAME_RULES_FONT.render("Press RETURN to check vs the solution and advance to next row", 1, BLACK)
    SCREEN.blit(rules_3,(10,HEIGHT-33))
    rules_4 = GAME_RULES_FONT.render("BLACK = one correct color and placement, WHITE = one correct color", 1, BLACK)
    SCREEN.blit(rules_4,(10,HEIGHT-18))


# Tegn opp løsningen   
def draw_solution(SCREEN, solution):     
    for i in range(4):
        solution_peg = pygame.Rect((60*i+20, HEIGHT-120), PEG_SIZE )
        pygame.draw.rect(SCREEN, solution.return_color(i), solution_peg, width = 0, border_radius=15)
    

# Sjekker om et hull på currrent row blir klikket og roterer fargen i såfall
def check_click(row, board):
    pegs= [0,0,0,0]
    for i in range(4):
        pegs[i]= pygame.Rect(((60*i)+20 , (60*row) +75), PEG_SIZE )
        mouse_pos = pygame.mouse.get_pos()
        if pegs[i].collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            old_color = board.return_color(i)
            new_color_index = COLORS.index(old_color)+1 
            if new_color_index in [0,1,9]:
                new_color_index = 2
            board.change_field_color(i, COLORS[new_color_index])
            board.fill = True
            time.sleep(0.2)

# Sjekker spillerens forslag opp imot løsningen
def check_row_fields(row, board, solution):
    
    solution_colors = []                                                # Lager en liste med solution sine farger
    for i in range(4):
        solution_colors.append(solution.return_color(i))

    answer_colors = []                                                  # Lager en liste med aktuell rekke sine farger
    for i in range(4):
        answer_colors.append(board[row].return_color(i))

                                         
    for i in range(4):
        if board[row].return_color(i) == solution.return_color(i):      # Rett farge og plass, fjerner pegs som matcher både i løsning og svar
            board[row].feedback.append(1)
            solution_colors.remove(solution.return_color(i))
            answer_colors.remove(board[row].return_color(i)) 
    
    white_pegs = 0                                         # Arne magic again! Rett farge men feil plass på gjenværende pegs
    checked_colors = []
    for color in answer_colors:
        if color in solution_colors and color not in checked_colors:
            num_answer = answer_colors.count(color)       # Number of times a remaining color is used in answer
            num_solution = solution_colors.count(color)   # Number of times a remaining color is used in solution
            white_pegs += min(num_answer, num_solution)   # Gives out the lowest of the above values  
        checked_colors.append(color)
    for _ in range(white_pegs):
        board[row].feedback.append(2)
    

# Main program starts here :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mastermind")
    clock = pygame.time.Clock()
  
    # Nytt spill setup
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
                    check_row_fields(current_row, board, solution)
                    if board[current_row].feedback==[1,1,1,1]: 
                        draw_board_state(SCREEN, board)                       
                        draw_solution(SCREEN, solution)
                        win_text=TITLE_FONT.render("You won!", 1, WHITE)          
                        SCREEN.blit(win_text,((WIDTH//2-win_text.get_width()//2),(HEIGHT//2-win_text.get_width()//2)))
                        pygame.display.flip()
                        time.sleep(5)
                        main()                                  
                    current_row += 1 
                    if current_row==10:
                        draw_board_state(SCREEN, board)
                        draw_solution(SCREEN, solution)
                        loose_text=TITLE_FONT.render("You lost!", 1, WHITE)          
                        SCREEN.blit(loose_text,((WIDTH//2-loose_text.get_width()//2),(HEIGHT//2-loose_text.get_width()//2)))
                        pygame.display.flip()
                        time.sleep(5)
                        main()

        # Tegner opp brettet
        draw_board_state(SCREEN, board)

        # Setter hvit ramme rundt current_row og fjerner på forrige
        board[current_row].has_border = True            
        if current_row > 0:                             
            board[current_row-1].has_border = False
        board[current_row].draw(SCREEN, current_row)    

        check_click(current_row, board[current_row])

        # Oppdaterer skjermen
        pygame.display.flip() 


if __name__=="__main__":
    main()
