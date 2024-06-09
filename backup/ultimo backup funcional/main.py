import pygame
import constantes
from personaje import Personaje
from mundo import Mundo

pygame.init()
# INICIALIZAMOS EL TAMAÑO Y LA VENTANA DEL JUEGO
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("The Weight Of My Name")

def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return nueva_imagen

def dibujar_grid():
    for x in range(30):
        pygame.draw.line(ventana, constantes.COLOR_BLANCO, (x * constantes.TILE_SIZE, 0), (x * constantes.TILE_SIZE, constantes.ALTO_VENTANA))
        pygame.draw.line(ventana, constantes.COLOR_BLANCO, (0, x * constantes.TILE_SIZE), (constantes.ANCHO_VENTANA, x * constantes.TILE_SIZE))

# Cargar imagenes del mundo
tile_list = []
for x in range(255):
    tile_image = pygame.image.load(f"assets/images/tiles/tile ({x + 1}).png")
    tile_image = pygame.transform.scale(tile_image, (constantes.TILE_SIZE, constantes.TILE_SIZE))
    tile_list.append(tile_image)

world_data = [
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
]

world = Mundo()
world.process_data(world_data, tile_list)

# Jugador:
animacion_stay = []
for i in range(4):
    img = pygame.image.load(f"assets/images/characters/player/stay/{i}.png")
    img = escalar_imagen(img, constantes.ESCALA_PERSONAJE)
    animacion_stay.append(img)
animacion_walking = []
for i in range(8):
    img = pygame.image.load(f"assets/images/characters/player/walking/{i}.png")
    img = escalar_imagen(img, constantes.ESCALA_PERSONAJE)
    animacion_walking.append(img)
animacion_running = []
for i in range(8):
    img = pygame.image.load(f"assets/images/characters/player/running/{i}.png")
    img = escalar_imagen(img, constantes.ESCALA_PERSONAJE)
    animacion_running.append(img)
animacion_jumping_up = []
for i in range(4):
    img = pygame.image.load(f"assets/images/characters/player/jumping_up/{i}.png")
    img = escalar_imagen(img, constantes.ESCALA_PERSONAJE)
    animacion_jumping_up.append(img)
animacion_jumping_down = []
for i in range(4):
    img = pygame.image.load(f"assets/images/characters/player/jumping_down/{i}.png")
    img = escalar_imagen(img, constantes.ESCALA_PERSONAJE)
    animacion_jumping_down.append(img)

animaciones = {
    'stay': animacion_stay,
    'walking': animacion_walking,
    'running': animacion_running,
    'jumping_up': animacion_jumping_up,
    'jumping_down': animacion_jumping_down
}

jugador = Personaje(150, 400, animaciones['stay'])

# Definir variables de movimiento del jugador
isJump = False
mover_derecha = False
mover_izquierda = False
sprint = False
vel_y = 0  # Velocidad vertical del jugador

# Seteamos la variable para definir los fps del juego
reloj = pygame.time.Clock()

run = True

while run:
    reloj.tick(constantes.FPS)
    ventana.fill(constantes.COLOR_BG)
    dibujar_grid()

    # Movimiento del jugador:
    delta_x = 0
    delta_y = vel_y

    if mover_derecha:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda:
        delta_x = -constantes.VELOCIDAD
    if sprint and mover_derecha:
        delta_x = constantes.AUMENTO_DE_VELOCIDAD
    if sprint and mover_izquierda:
        delta_x = -constantes.AUMENTO_DE_VELOCIDAD


    # Aplica la gravedad cuando el jugador está en el aire
    if isJump:
        vel_y += constantes.GRAVEDAD
        if vel_y > 10:  # Limita la velocidad de caída
            vel_y = 10

    # Verificar colisión con el suelo
    if jugador.forma.bottom + delta_y > constantes.ALTURA_SUELO:
        jugador.forma.bottom = constantes.ALTURA_SUELO
        isJump = False
        vel_y = 0
        delta_y = 0

    # Dibujar mundo
    world.draw(ventana)

    # Mover al jugador
    jugador.movimiento(delta_x, delta_y)

    # Actualizar estado del jugador y animaciones
    if isJump:
        jugador.animaciones = animaciones['jumping_up'] if vel_y < 0 else animaciones['jumping_down']
    elif sprint and (mover_izquierda or mover_derecha):
        jugador.animaciones = animaciones['running']
        if sprint == True:
            constantes.VELOCIDAD = constantes.AUMENTO_DE_VELOCIDAD
        else:
            constantes.VELOCIDAD = constantes.VELOCIDAD
    elif mover_derecha or mover_izquierda:
        jugador.animaciones = animaciones['walking']
    else:
        jugador.animaciones = animaciones['stay']

    jugador.update()
    jugador.draw(ventana)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mover_izquierda = True
            if event.key == pygame.K_RIGHT:
                mover_derecha = True
            if event.key == pygame.K_LSHIFT:
                sprint = True
            if event.key == pygame.K_SPACE and not isJump:
                isJump = True
                vel_y = -constantes.SALTO  # Ajusta este valor para cambiar la altura del salto
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mover_izquierda = False
            if event.key == pygame.K_RIGHT:
                mover_derecha = False
            if event.key == pygame.K_LSHIFT:
                sprint = False

    pygame.display.update()

pygame.quit()
