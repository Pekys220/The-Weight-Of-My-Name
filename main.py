import pygame
import constantes
from personaje import Personaje
from mundo import Mundo

pygame.init()
pygame.mixer.init #Permite agregar musica

# Definimos funciones importantes

def pantalla_inicio():
    ventana.fill(constantes.COLOR_CELESTE)
    dibujar_texto("The Weight Of My Name", font, constantes.COLOR_BLANCO,
                  constantes.ANCHO_VENTANA / 2 - 280,
                  constantes.ALTO_VENTANA / 2 - 200)
    dibujar_texto("El juego que te dice cuanto pesa tu nombre!", font_subtext, constantes.COLOR_BLANCO,
                  constantes.ANCHO_VENTANA / 2 - 180,
                  constantes.ALTO_VENTANA / 2 - 100)
    pygame.draw.rect(ventana, constantes.COLOR_BLANCO, input_box)
    dibujar_texto(nombre_jugador, font_text_input, constantes.COLOR_NEGRO, 
                  input_box.x + 10, input_box.y + 10)
    pygame.display.update()

def dibujar_texto(texto, fuente, color, x, y):
    img = fuente.render(texto, True, color)
    ventana.blit(img, (x, y))

def dibujar_nickname(jugador, nombre):
    texto = font_nickname.render(nombre, True, constantes.COLOR_BLANCO)
    texto_rect = texto.get_rect(center=(jugador.forma.centerx + 15, jugador.forma.top - 30),)
    ventana.blit(texto, texto_rect)


def escalar_imagen(image, scale):
    w = image.get_width()
    h = image.get_height()
    nueva_imagen = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    return nueva_imagen

def dibujar_grid():
    for x in range(30):
        pygame.draw.line(ventana, constantes.COLOR_BLANCO, (x * constantes.TILE_SIZE, 0), (x * constantes.TILE_SIZE, constantes.ALTO_VENTANA))
        pygame.draw.line(ventana, constantes.COLOR_BLANCO, (0, x * constantes.TILE_SIZE), (constantes.ANCHO_VENTANA, x * constantes.TILE_SIZE))

# INICIALIZAMOS EL TAMAÑO Y LA VENTANA DEL JUEGO
ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA, constantes.ALTO_VENTANA))

pygame.display.set_caption("The Weight Of My Name")

# Caja de texto

input_box = pygame.Rect(constantes.ANCHO_VENTANA / 2 - 100,
                        constantes.ALTO_VENTANA / 2 + 25, 200, 50)


# Variable para almacenar el nombre del jugador
nombre_jugador = "Ingrese su nombre..."

tamaño_nickname = 25

# Fuentes de texto

font = pygame.font.Font("assets/fonts/m3x6.ttf", 100)
font_subtext = pygame.font.Font("assets/fonts/Abaddon_Light.ttf", 20)
font_text_input = pygame.font.Font("assets/fonts/m3x6.ttf", 32)
font_nickname = pygame.font.Font("assets/fonts/m3x6.ttf", 25)

# Cargar imagenes del mundo
tile_list = []
for x in range(255):
    tile_image = pygame.image.load(f"assets/images/tiles/tile ({x + 1}).png")
    tile_image = pygame.transform.scale(tile_image, (constantes.TILE_SIZE, constantes.TILE_SIZE))
    tile_list.append(tile_image)

world_data = [
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164, 164],
    [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
]

world = Mundo()
world.process_data(world_data, tile_list)

# Definimos listas que contienen cada animacion del jugador:

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

mostrar_inicio = True
run = True

#Definimos la musica de fondo y los sonidos de algunas acciones

pygame.mixer.music.load("assets/sounds/time_for_adventure.mp3")
pygame.mixer.music.play(-1)

tecla = pygame.mixer.Sound("assets/sounds/tecla.mp3")
error = pygame.mixer.Sound("assets/sounds/error.mp3")
salto = pygame.mixer.Sound("assets/sounds/salto.mp3")

