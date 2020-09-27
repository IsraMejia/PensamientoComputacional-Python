print("\n\tComputo Exahustivo, Aproximacion de soluciones")
print("\n Calculo de una raiz cuadrada aproximada")

objetivo = int(input("Ingrese el numero a calcular su raiz: "))
epsilon = float(input('Agrega el valor de epsilon, se recomienda 0.01: '))
paso = epsilon**2
respuesta= 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo) , respuesta) #Para ver que es lo que pasa
    respuesta += paso

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada del {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es: {respuesta}')

