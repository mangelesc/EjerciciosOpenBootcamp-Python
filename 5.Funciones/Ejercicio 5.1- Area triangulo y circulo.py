import math

def areaCirculo(radio): 
    area = math.pi * pow(radio, 2)
    return area 

def areaTriangulo(altura, base):
    area = (altura * base) / 2
    return area

circulo = areaCirculo(3)
triangulo = areaTriangulo(5,7)


print('El área del círculo es : {}'.format(circulo))
print('El área del triángulo es : {}'.format(triangulo))
