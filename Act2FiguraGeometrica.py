'''
Clase Figura Geometrica padre para Actividad 2
'''

class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho

    @property
    def alto(self):
        return self.__alto

    @property
    def ancho(self):
        return self.__ancho

    @alto.setter
    def alto(self,alto):
        self.__alto = alto

    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho

    def __str__(self):
        return f'''--> Alto: {self.__alto} --> Ancho: {self.__ancho}'''