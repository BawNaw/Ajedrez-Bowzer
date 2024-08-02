# tablero.py

class Tablero:
    def __init__(self):
        self.tablero = [
            [None for _ in range(8)] for _ in range(8)
        ]
        self.imagenes = {0: None, 1: None}

    def asignar_imagen_por_valor(self, valor, imagen):
        if valor in self.imagenes:
            self.imagenes[valor] = imagen
        else:
            raise ValueError(f"Valor {valor} no soportado en el tablero")

    def obtener_imagen_por_valor(self, valor):
        return self.imagenes.get(valor, None)

    def obtener_casilla(self, fila, columna):
        return self.tablero[fila][columna]

    def asignar_casilla(self, fila, columna, valor):
        self.tablero[fila][columna] = valor
