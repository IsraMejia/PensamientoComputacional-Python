print('\nSecuencias de objetos mutables')

my_list = [1, 2, 3]
print('\n my_list = [1, 2, 3]  Para hacer uso de ellas se meten los valores en corchetes \n')
print(my_list[0])
print(f'Podemos usar la notacion de slices my_list[1:] para ir del indice 1 al final')
print(my_list[1:])

print('\t\tAlgunos metodos')
print('append(i) nos sirve para agregar al final de la lista un elemento')
my_list.append('xD')
print(my_list[0:])

print('Podemos reasignar usando el indice')
my_list[1] = 0.22
print(my_list[0:])

print(' .pop()  sacamos de la lista y nos puede retornar el ultimo elemento')
print(my_list.pop())
print(my_list[0:])

print('Tambien podemos iterar usando los elementos de las listas')
for element in my_list : 
  print(f'Iterando, voy en: {element}')

a = [1, 2, 3]
b= a #Realmente apuntamos con las variables a la misma ubicacion de memoria donde se guardo
#la primera lista [1, 2, 3]

print(f' ID de a={id(a)}   y  b={id(b)} ')

print('OJO cuidaho xD, si hacemos una lista de listas con c=[a, b] NO guardamos dos listas ')
c=[a, b]
print(c)
a.append(5)
print('Se hacen los cambios sobre la lista y estos los podemos ver usando los apuntadores de ')
print(' nuestras variables -> a.append(5)')
print(c)

print('\n\nPara evitar estos errores vamos a CLONAR las listas')
print('\tPodemos usar los slice o bien la funcion list')
d = [1, 2, 3]
e= d
g = list(d)  #Clonamos la lista y se la asignamos a g
print(f' ID de d={id(d)} ,  b={id(e)} , g={id(g)} ')
print(g)
print('\tOtra forma mas logica para hacer esto es usando slices ')
print('e = d[::] del inicio al fin de uno a uno se pasan los elementos de la lista a e')
e = d[::]
print(f'e = {e} \t ID={id(e)}')
print('\n Conclusioon, siempre clona la lista')


print('\n\t\tList Comprehension')
print('Nos permiten aplicar operaciones/filtrar a los valores de la secuencia de objetos')
print('Generamos operaciones a los elementos de las listas')
mi_lista = list(range(100)) #Creamos una lista con enteros del 0 al 99 E N
print(f'\nLista generanda usando rangos=\n {mi_lista} \n')

doble = [ i*2 for i in mi_lista] #Duplicamos los valores y los asignamos a doble
print(f'Generando la lista doblando el valor de sus elementos, doble= \n {doble}  \n')

pares = [i for i in mi_lista  if i%2 == 0] 
#Se le asigna el elemento i solo si es par a pares
print(f'Generando la lista pares = \n {pares}  \n')

