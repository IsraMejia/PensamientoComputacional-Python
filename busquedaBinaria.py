print("\n\t Busqueda Binaria")
print('El antecedente de QuikSort, aqui solo se busca, no se ordena')

objetivo = int(input('Escoge un numero: '))
epsilon = 0.01 #margen de error
bajo = 0.0
alto= max(1.0 , objetivo) #Retorna el mayor valor entre 1.0 y objetivo
#El valor minimo sera 1.0 -> No hay negativos
respuesta = (alto + bajo) /2

while abs(respuesta **2 - objetivo) >= epsilon :
    print(f'\n bajo = {bajo} ,  alto= {alto} , resp = {respuesta}') #Para ver que hace
    if respuesta**2 < objetivo : 
        bajo = respuesta #nos vamos a la izquierda
    else:
        alto = respuesta #nos vamos a la derecha
    
    respuesta =  (alto + bajo) / 2 # Se parte a la mitad la busqueda

print(f'\nLa raiz cuadrada del {objetivo} es {respuesta} \n')