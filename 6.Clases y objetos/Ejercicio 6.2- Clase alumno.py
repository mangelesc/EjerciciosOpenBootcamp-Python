class Alumno: 
    def __init__(self, nombre, nota):
        self.nombre = nombre 
        self.nota = nota

    def __str__(self):
        return '{}: Nombre: {}, nota: {}'.format(type(self).__name__, self.nombre, self.nota)

    def aprobado(self):
        if self.nota < 5:
            return 'Ups, has suspendido. T nota es: {}'.format(self.nota)
        
        else: 
            return 'Has aprobado!. Tu nota es: {}'.format(self.nota)


a1 = Alumno('Ángeles', 7)

print(a1)
print(a1.aprobado())