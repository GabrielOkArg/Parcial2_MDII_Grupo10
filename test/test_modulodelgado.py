# test/test_modulodelgado.py

from funciones.modulo_delgado import modulo_delgado

def test_modulodelgado():
    assert modulo_delgado(10, 3) == 1
    assert modulo_delgado(25, 5) == 0
    assert modulo_delgado(7, 0) is None
