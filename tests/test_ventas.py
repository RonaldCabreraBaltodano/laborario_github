import unittest

from ventas import calcular_total


class CalcularTotalTest(unittest.TestCase):
    def test_descuento_de_diez_por_ciento(self):
        self.assertEqual(calcular_total(10000, 10), 9000)

    def test_sin_descuento(self):
        self.assertEqual(calcular_total(10000, 0), 10000)

    def test_redondea_medio_centavo_hacia_arriba(self):
        self.assertEqual(calcular_total(1, 50), 1)

    def test_rechaza_descuento_mayor_a_cien(self):
        with self.assertRaises(ValueError):
            calcular_total(10000, 101)