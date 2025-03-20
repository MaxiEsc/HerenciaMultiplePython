'''
Clase Rectangulo
'''
from Act2Color import Color
from Act2FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self,ladoA,ladoB,color):
        FiguraGeometrica.__init__(self,ladoA,ladoB)
        Color.__init__(self,color)

    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'''Este rectangulo es de alto = {self.ancho} de ancho = {self.ancho} color = {self.color}'''