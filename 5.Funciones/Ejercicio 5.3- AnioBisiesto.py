def bisiesto():
    anio = int(input('¿Qué año quieres consultar? '))
        
    if anio % 4 != 0:
        return False
    
    if anio % 100 == 0 and anio % 400 != 0:
        return False
    
    return True

print(bisiesto())