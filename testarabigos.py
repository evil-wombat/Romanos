import unittest
from romanos import *

class ArabigosTest(unittest.TestCase):

    def test_descomponer(self):
        self.assertEqual(descomponer(1987), [1, 9, 8, 7])
       
    def test_convertir_987 (self):
        self.assertEqual (convertir([9, 8, 7]), 'CMLXXXVII')
             
    def test_arabigo_a_romano (self):
        self.assertEqual (arabigo_a_romano (1987), 'MCMLXXXVII')
        self.assertRaises (SyntaxError, arabigo_a_romano (1987.6))
        
          






if __name__ == "__main__":
    unittest.main()