
import pygame,time,random


from Maze.maze_diagonal_good import labirinth as maze   

from color import *
from animation import *




def dfs(screen,maze, source,target, end_algorithm=True,start_paused = True):

    # se quiser criar screen, passe ela como False
    if not screen:
    
        pygame.init()

        screen_height = 700
        screen_width = 1250
        screen = pygame.display.set_mode((screen_width,screen_height))

        screen.fill( Black ) # background color


    # start maze
    display_maze(screen,maze,terrain, "Stack", rect_size = 7,animation = False)
    for color in square_counter:
        display_counter(screen, 0 , color ,altura(color),screen_width)

    pygame.display.update()
    time.sleep(1)

    from math import inf as INFINITY

    from data_struct.stack import stack

    # data struct for the algorithm
    predecessor =  list( list( ( -1 , -1 ) for _ in range(ROWS) ) for _ in range(COLS) )

    
    S = stack()


    # prepare to start the algorithm
    current = source

    S.insert(source)
    
    predecessor[source[0]][source[1]] = source

    # animation loop
    found = False
    pause = start_paused
    running =  True

    while running :
        
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
        
        if not found:
           
            if S.not_empty():
                
                current = S.pop()
                i,j = current
                # bug dos pontos sem sentido
                if predecessor[i][j] == (-1,-1) :print("strange menu ",(i,j), "predecessor: ",predecessor[i][j]);continue
                
            else:
                pause = True
                continue

            i,j = current
           
            
            
            square_counter[maze[i][j]] += 1
                
            
                                
            display_counter(screen, square_counter[maze[i][j]] ,maze[i][j],altura(maze[i][j]),screen_width)
            pygame.display.update()
            
            if current == target:
                
                # avisar que achou
                font = pygame.font.Font('freesansbold.ttf',40)
                text = font.render("Found",True,(0,235,0))                          
                screen.blit(text,text.get_rect(center = (860,50)))
                pygame.display.update()
                
                found = True
                continue

            remove_queue(screen,i,j)  # animation
            

        if not found:
            i,j = current
            
            neighbours_pos = [ (i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            
            # tenta atualizar posicoes ao redor para obter caminhos melhores
            for i_n,j_n in neighbours_pos:
                
                if ( not out_of_limits(i_n,j_n,ROWS-1,COLS-1)  )  and   not_obstacle(maze,i_n,j_n) :
                    
                    if predecessor[i_n][j_n] == (-1,-1) and maze[i_n][j_n] != White:           # have not seen position (i_n,j_n)
                        
                        predecessor[i_n][j_n] = current       # remember predecessor to construct final path
                        S.insert( (i_n , j_n) ) # insert in the stack
                        insert_queue(screen, i_n , j_n )               # animation
            
            
            time.sleep(0.005)
            

        if found:
            time.sleep(0.01)

            path = find_path(screen,source,current,predecessor)
            path = traverse_path(screen,maze,path)
            
            # if path == False, user has closed window during find_path
            if path == False:
                executar_novamente = False
                return executar_novamente            
            if end_algorithm: 
                exectura_novamente = True
                return exectura_novamente
            pause = True
            found = False
            continue



if __name__ == "__main__":

    maze = random_maze(70,70,9)

    i,j = source  = random_position(maze)
    print(source) 
    temp_source = maze[i][j]
    maze[i][j] = source_color



    executar_novamente = True
    while executar_novamente:
        
        i,j = target = random_position(maze)
        #i,j = target = (ROWS-1,COLS-1) 
        temp_target = maze[i][j]
        maze[ i ][ j ] = target_color
        time.sleep(0.5)
        
        executar_novamente = dfs(None, maze, source, target, end_algorithm=True,start_paused = False)

        maze[source[0]][source[1]] = temp_source  # repinta a source
        maze[target[0]][target[1]] = source_color # pinta target como novo source
        
        temp_source = temp_target                 # lembrar da cor do target (que sera novo source)
        source = target
        print()
