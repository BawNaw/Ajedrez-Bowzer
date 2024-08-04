# caballo.py

class Caballo:
    def __init__(self, color, fila, columna):
        self.color = color
        self.fila = fila
        self.columna = columna

    def movimiento_valido(self, nueva_fila, nueva_columna, tablero):
        # El caballo se mueve en forma de L: dos casillas en una dirección y una en la otra
        movs_posibles = [
            (self.fila + 2, self.columna + 1),
            (self.fila + 2, self.columna - 1),
            (self.fila - 2, self.columna + 1),
            (self.fila - 2, self.columna - 1),
            (self.fila + 1, self.columna + 2),
            (self.fila + 1, self.columna - 2),
            (self.fila - 1, self.columna + 2),
            (self.fila - 1, self.columna - 2)
        ]
        return (nueva_fila, nueva_columna) in movs_posibles
