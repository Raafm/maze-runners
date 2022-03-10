from tkinter import *
from tkinter import ttk
from Dijkstra import dijkstra
from Gulosa import gulosa
from DFS import dfs
from BFS import bfs
from A_star import a_star
from color import *
from Maze.maze_diagonal_good import labirinth as maze

from animation import *
import time

source_color = Dark_yellow
target_color = Green

terrain = [
    Black,  
    brown, 
    royal_blue ,
]

square_counter = {terrain[0] : 0, terrain[1] : 0, terrain[2] : 0, source_color : 0, target_color : 0}
ROWS = len(maze)
COLS = len(maze[0])
rect_size = 7

def generate_random_maze():
    global maze
    maze = random_maze(ROWS,COLS,rect_size)




def selecionarAgente():
    N_score = 0

    opcao = vlista.get()

    
    if opcao == "Busca em Largura":
        print("Busca em Largura")
        i,j = source  = random_position(maze)
        #i,j = source = (0,0)
        temp_source = maze[i][j]
        maze[i][j] = source_color



        executar_novamente = True
        while executar_novamente:
            
            i,j = target = random_position(maze)
           
            temp_target = maze[i][j]
            maze[ i ][ j ] = target_color
            time.sleep(0.5)
            
            executar_novamente = bfs(None, maze, source, target, end_algorithm=True,start_paused = False,N_score = N_score)
            N_score += 1

            maze[source[0]][source[1]] = temp_source  # repinta a source
            maze[target[0]][target[1]] = source_color # pinta target como novo source
            
            temp_source = temp_target                 # lembrar da cor do target (que sera novo source)
            source = target
           
            # conserta o maze antes de terminar
            if executar_novamente ==  False:
                i,j = source
                maze[i][j] = temp_source

    elif opcao == "Busca em Profundidade":
        print("Busca em Pronfundidade")
        i,j = source  = random_position(maze)
        #i,j = source = (0,0)
        temp_source = maze[i][j]
        maze[i][j] = source_color



        executar_novamente = True
        while executar_novamente:
            
            i,j = target = random_position(maze)
            
            temp_target = maze[i][j]
            maze[ i ][ j ] = target_color
            time.sleep(0.5)
            
            executar_novamente = dfs(None, maze, source, target, end_algorithm=True,start_paused = False,N_score = N_score)
            N_score += 1
            maze[source[0]][source[1]] = temp_source  # repinta a source
            maze[target[0]][target[1]] = source_color # pinta target como novo source
            
            temp_source = temp_target                 # lembrar da cor do target (que sera novo source)
            source = target
           
            # conserta o maze antes de terminar
            if executar_novamente ==  False:
                i,j = source
                maze[i][j] = temp_source
        
    elif opcao == "Gulosa":
        print("Gulosa")
        i,j = source  = random_position(maze)
        #i,j = source = (0,0)
        temp_source = maze[i][j]
        maze[i][j] = source_color



        executar_novamente = True
        while executar_novamente:
            
            i,j = target = random_position(maze)
            #i,j = target = (ROWS-1,COLS-1) 
            temp_target = maze[i][j]
            maze[ i ][ j ] = target_color
            time.sleep(0.5)
            
            executar_novamente = gulosa(None, maze, source, target, end_algorithm=True,start_paused = False,N_score = N_score)
            N_score += 1
            maze[source[0]][source[1]] = temp_source  # repinta a source
            maze[target[0]][target[1]] = source_color # pinta target como novo source
            
            temp_source = temp_target                 # lembrar da cor do target (que sera novo source)
            source = target
           
            # conserta o maze antes de terminar
            if executar_novamente ==  False:
                i,j = source
                maze[i][j] = temp_source
            
    elif opcao == "Dijkstra":
        print("Dijkstra")
        
        i,j = source  = random_position(maze)
        #i,j = source = (0,0)
        temp_source = maze[i][j]
        maze[i][j] = source_color


        executar_novamente = True
        while executar_novamente:
            
            i,j = target = random_position(maze)
            
            temp_target = maze[i][j]
            maze[ i ][ j ] = target_color
            time.sleep(0.5)
            
            executar_novamente = dijkstra(None, maze, source, target, end_algorithm=True,start_paused = False,N_score = N_score)
            N_score += 1
            
            maze[source[0]][source[1]] = temp_source  # repinta a source
            maze[target[0]][target[1]] = source_color # pinta target como novo source
            
            temp_source = temp_target                 # lembrar da cor do target (que sera novo source)
            source = target

            # conserta o maze antes de terminar
            if executar_novamente ==  False:
                i,j = source
                maze[i][j] = temp_source

    elif opcao == "A*":
        print("A*")
        
        i,j = source  = random_position(maze)
        #i,j = source = (0,0)
        temp_source = maze[i][j]
        maze[i][j] = source_color


        executar_novamente = True
        while executar_novamente:
            
            i,j = target = random_position(maze)
            
            temp_target = maze[i][j]
            maze[ i ][ j ] = target_color
            time.sleep(0.5)
            
            executar_novamente = a_star(None, maze, source, target, end_algorithm=True,start_paused = False,N_score = N_score)
            N_score += 1

            maze[source[0]][source[1]] = temp_source  # repinta a source
            maze[target[0]][target[1]] = source_color # pinta target como novo source
            
            temp_source = temp_target                 # lembrar da cor do target (que sera novo source)
            source = target
            
            # conserta o maze antes de terminar
            if executar_novamente ==  False:
                i,j = source
                maze[i][j] = temp_source




#Definindo estrutura básica
app = Tk()
app.title("Labirintos e Agentes")
app.geometry("1000x550")

#Colocando imagem de fundo
#img = PhotoImage(file="labirinto_rodrigo.png")
#imagem_de_fundo = Label(app, image=img).pack()

#Definindo o texto do menu
texto_Agente = Label(app, fg = "black", text="MENU", font=("Helvetica", 18))
texto_Agente.pack(ipadx=10, ipady=70)
texto_Agente = Label(app, fg = "black", text="  Selecione o agente ", font=("Helvetica", 10))
texto_Agente.pack()
#Definindo as opções de Agentes
lista_de_Agentes = ["Busca em Largura", "Busca em Profundidade", "Gulosa", "Dijkstra", "A*"]
vlista = StringVar()
vlista.set(lista_de_Agentes[0]) #valor padrão

op_Agents = OptionMenu(app, vlista, *lista_de_Agentes)
op_Agents.pack()

#Definindo o botão de seleção
bnt_select = Button(app, text="selecionar", command=selecionarAgente, font=("Arial", 16))
bnt_select.pack()

texto_Agente = Label(app, text="")
texto_Agente.pack()
bnt_select = Button(app, text="gerar mapa", command = generate_random_maze, font=("Arial", 16))
bnt_select.pack()


app.mainloop()
