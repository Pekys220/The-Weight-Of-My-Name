import pygame
import constantes
#Creamos el personaje y le damos forma y color

class Personaje():
    def __init__(self, x, y, animaciones):
        self.flip = True
        self.animaciones = animaciones
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = self.animaciones[self.frame_index] if self.animaciones else None
        self.forma = pygame.Rect(0, 0, constantes.ANCHO_PERSONAJE, constantes.ALTO_PERSONAJE)
        self.forma.center = (x, y)
    def update(self):
        if self.animaciones:  # Verificar si hay animaciones definidas
            cooldown_animacion = 400
            if pygame.time.get_ticks() - self.update_time >= cooldown_animacion:
                self.frame_index += 1
                self.frame_index %= len(self.animaciones)  # Utilizar operador módulo para asegurar que el índice esté dentro del rango válido
                self.update_time = pygame.time.get_ticks()
            self.image = self.animaciones[self.frame_index % len(self.animaciones)]

    def draw(self, interfaz):
        imagen_flip = pygame.transform.flip(self.image, self.flip, False) 
        interfaz.blit(imagen_flip, self.forma)
        #pygame.draw.rect(interfaz, pygame.Color(constantes.COLOR_PERSONAJE), self.forma)
    def movimiento(self, delta_x, delta_y):
        if delta_x < 0:
            self.flip= False
        if delta_x > 0:
            self.flip = True
        self.forma.x = self.forma.x + delta_x
        self.forma.y = self.forma.y + delta_y
