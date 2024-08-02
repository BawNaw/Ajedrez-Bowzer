# peon.py

class Peon:
    def __init__(self, color, fila, columna):
        self.color = color
        self.fila = fila
        self.columna = columna
        self.direccion = -1 if color == 'blanco' else 1  # Los peones blancos se mueven hacia arriba, los negros hacia abajo

    def movimiento_valido(self, nueva_fila, nueva_columna):
        # Movimiento básico de un peón: un paso adelante
        if nueva_columna == self.columna and nueva_fila == self.fila + self.direccion:
            return True
        # Movimiento inicial: dos pasos adelante
        if (self.color == 'blanco' and self.fila == 6) or (self.color == 'negro' and self.fila == 1):
            if nueva_columna == self.columna and nueva_fila == self.fila + 1 * self.direccion:
                return True
        return False