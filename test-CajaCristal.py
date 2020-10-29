import unittest

print('\n\tPruebas de Caja de Cristal')
print('Se basan en el flujo del programa , revisan los caminos en la funcion') 
print('Como las ramificicaicones, bucles y recursion ')
print('Util en el Regresion Testing, cuando ya esta en produccion el producto')
print('y tenemos que encontrar donde esta el bug \n\n')

"""En el caso de un if se prueba la condicion cuado es valida y sus elif o else

en un Loop tenemos que probar cuando entremos al loop, cuando no lo hagamos y 
en donde entremos mas de una vez al loop

con los while se prueba donde la condicion de entrada  sea falsa y una en la que 
se compueben los estados internos del while 

Si hay excepciones, igual se tienen que probar
"""

def es_mayor_de_edad(edad):
    if edad >= 18 :
        return True
    else:
        return False



class PruebaCristalTest( unittest.TestCase):
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, True)
    


    def test_es_menor_de_edad(self):
        edad = 17

        resultado = es_mayor_de_edad(edad)
        self.assertEqual(resultado, False)
    


if __name__ == '__main__':
    unittest.main()


