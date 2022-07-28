from romanos2 import entero_a_romano

def test_3_es_igual_a_2_mas_1():
    assert 2 + 1 == 3

def test_entero_a_romano_1994():
    assert entero_a_romano(1994) == 'MCMXCIV'

def test_entero_a_romano_21():
    assert entero_a_romano(21) == 'XXI'