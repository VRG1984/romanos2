import pytest

from romanos2 import entero_a_romano, romano_a_entero, RomanNumberError

def test_3_es_igual_a_2_mas_1():
    assert 2 + 1 == 3

def test_entero_a_romano_1994():
    assert entero_a_romano(1994) == 'MCMXCIV'

def test_entero_a_romano_21():
    assert entero_a_romano(21) == 'XXI'

def test_romano_a_entero_ordenados():
    assert romano_a_entero("I") == 1
    assert romano_a_entero("MDCCXIII") == 1713

def test_romano_a_entero_mas_de_tres():
    with pytest.raises(RomanNumberError) as exceptionInfo:
        romano_a_entero('LIIII')
    assert str(exceptionInfo.value) == "No se pueden dar más de tres repeticiones"

def test_romano_a_entero_resta_si_soy_mayor_que_anterior():
    assert romano_a_entero("IV") == 4

