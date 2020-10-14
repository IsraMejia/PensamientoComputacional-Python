print('\n\nSecuencias de enteros con un Comienzo, Fin y Pasos . Es una EstDato')
print('Son inmutables y muuy eficientes con la memoria')

#range( comienzo, fin, pasos)

my_range = range(1,5) #El intervalo es cerrado abierto ->No inclusivo en el Final
#Se repetira iniciando uno y terminara en el entero anterior al Fin (1,2,3,4) = En intervalos matematicos [1,5)
print('\n No inclusivo en el Final. Se repetira iniciando uno y terminara en el entero anterior al Fin\n (1,2,3,4) = En intervalos matematicos [1,5) \n')
print(type(my_range))

for i in my_range:
  print(f'Iteracion {i}')

mi_rango = range(0,7,2)
otro_rango = range(0,8,2)
print('\nmi_rango = range(0,7,2)     otro_rango = range(0,8,2)')

if (mi_rango == otro_rango): #La secuencia de enteros es la misma?
  print('Son iguales mi_rango == otro_rango')

for i in mi_rango:
  print(f'Iteracion  mi_rango {i}') 


print('\n\n')
for i in otro_rango:
  print(f'Iteracion  otro_rango {i}') 


print('\nPara saber si realmente son iguales los objetos podemos usar ')
print(f'sus ID, mi_rango = {id(mi_rango)}  y otro_rango={id(otro_rango)}')
print('Como vemos son distintos, para realmente comparar los objetos usamos (is)')
print(f'mi_rango is otro_rango -> {mi_rango is otro_rango} ')

print('Esto es muy util porque puedes saber todos los pares del 0 al 100 con solo dos linea de codigo')
for i in range(0, 101 ,2):
  print(i)

print('Esto es muy util porque puedes saber todos los imppares del 0 al 100 con solo dos linea de codigo')
for i in range(0, 100 ,2):
  print(i+1)

 