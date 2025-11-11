from funciones.restaortiz import restar

def test_restar():
    """Prueba que la función restar funcione correctamente."""
    assert restar(5, 3) == 2
    assert restar(10, 5) == 5
    assert restar(0, 7) == -7