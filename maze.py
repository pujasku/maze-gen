import pygame
import random
from draw import drawMatrix,lastMaze
import numpy as np
##Generador de laberintos utilizando el algoritmo de prim
#parametros pygame
SCREEN_WIDHT = 400
SCREEN_HEIGHT = 400
CELL_SIZE = 10

def initMaze(width,height):
    #inicializa matriz con todos valores false
    maze = np.zeros((width,height),dtype=bool)
    return maze

def frontier(maze,x,y):
    #devuelve frontera de la celda x,y (todas las paredes a una distancia de 2 sin contar diagonales)
    f = []
    width = len(maze[0])
    height = len(maze)
    if x >= 0 and x < width and y >= 0 and y < height:
        if x > 1 and not maze[x-2][y]:
            f.append((x-2, y))
        if x + 2 < width and not maze[x+2][y]:
            f.append((x+2, y))
        if y > 1 and not maze[x][y-2]:
            f.append((x, y-2))
        if y + 2 < height and not maze[x][y+2]:
            f.append((x, y+2))
    return f

def neighbours(maze,x,y):
    #devuelve todos los pasajes a 2 cuadros de distancia
    width = len(maze[0])
    height = len(maze)
    n = []
    if x >= 0 and x < width and y>=0 and y < height:
        if x > 1 and maze[x-2][y]:
            n.append((x-2,y))
        if x + 2 < width and maze[x+2][y]:
            n.append((x+2,y))
        if y > 1 and maze[x][y-2]:
            n.append((x,y-2))
        if y + 2 < height and maze[x][y+2]:
            n.append((x,y+2))
    return n

def union(maze,x1,y1,x2,y2):
    #uno ambos puntos
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    maze[x1][y1] = True
    maze[x][y] = True

def prim(width,height,screen):
    walls = set()
    maze = initMaze(width,height)
    x, y = (random.randint(0,width - 1), random.randint(0, height - 1))
    maze[x][y] = True
    front = frontier(maze,x,y)
    for f in front:
        walls.add(f)
    while walls:
        x,y = random.choice(tuple(walls)) 
        walls.remove((x,y))
        vec=neighbours(maze,x,y)
        if vec:
            nx,ny = random.choice(tuple(vec))
            union(maze,x,y,nx,ny)
        newfront = frontier(maze,x,y)
        for f in newfront:
            walls.add(f)
        # pygame
        screen.fill((0,0,0))
        drawMatrix(maze,screen)
        pygame.display.flip()
        pygame.time.wait(10)
    lastMaze(maze,screen)
        # printMaze(maze)
    # lasttMaze(maze)
def main():
    pygame.init()
    ventana = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDHT))
    pygame.display.set_caption("Prim's Algorythm")
    prim(40,40,ventana)

if __name__ == '__main__':
    main()
