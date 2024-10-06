import ejercicio1


def test_calcular_temperatura():
    assert ejercicio1.calcular_temperatura(0) == 40.00
    assert ejercicio1.calcular_temperatura(40) == 50.00
    assert ejercicio1.calcular_temperatura(160) == 80.00
    print("Todos los casos de prueba pasaron exitosamente.")



