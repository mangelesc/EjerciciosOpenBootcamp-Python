def numPrimo():
    
    num = int(input('Introduce un número entero: '))

    if num>1:
        for i in range(2,int(num)):
            if (int(num) % i) == 0:
                return 'Ups, el número {} NO es primo. Es divisible entre {}'.format(num,i)
        else:
            return 'El número {} SI es primo'.format(num)
    else:
        return 'Lo siento, el número {} NO ES PRIMO. Los números primos son mayores que 1'.format(num)

print(numPrimo())