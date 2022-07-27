from romanos2 import entero_a_romano

def test_3_es_igual_a_2_mas_1():
    assert 2 + 1 == 3

def test_error_si_emtero_mayor_de_3999():
    assert entero_a_entero(1994) == 'MCMXCIV'