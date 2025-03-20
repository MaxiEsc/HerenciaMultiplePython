'''
Clase Cuadrado
'''
from Act2Color import Color
from Act2FiguraGeometrica import FiguraGeometrica

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'''Este Cuadrado es de alto = {self.ancho} de ancho = {self.ancho} color = {self.color}'''