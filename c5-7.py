print(1+2)
#print(1/"cadena xd") #error de sintaxis
print(5*" 5cadenas")

#Objetos: abstacciones para modelar el mundo
my_none= None
print(type(my_none)) #Clase de tipo None

print(6 // 4)  #   // <-Trucar 

print( f'{"Hip"*3} hurra' )

rex ="LuchitoBailador"

print( len(rex) ) #longitud
print( rex[2] ) #cadena del indice
print( rex[2:] ) #apartir del indice 2 en adelante 
print( rex[:3] ) #hasta el 3
print(  rex[:-2] ) #todos excepto los ultimos
print(  rex[::3]) # salte de 3 en 3

print("Rex es un "+rex +"\n")     #concatenando
print(f'Rex es un {rex}\n'*10)   #interpolando

# Entradas---- siempre recibe cadenas
nombre = input("Cual es tu nombre xd?")
print(f'Tu nombre es {nombre} ')
print('Your name is', nombre)

num= int(input("Cual es tu edad compa?"))
print("Tu edad es ", num)
num = float(num)
print(type(num))

cadena = f'Hola, Tu nombre es: {nombre}'
print(cadena)
longitud = len(cadena)
print(f'La longitud de la cadena de salu2 es: {longitud}')