#EMPIEZA EL JUEGO

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if mostrar_inicio:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and nombre_jugador != "Ingrese su nombre...":
                    mostrar_inicio = False
                elif event.key == pygame.K_BACKSPACE:
                    nombre_jugador = nombre_jugador[:-1]
                    tecla.play()
                    if nombre_jugador == "":
                        nombre_jugador = "Ingrese su nombre..."
                elif event.key == pygame.K_SPACE:
                    error.play()
                else:
                    if nombre_jugador == "Ingrese su nombre...":
                        nombre_jugador = ""
                    nombre_jugador += event.unicode
                    tecla.play()
                    


    if mostrar_inicio:
        pantalla_inicio()
    else:
        reloj.tick(constantes.FPS)
        ventana.fill(constantes.COLOR_BG)
        dibujar_grid()

        # Movimiento del jugador:
        delta_x = 0
        delta_y = vel_y

        if mover_derecha:
            delta_x = jugador.velocidad
        elif mover_izquierda:
            delta_x = -jugador.velocidad

        # Restablecer la velocidad normal si no está corriendo
        if not sprint:
            jugador.velocidad = constantes.VELOCIDAD 

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

        #Limitar el mapa de forma horizontal

        jugador.forma.left += delta_x
        if jugador.forma.left < 0:
            jugador.forma.left = 0
        if jugador.forma.right > 965:
            jugador.forma.right = 965


        # Dibujar mundo
        world.draw(ventana)

        # Mover al jugador
        jugador.movimiento(delta_x, delta_y)

        #Modificar caracteristicas del jugador en consecuencia al nombre:

        caracteres_del_nombre = list(nombre_jugador)
        if len(caracteres_del_nombre) <= 2:
                tamaño_nickname = 25
                constantes.VELOCIDAD = 8.5
                constantes.AUMENTO_DE_VELOCIDAD = 10
                constantes.GRAVEDAD = 0.2
        elif len(caracteres_del_nombre) > 2 and len(caracteres_del_nombre) < 5:
                tamaño_nickname = 35
                constantes.VELOCIDAD = 6
                constantes.AUMENTO_DE_VELOCIDAD = 8
                constantes.GRAVEDAD = 0.4
        elif len(caracteres_del_nombre) >= 5 and len(caracteres_del_nombre) <= 6:
                tamaño_nickname = 45
                constantes.VELOCIDAD = 4
                constantes.AUMENTO_DE_VELOCIDAD = 6
                constantes.GRAVEDAD = 0.6
        elif len(caracteres_del_nombre) == 7:
                tamaño_nickname = 60
                constantes.VELOCIDAD = 3
                constantes.AUMENTO_DE_VELOCIDAD = 5
                constantes.GRAVEDAD = 0.8
        elif len(caracteres_del_nombre) >= 8 and len(caracteres_del_nombre) <= 12:
                tamaño_nickname = 70
                constantes.VELOCIDAD = 1.3
                constantes.AUMENTO_DE_VELOCIDAD = 2.5
                constantes.GRAVEDAD = 1
        elif len(caracteres_del_nombre) >= 12:
                tamaño_nickname = 80
                constantes.VELOCIDAD = 0.6
                constantes.AUMENTO_DE_VELOCIDAD = 0.9
                constantes.GRAVEDAD = 2
        font_nickname = pygame.font.Font("assets/fonts/m3x6.ttf", tamaño_nickname)
        


        # Actualizar estado del jugador y animaciones
        if isJump:
            jugador.animaciones = animaciones['jumping_up'] if vel_y < 0 else animaciones['jumping_down']
        elif mover_derecha or mover_izquierda:
            if sprint:
                jugador.animaciones = animaciones['running']
                jugador.velocidad = constantes.AUMENTO_DE_VELOCIDAD
            else:
                jugador.animaciones = animaciones['walking']
                jugador.velocidad = constantes.VELOCIDAD
        else:
            jugador.animaciones = animaciones['stay']
            jugador.velocidad = constantes.VELOCIDAD

        jugador.update()
        jugador.draw(ventana)

        dibujar_nickname(jugador, nombre_jugador.upper())
        dibujar_texto("Presiona shift derecho para cambiar nuevamente tu nombre", font_subtext, constantes.COLOR_BLANCO, 10, constantes.ALTO_VENTANA - 590)

        #Movimiento del jugador de acuerdo al pulsamiento (o no) de las teclas

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
                    salto.play()
                    vel_y = -constantes.SALTO  # Ajusta este valor para cambiar la altura del salto
                if event.key == pygame.K_RSHIFT:
                    mostrar_inicio = True
                    nombre_jugador = "Ingrese su nombre..."
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    mover_izquierda = False
                if event.key == pygame.K_RIGHT:
                    mover_derecha = False
                if event.key == pygame.K_LSHIFT:
                    sprint = False

        pygame.display.update()

pygame.quit()
