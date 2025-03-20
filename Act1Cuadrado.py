'''
En este archivo .py tenemos un clase que hereda caracteristicas de 2 clases Por eso el concepto de herencia multiple
'''

from Act1FiguraGeometrica import FiguraGeometrica
from Act1Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho