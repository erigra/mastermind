from dataclasses import Field
from tkinter import Button
import pygame
import random

pygame.init()

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


# Screen setup
WIDTH, HEIGHT = 400, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind")

# Functions ::::::::::::::::::::::::::::::::::::::::::::::::::::

# Main program starts here :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def main():
    clock = pygame.time.Clock()   
    run = True 

    # Board setup
    board = []
    for i in range(10):
        grid_row = Grid_Row()
        board.append(grid_row)
    
    # Solution setup
    solution = Grid_Row()
    for i in range(3):
        solution.change_field_color(i, COLORS[random.randint(1,5)])

    print (solution.fields)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                      

if __name__=="__main__":
    main()



