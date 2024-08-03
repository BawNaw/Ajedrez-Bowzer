# torre.py

class Torre:
    def __init__(self, color, fila, columna):
        self.color = color
        self.fila = fila
        self.columna = columna

    def movimiento_valido(self, nueva_fila, nueva_columna, tablero):
        # La torre se mueve en línea recta a lo largo de filas o columnas
        if nueva_fila == self.fila or nueva_columna == self.columna:
            # Asegurarse de que no hay obstáculos en el camino
            if nueva_fila == self.fila:  # Movimiento horizontal
                paso = 1 if nueva_columna > self.columna else -1
                for columna in range(self.columna + paso, nueva_columna, paso):
                    if tablero[self.fila][columna] is not None:
                        return False
            else:  # Movimiento vertical
                paso = 1 if nueva_fila > self.fila else -1
                for fila in range(self.fila + paso, nueva_fila, paso):
                    if tablero[fila][self.columna] is not None:
                        return False
            return True
        return False
