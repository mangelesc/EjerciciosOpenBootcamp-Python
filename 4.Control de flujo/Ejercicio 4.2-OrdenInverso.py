numInicial = int(input('Numero inicial: '))
numFinal = int(input('Numero final: '))

print('Los números impares entre {} y {} son: '.format(numInicial,numFinal))
for n in range(numInicial,numFinal):
    
    if n % 2 != 0:
        print (n)
    n += 1
