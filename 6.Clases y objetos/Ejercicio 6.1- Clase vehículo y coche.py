from traceback import print_tb


class Vehículo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self) :
        return 'Color: {}\nRuedas:{}\nPuertas: {}'.format( self.color, self.ruedas, self.puertas)

class Coche(Vehículo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)

        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self) :
        return 'Color: {}\nRuedas:{}\nPuertas: {}\nVelocidad: {}\nCilindrada: {}'.format(self.color, self.ruedas, self.puertas,self.velocidad, self.cilindrada)


v = Vehículo('Azul', 4, 3)

c = Coche('Azul', 4, 3,250,300)

print(v)
print(c)