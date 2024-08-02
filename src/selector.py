# selector.py

class SelectorMovimiento:
    def __init__(self, tablero):
        self.tablero = tablero
        self.seleccion = None

    def seleccionar_pieza(self, fila, columna):
        pieza = self.tablero.obtener_casilla(fila, columna)
        if pieza:
            self.seleccion = (fila, columna)
            return True
        return False

    def mover_pieza(self, nueva_fila, nueva_columna):
        if self.seleccion:
            fila, columna = self.seleccion
            pieza = self.tablero.obtener_casilla(fila, columna)
            if pieza and pieza.movimiento_valido(nueva_fila, nueva_columna):
                self.tablero.tablero[nueva_fila][nueva_columna] = pieza
                self.tablero.tablero[fila][columna] = None
                self.seleccion = None
                return True
        return False
