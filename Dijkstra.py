
import pygame,time,random


from Maze.maze_diagonal_good import labirinth as maze   

from color import *
from animation import *



def dijkstra(screen,maze, source,target, end_algorithm=True,start_paused = True):

    # se quiser criar screen, passe ela como False
    if not screen:
    
        pygame.init()

        screen_height = 700
        screen_width = 1250
        screen = pygame.display.set_mode((screen_width,screen_height))

        screen.fill( Black ) # background color


    square_counter = {terrain[0] : 0, terrain[1] : 0, terrain[2] : 0, source_color : 0, target_color : 0}


    # start maze
    display_maze(screen,maze,terrain, "Heap", "Dijkstra",rect_size = 7,animation = False)
    for color in square_counter:
        display_counter(screen, 0 , color ,altura(color),screen_width)

    pygame.display.update()
    time.sleep(1)

    from math import inf as INFINITY

    from data_struct.priority_queue import Heap

    # data struct for the algorithm
    predecessor =  list( list( ( -1 , -1 ) for _ in range(COLS) ) for _ in range(ROWS) )
    dist        =  list( list(   INFINITY  for _ in range(COLS) ) for _ in range(ROWS) )

    square_counter = {terrain[0] : 0, terrain[1] : 0, terrain[2] : 0, source_color : 0, target_color : 0}
    PQ = Heap(comp = lambda a,b: a[1] > b[1])


    # prepare to start the algorithm
    current = source

    PQ.insert((source,0))
    dist[source[0]][source[1]] = 0
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
           
            if PQ.not_empty():
                
                current,w = PQ.pop()
                i,j = current
                # bug dos pontos sem sentido
                if predecessor[current[0]][current[1]] == (-1,-1) or w == INFINITY or w > dist[current[0]][current[1]]:print("strange menu ",(i,j), "predecessor: ",predecessor[i][j], "peso:", dist[i][j], "w: ",w);continue
                
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
            cur_dist = dist[i][j]
            
            neighbours_pos = [ (i+1,j), (i-1,j), (i,j+1), (i,j-1)]
            
            # tenta atualizar posicoes ao redor para obter caminhos melhores
            for i_n,j_n in neighbours_pos:
                
                if  not out_of_limits(i_n,j_n,ROWS-1,COLS-1)    and   not_obstacle(maze,i_n,j_n) :
                    
                    if dist[i_n][j_n] > cur_dist + peso(maze[i_n][j_n]):           # found a better path to position (i_n,j_n)
                        dist[i_n][j_n] = cur_dist + peso(maze[i_n][j_n])           # update distance
                        
                        predecessor[i_n][j_n] = ( i , j )       # remember predecessor to construct final path
                        PQ.insert(((i_n , j_n),dist[i_n][j_n])) # insert in the priority_queue
                        insert_queue(screen, i_n , j_n )               # animation
            
            
            time.sleep(0.003)
            

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
    i,j = source = (0,0)
    temp_source = maze[i][j]
    maze[i][j] = source_color



    executar_novamente = True
    while executar_novamente:
        
        i,j = target = random_position(maze)
        #i,j = target = (ROWS-1,COLS-1) 
        temp_target = maze[i][j]
        maze[ i ][ j ] = target_color
        time.sleep(0.5)
        
        executar_novamente = dijkstra(None, maze, source, target, end_algorithm=True,start_paused = False,)

        maze[source[0]][source[1]] = temp_source  # repinta a source
        maze[target[0]][target[1]] = source_color # pinta target como novo source
        
        temp_source = temp_target                 # lembrar da cor do target (que sera novo source)
        source = target
        print()
