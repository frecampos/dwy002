from django.test import TestCase
import unittest
from .models import MisionVision,Insumos
# Create your tests here.
class TestEjemplos(unittest.TestCase):

    def test_de_iguales(self):

        self.assertEqual('ii','ii')

    def test_no_esta_el_texto(self):

        self.assertFalse('hola' in ' este es un HOLA mundo')

    def grabar_insumo(self):
        valor = 0
        try:
            insumo = Insumos(
                nombre='JaJa', 
                precio=2500,
                descripcion='lubricante',
                stock=7
            )
            insumo.save()
            valor =1
        except:
            valor =0
        self.assertEqual(valor, 1)
        
if __name__ == "__main__":
    unittest.main()
