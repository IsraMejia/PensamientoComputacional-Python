print("\n\t Funciones y Abstraccion")
print('Las funciones nos permite leer el codigo facilmente, creando componentes reutilizables del codigo')

def suma(a , b):
    total = a + b
    return total


Suma = suma(2,3)
print(f'La suma es {Suma}')

def nombre_completo(nombre, apellido, inverso = False):
    if inverso:
        return print(f'{apellido} {nombre}')
    else :
        return print(f'{nombre} {apellido}')

nombre_completo('Isra', 'Mejia') #Sobrecarga
nombre_completo('Isra', 'Mejia' , inverso=True) #Sobrecarga y se hace la escritura en reversa
nombre_completo(apellido="Mejia", nombre='Israel') #Keyword para ejecutar la funcion