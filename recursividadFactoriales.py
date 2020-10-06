print('\n\n--------------La recursividad')
print('Tecnica en la que una funcion se llama a si misma para')
print('solucionar el mismo problema en partes mas pequeñas')
print('que eventualmente al unir todo obtienes el resultado')

print('\nFACTORIALES    n! = n*(n-1)!')
 
def factorial(n):
    """ Calcula el factorial de la entrada n
    n = int > 0
    return n!
        Se repite multiplicandose por el valor anterior  4! = 4*3*2*1
    """ #documentacion
    print(f'El valor de n es {n}')
    if(n == 1):
        return 1
    
    return n  *  factorial(n-1)


n = int(input('Ingresa un entero al que quieras saber su factorial:  '))
print(f'El factorial de {n} es {factorial(n)}')
