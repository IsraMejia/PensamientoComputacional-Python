print('-----------TUPLAS')
print('Secuencia inmutables de objetos, pueden ser de distintos tipos y \n pueden retornar varios valores')

my_tuple =()
print( f'my tuple es de tipo: {type(my_tuple)}' )

my_tuple = (2020 , 'LackersWin', True)
print(f'El indice 0 es {my_tuple[0]}')

# my_tuple[2] = False  #Nos marca error porque no se pueden reasignar

my_tupla = (1,) #Tiene que llevar la coma si no python lo toma como un entero
print( f'my tupla es de tipo: {type(my_tupla)}' )

otra_tupla = (2,3,4)

my_tupla += otra_tupla #Realmente se crea una nueva tupla que une la anterior con otra_tupla
#Se reasigna el objeto, no se muta o cambian sus elementos internos

print(f'El nuevo valor de my_tupla es :  {my_tupla}')

#Desempaquetando la tupla
x, y, z = otra_tupla
print(f'Desempaquetando los valores de otra_tupla: {otra_tupla}')
print(f'x = {x} , y = {y} , z = {z}')

print('\nAhora vamos a retornar varios valores de una funcion')
def coordenadas():
    return (5 ,4) #Retorna esta tupla

coordenada = coordenadas()
print(f'la coordenada es ({coordenada}) \n si las desempaquetamos')
x , y = coordenadas()
print(f'x,y = {x} , {y}')


