# tests/test_potenciachavez.py

# Importante: Le decimos al test dónde encontrar tu función
from funciones.potenciaChavez import potencia_Chavez

# Creamos el test para esa función
def test_potencia_Chavez():
  assert potencia_Chavez(2, 3) == 8
  assert potencia_Chavez(5, 0) == 1
  assert potencia_Chavez(3, 1) == 3