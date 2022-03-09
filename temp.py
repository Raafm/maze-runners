import pygame,time,random

from Maze.maze_diagonal_good import labirinth as maze   

from color import *
from animation import *



image_sprite = [pygame.image.load("pc\pc_right.png"),
                pygame.image.load("pc\pc_right_1.png"),
                pygame.image.load("pc\pc_right.png")]

img_with_flip = pygame.Surface((10, 10))

rect_size = 10


pygame.init()

screen_height = 700
screen_width = 1250
screen = pygame.display.set_mode((screen_width,screen_height))

screen.fill( Black ) # background color




# start maze
display_maze(screen,maze,terrain,rect_size = 8,animation = False)
for color in square_counter:
    display_counter(screen, 0 , color ,altura(color),screen_width)





pygame.display.update()
time.sleep(1)


pause = 0
running =  True

while running :

    # pygame stuff:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                   # exit pygame,
            running = False                          # exit() program
            


        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_SPACE:     # press breakspace to pause or play
                pause = not pause   
                time.sleep(0.2)

        if pause:
            continue


