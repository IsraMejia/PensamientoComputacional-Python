print('\nDiccionarios \tSecuencias de objetos mutables, llave -> valor')
print('El acceso a los datos son super eficientes a pesar de no tener un orden interno')
print('Pueden iterarse')

my_dict = { 
    'Isra' : 23 ,
    'Ana' : 21,
    'Rex' : 7,
}

#print(f'La edad de Isra es:{ my_dict['Isra'] }') #No se porque no jala asi
#Para que funcione tienes que usar el Metodo   .keys(), .values(), .items()
print(my_dict['Isra']) 
xD = my_dict.get('Juan' , 30) #Retorna el valor de juan, si no existe retorna 30
print(f'Juan = { xD}') #No se porque asi si deja, pero bueno jaja

my_dict['Rex'] = 20 #ReAsignacion
print(my_dict)

my_dict['Hector'] = 22 #Creacion de una nueva llave
#Si ya existiera lo que haria py3 es reasignacion
print(my_dict)

del my_dict['Hector'] #Borrar una llave
print(my_dict)


print('\t\t Iterar')#-----
for llave in my_dict.keys():
    print(f'Iterando llaves: {llave}')

for valor in my_dict.values():
    print(f'Iterando valor: {valor}')


print('\nIterando llave y valor')
for llave, valor  in my_dict.items():
    print(f'Los Items son: {llave} -> {valor}')



print('Para saber si un elemento esta dentro del diccionario podemos usar "in" ')
if('Isra' in my_dict):
    print('Si, Isra esta dentro')

if('Pancho' in my_dict):
    print('Si, Isra esta dentro')
