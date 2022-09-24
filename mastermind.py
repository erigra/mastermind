from tkinter import Button
import pygame
import random

pygame.init()

# Colors
WHITE= (255,255,255)
BLACK = (0, 0, 0)

RED = (128, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 255)
YELLOW = (255,255,0)

COLORS = {1:RED, 2:GREEN, 3:BLUE, 4:PURPLE, 5:YELLOW}


# Board setup
WIDTH, HEIGHT = 400, 800
BOARD = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind")


# Functions ::::::::::::::::::::::::::::::::::::::::::::::::::::
def draw_peg(color, pos):
    pygame.draw.circle(BOARD, color, pos, 20)
    


def draw_board(pos): 
    BOARD.fill(BLACK)
    pygame.draw.circle(BOARD, RED, pos, 20)
  #  draw_peg(RED, pos)
    pygame.display.update()


def handle_mouse_movement(mousepressed):
    if mousepressed[pygame.MOUSEBUTTONDOWN]:
        pos = pygame.mouse.get_pos()
        return pos
        


def setup_correct():
    solution = [BLACK, BLACK, BLACK, BLACK]
    for n in range(4):
        solution[n]= COLORS[random.randint(1,5)]
    return solution


# Main program starts here :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def main():
    clock = pygame.time.Clock()
    position= (100,100)

    run = True 
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
               
        position = pygame.mouse.get_pos()
       
        draw_board(position)

if __name__=="__main__":
    main()



