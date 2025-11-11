import unittest
from funciones.divisionruizgonzalo import dividir

def test_dividir():
    # Estas líneas deben estar indentadas
    assert dividir(10, 2) == 5
    assert dividir(5, 0) is None