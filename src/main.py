import pygame
import sys
from tablero import Tablero
from peon import Peon
from torre import Torre
from selector import SelectorMovimiento
from variables import ubicaciones

# Configuración de la ventana
ANCHO, ALTO = 512, 512  # Ajusta el tamaño de la ventana al tamaño del tablero de ajedrez
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tablero de Ajedrez")

# Inicializa Pygame
pygame.init()

# Carga las imágenes (reemplaza con tus rutas reales)
imagen_colorA = pygame.image.load(ubicaciones.ref1)
imagen_colorB = pygame.image.load(ubicaciones.ref2)
imagen_peon_blanco = pygame.image.load(ubicaciones.ref3)
imagen_peon_negro = pygame.image.load(ubicaciones.ref4)
imagen_torre_blanca = pygame.image.load(ubicaciones.ref5)
imagen_torre_negra = pygame.image.load(ubicaciones.ref6)

# Redimensiona las imágenes a 64x64 píxeles
imagen_colorA = pygame.transform.scale(imagen_colorA, (64, 64))
imagen_colorB = pygame.transform.scale(imagen_colorB, (64, 64))
imagen_peon_blanco = pygame.transform.scale(imagen_peon_blanco, (52, 62))
imagen_peon_negro = pygame.transform.scale(imagen_peon_negro, (52, 62))
imagen_torre_blanca = pygame.transform.scale(imagen_torre_blanca, (52,62))
imagen_torre_negra = pygame.transform.scale(imagen_torre_negra, (52,62))

if __name__ == "__main__":
    mi_tablero = Tablero()

    # Asigna imágenes a las casillas
    mi_tablero.asignar_imagen_por_valor(0, imagen_colorA)
    mi_tablero.asignar_imagen_por_valor(1, imagen_colorB)

    # Crear peones blancos y negros
    peones_blancos = [Peon('blanco', 6, i) for i in range(8)]
    peones_negros = [Peon('negro', 1, i) for i in range(8)]

    # Crear torres blancas y negras
    torres_blancas = [Torre(imagen_torre_blanca, 7, 0), Torre(imagen_torre_blanca, 7, 7)]
    torres_negras = [Torre(imagen_torre_negra, 0, 0),Torre(imagen_torre_negra, 0, 7)]

    # Agregar peones al tablero
    for peon in peones_blancos:
        mi_tablero.asignar_casilla(peon.fila, peon.columna, peon)

    for peon in peones_negros:
        mi_tablero.asignar_casilla(peon.fila, peon.columna, peon)

    # Agregar torres al tablero
    for torre in torres_blancas:
        mi_tablero.asignar_casilla(torre.fila, torre.columna, torre)

    for torre in torres_negras:
        mi_tablero.asignar_casilla(torre.fila, torre.columna, torre)

    # Inicializar selector de movimiento
    selector_mov = SelectorMovimiento(mi_tablero)

    seleccion = None

    # Bucle principal
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                fila = y // 64
                columna = x // 64
                if seleccion:
                    if selector_mov.mover_pieza(fila, columna):
                        seleccion = None
                    else:
                        seleccion = (fila, columna)
                else:
                    if selector_mov.seleccionar_pieza(fila, columna):
                        seleccion = (fila, columna)

        # Dibuja el tablero
        for fila in range(8):
            for columna in range(8):
                x = columna * 64  # Tamaño de cada casilla es 64x64
                y = fila * 64
                if (fila + columna) % 2 == 0:
                    VENTANA.blit(imagen_colorA, (x, y))
                else:
                    VENTANA.blit(imagen_colorB, (x, y))

        # Dibuja las piezas
        for fila in range(8):
            for columna in range(8):
                pieza = mi_tablero.obtener_casilla(fila, columna)
                if isinstance(pieza, Peon):
                    x = columna * 64
                    y = fila * 64
                    if pieza.color == 'blanco':
                        VENTANA.blit(imagen_peon_blanco, (x, y))
                    else:
                        VENTANA.blit(imagen_peon_negro, (x, y))
                elif isinstance(pieza, Torre):
                    x = columna * 64
                    y = fila * 64
                    if pieza.color == imagen_torre_blanca:
                        VENTANA.blit(imagen_torre_blanca, (x, y))
                    else:
                        VENTANA.blit(imagen_torre_negra, (x, y))

        pygame.display.flip()
