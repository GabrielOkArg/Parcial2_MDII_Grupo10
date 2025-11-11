import unittest
from funciones.sumaSilva import suma


def test_sumar():
 assert suma(3, 5) == 8
 assert suma(-2, 2) == 0