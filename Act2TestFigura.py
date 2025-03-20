from Act2Cuadrado import Cuadrado
from Act2Rectangulo import Rectangulo

cuadrado1 = Cuadrado(10, 'rojo')
print(f'Cálculo área cuadrado: {cuadrado1.area()}')
print(cuadrado1)
rectangulo1 = Rectangulo(3, 8, 'verde')
print(f'Cálculo área rectángulo: {rectangulo1.area()}')
print(rectangulo1)

print('Creación Objeto cuadrado'.center(50,'+'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f'Cálculo área cuadrado: {cuadrado1.area()}')
print(cuadrado1)

print('Creación Objeto rectángulo'.center(50,'+'))
rectangulo1 = Rectangulo(ladoB=9, ladoA=8, color='verde')
rectangulo1.ancho = 15
print(f'Cálculo área rectángulo: {rectangulo1.area()}')
print(rectangulo1)