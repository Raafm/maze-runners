import pygame,random,time
from color import *

from Maze.maze_diagonal_good import labirinth as maze

def out_of_limits(i, j, i_max, j_max):
    return  i < 0 or j < 0 or i > i_max or j > j_max

def draw_point(screen, color, i,j,rect_size = 8,show = False,radius = None):
    if radius is None:
        pygame.draw.circle(screen ,  color  ,  (50 + rect_size//2 + rect_size*i , 50 + rect_size//2 + rect_size*j ), rect_size//3  )
    else:  pygame.draw.circle(screen ,  color  ,  (50 + rect_size//2 + rect_size*i , 50 + rect_size//2 + rect_size*j ), radius  )
    if show: pygame.display.update()


def random_maze(ROWS = 100,COLS = 100, rect_size = 6):
    from Maze.randomHumanizedweightMaze import  assign_weights
    empty_maze = list(list( White for _ in range(COLS) ) for _ in range(ROWS)) 
    maze = assign_weights(empty_maze, rect_size = rect_size,  end_animation = True,N_loops = 100)
    return maze


def random_position(maze):
    ROWS = len(maze)
    COLS = len(maze[0]) 
    # choose random obstacles' positions
    i,j = random.randint(1, ROWS-1), random.randint(1, COLS-1)

    while maze[i][j] == White:
        i,j = random.randint(1, ROWS-1), random.randint(1, COLS-1)
        # if is not an obstacle
    return i,j

def display_maze(screen, maze, terrain, name_data_struct, algorithm_name, rect_size = 7, animation = True ):
    ROWS = len(maze)
    COLS = len(maze[0])

    for x in range(ROWS):
        if animation: time.sleep(0.01)
        for y in range(COLS):
            pygame.draw.rect(screen ,  maze[x][y]  , ( 50 + rect_size*x , 50 + rect_size*y , rect_size , rect_size ) )
        
        if animation: pygame.display.update()

    pygame.display.update()
    if animation: time.sleep(1)
    
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render(algorithm_name,True, Dark_red)                      
    screen.blit(text,text.get_rect(center = (1100,80)))

    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("in "+ name_data_struct,True, Flame)                      
    screen.blit(text,text.get_rect(center = (1100,250)))
    
    font = pygame.font.Font('freesansbold.ttf',40)
    text = font.render("seen",True, Dark_yellow)                      
    screen.blit(text,text.get_rect(center = (1100,350)))

    pygame.display.update()


def display_counter(screen,number,color,position,screen_width= 1200):
    pygame.draw.rect(screen, color, (760 , 100+100*position , 80, 60))    # erase what was before in the prime 
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render(str(number) ,True, White)                      
    screen.blit(text,text.get_rect(center = (800,135+100*position)))


ROWS = len(maze)
COLS = len(maze[0])
rect_size = 7

terrain = [
    Black,  # terrain [0], peso 1
    brown, 
    royal_blue ,
]

source_color = Dark_yellow
target_color = Green

square_counter = {terrain[0] : 0, terrain[1] : 0, terrain[2] : 0, source_color : 0, target_color : 0}




def remove_queue(screen,i,j):
    if not out_of_limits(i,j,ROWS-1,COLS-1):
        draw_point(screen, Dark_yellow, i,j, rect_size, False)

def insert_queue(screen,i,j):
    if not out_of_limits(i,j,ROWS-1,COLS-1):
        draw_point(screen, Flame, i,j, rect_size, False)

def peso(color):
    return 1*(color == terrain[0]) + 10*(color == terrain[1]) + 100*(color == terrain[2])

def altura(color): 
    return 0*(color == terrain[0]) + 1*(color == terrain[1]) + 2*(color == terrain[2]) + 3*(color == target_color) + 4*(color == source_color)


def not_obstacle(maze,i,j):
    return (maze[i][j] in terrain) or (maze[i][j] == Green)



def find_path(screen,source,current,predecessor):
    

    path = []

    pause = False
    running = True
    while  running:
        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   # exit pygame,
                running = False                          # exit() program
                
                executar_novamente = False
                return executar_novamente

            
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_SPACE:     # press breakspace to pause or play
                    pause = not pause   
                    time.sleep(0.2)
        
        if pause:
            continue

        time.sleep(0.01)
        

        (x,y) = current
        path.append(current)

        if( current != source ):
            draw_point(screen,Lime,x,y,rect_size,False)
            x,y = predecessor[x][y]
            draw_point(screen,Green,x,y,rect_size,False)
            pygame.display.update()

            current = (x,y)

        if current == source:
            draw_point(screen,Green,x,y,rect_size,True)
            
            path.reverse()
            return path


def traverse_path(screen,maze,path,rect_size = 7):
    
    pos_antiga = path[0]
    C = 1

    pause = False
    running = True
    while  running:
        # pygame stuff:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   # exit pygame,
                running = False                          # exit() program
                
                executar_novamente = False
                return executar_novamente

            
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_SPACE:     # press breakspace to pause or play
                    pause = not pause   
                    time.sleep(0.2)
        
        if pause:
            continue

        i,j = path[C]

        # pinta proxima posicao (desloca o agente uma casa pra "frente")
        draw_point(screen,     White    , i  ,  j  ,  rect_size, show = True)
        
        # apaga posicao antiga
        i_a , j_a  =  pos_antiga
        draw_point(screen, maze[i_a][j_a], i_a , j_a , rect_size, show = True)

        pos_antiga = i,j

        C+= 1
        if C == len(path):
            executar_novamente = True
            return executar_novamente
        
        # tempo que demora na casa (variar o tempo de acordo com o peso)
        "TALVEZ VALHA A PENA MUDAR O VALOR DOS PESOS"
        time.sleep(0.003*peso(maze[i][j]))
        #if maze[i][j] == terrain[0]:
        #   time.sleep(0.1)
        #if maze[i][j] == terrain[1]:
        #    time.sleep(0.4)
        #if maze[i][j] == terrain[2]:
        #    time.sleep(0.8)
