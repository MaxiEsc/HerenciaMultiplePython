from Act1Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'rojo')
print(f'Cálculo área cuadrado: {cuadrado1.calcular_area()}')

#MRO - Method Resolution Order:
# Es una funcionalidad super interesante acerca sobre como funciona y que pasos ha seguido el interpretador de codigo para llevar a cabo el procedimiento
# Esto es lo que se resume la basicamente la funcion.
print(Cuadrado.mro())