import pygame

#Dimensiones ventana:
W = 400
H = 400

#colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)

def drawMatrix(matrix, screen):
    tam_celda_x = 10
    tam_celda_y = 10
    for row in range(0,len(matrix)):
        for i in range(0,len(matrix[0])):
            value = matrix[row][i]
            if value:
                color = WHITE
            else:
                color=BLACK
            pygame.draw.rect(screen, color, (i * tam_celda_x, row * tam_celda_y, tam_celda_x, tam_celda_y))

def lastMaze(matrix,screen):
    drawMatrix(matrix,screen)
    end = False
    pygame.display.set_caption("Prim's Algorythm (Press ESC to exit)")
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    end = True 
    
