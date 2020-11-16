import unittest
from romanos import *

class RomanosTest(unittest.TestCase):

    def test_single_simbol(self):

        # Con esta funcion comparamos el valor de la función con una solucion para ver si es igual
        self.assertEqual (simbolo_a_entero('M'), 1000)
        self.assertEqual (simbolo_a_entero('D'), 500)
        self.assertEqual (simbolo_a_entero('C'), 100)
        self.assertEqual (simbolo_a_entero('L'), 50)
        self.assertEqual (simbolo_a_entero('X'), 10)
        self.assertEqual (simbolo_a_entero('V'), 5)
        self.assertEqual (simbolo_a_entero('I'), 1)

        self.assertRaises (ValueError, simbolo_a_entero, 'Z')
        self.assertRaises (ValueError, simbolo_a_entero, 23)
        
    
    def test_sumas (self):
        self.assertEqual (romano_a_entero('MMM'), 3000)
        self.assertEqual (romano_a_entero ('CC'), 200)
        self.assertEqual (romano_a_entero ('XX'), 20)

        self.assertRaises (OverflowError, romano_a_entero, 'MMMM')
        self.assertRaises (OverflowError, romano_a_entero, 'VV')

    def test_restas (self):
       self.assertEqual (romano_a_entero('IV'), 4)

       self.assertRaises (ValueError, romano_a_entero, 'IC')

"""
MMMCMMM -> Error
IIX -> Error
"""

        


if __name__ == "__main__":
    unittest.main()