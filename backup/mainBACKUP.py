import pygame
import constantes
from personaje import Personaje
from mundo import Mundo

pygame.init()
#INICIALIZAMOS EL TAMAÑO Y LA VENTANA DEL JUEGO
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("The Weight Of My Name")


def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (w*scale, h*scale))
    return nueva_imagen

def dibujar_grid():
    for x in range(30):
        pygame.draw.line(ventana, constantes.COLOR_BLANCO, (x*constantes.TILE_SIZE, 0), (x*constantes.TILE_SIZE, constantes.ALTO_VENTANA))
        pygame.draw.line(ventana, constantes.COLOR_BLANCO, (0, x*constantes.TILE_SIZE), (constantes.ANCHO_VENTANA, x*constantes.TILE_SIZE))

#cargar imagenes del mundo

tile_list= []
for x in range(255):
    tile_image = pygame.image.load(f"Juego_pygame/assets/images/tiles/tile ({x+1}).png")
    tile_image = pygame.transform.scale(tile_image, (constantes.TILE_SIZE, constantes.TILE_SIZE))
    tile_list.append(tile_image)

world_data= [
    [164,164,164,164,164,164,164,164,164,164,164,164,164, 164, 164],
    [164,164,164,164,164,164,164,164,164,164,164,164,164, 164, 164],
    [164,164,164,164,164,164,164,164,164,164,164,164,164, 164, 164],
    [164,164,164,164,164,164,164,164,164,164,164,164,164, 164, 164],
    [164,164,164,164,164,164,164,164,164,164,164,164,164, 164, 164],
    [164,164,164,164,164,164,164,164,164,164,164,164,164, 164, 164],
    [164,164,164,164,164,164,164,164,164,164,164,164,164, 164, 164],
    [164,164,164,164,164,164,164,164,164,164,164,164,164, 164, 164],
    [164,164,164,164,164,164,164,164,164,164,164,164,164, 164, 164],
    [164,164,164,164,164,164,164,164,164,164,164,164,164, 164, 164],
    [ 0 , 0 , 0 , 0 , 0 , 0,  0 , 0 , 0 , 0 , 0 , 0 , 0 ,  0 ,  0 ]

]

world= Mundo()
world.process_data(world_data, tile_list)
#Jugador:
animaciones= []

for i in range(4):
    img = pygame.image.load(f"Juego_pygame/assets/images/characters/player/stay/{i}.png")
    img = escalar_imagen(img, constantes.ESCALA_PERSONAJE)
    animaciones.append(img)


jugador = Personaje(150, 400, animaciones)



#Definir variables de movimiento del jugador

mover_arriba = False
mover_abajo = False
mover_derecha = False
mover_izquierda= False

#Seteamos la variable para definir los fps del juego
reloj = pygame.time.Clock()

run =  True

while run == True:

    reloj.tick(constantes.FPS)

    ventana.fill(constantes.COLOR_BG)
    dibujar_grid()

    #Movimiento del jugador:
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD

    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD

    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    
    #dibujar mundo
    world.draw(ventana)
    #Mover al jugador
    jugador.movimiento(delta_x, delta_y)

    jugador.update()

    jugador.draw(ventana)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_a:
                mover_izquierda = True
                Jugador_quieto = False
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.K_d:
                mover_derecha = True
                Jugador_quieto = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_a:
                mover_izquierda = False
                Jugador_quieto = True
            if event.key == pygame.K_s:
                mover_abajo = False
            if event.key == pygame.K_d:
                mover_derecha = False
                Jugador_quieto = True
            

    #print(f"{delta_x}, {delta_y}")

    pygame.display.update()
pygame.quit()