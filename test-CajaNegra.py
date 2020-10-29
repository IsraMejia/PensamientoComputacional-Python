print('\n\t Pruebas de Caja Negra')
print('Nos sirven para detectar bugs, esto cuando no conocemos la implementacion.')
print('Se basan en la especificacion de la funcion o del programa')
print('\tSe comprueban la entradas y salidas validas')
print('Son las bases de las pruebas unitarias (por modulos) y de integracion entre los modulos\n\n')


import unittest

def suma(num_1 , num_2):
    #pass #No hay nada mas xd => { }
    return abs(num_1) + num_2

class CajaNegraTest(unittest.TestCase):
    
    def test_suma_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)
        self.assertEqual( resultado, 15)
    
    def test_suma_negativos(self):
        num_1 = -10
        num_2 = -7
        
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, -17)


if __name__ == '__main__' : #Si es el modulo principal (el que estamos ejecutando ahorita)
    unittest.main() #Nos va a dar un error porque suma(n1 , n2) no definido



#Como vimos el test nos aviso de los posibles errores cuando hicimos el codigo, la idea aqui es aprender como
#Esbribimos nuestro codigo profesional apoyandonos de estas herramientas y no arrastrar errores que nos retrasen