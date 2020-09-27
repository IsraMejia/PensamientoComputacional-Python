#Programas Ramificados
"""
print("\nAqui se ve estructuras de control xd \n")
nombre1 = input("Dime el nombre del primer usuario: ")
num1 = int(input("\tAhora dime su edad: "))

nombre2 = input("Dime el nombre del segundo usuario: ")
num2 = int(input("\tAhora dime su edad: "))

if num1>num2 : 
    print(f'El primer usuario({nombre1}) es mayor  que el primero ({nombre2})')
elif num1<num2:
    print(f'El segundo usuario({nombre2})  es mayor que el primero ({nombre1})')
else:
    print("Las edades de los usuarios son iguales")
"""
#Iteraciones
contador=2
while contador<11:
    print(contador)
    contador += 1

print("\n\n Valores de x")
x= 0.0
for i in range(10):
    x +=0.1
    print(x)

if x == 1.0:
    print(f'x ={x}')
else:
    print(f'x != {x}')
