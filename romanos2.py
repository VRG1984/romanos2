componentes = {
    1000: 'M', 2000: 'MM', 3000: 'MMM', 
    100: 'C', 200: 'CC', 300: 'CCC',
    400: 'CD', 500: 'D', 600: 'DC',
    700: 'DCC', 800: 'DCCC', 900: 'CM',
    10: 'X', 20: 'XX', 30: 'XXX',
    40: 'XL', 50: 'L', 60: 'LX',
    70: 'LXX', 80: 'LXXX', 90: 'XC',
    1: 'I', 2: 'II', 3: 'III',
    4: 'IV', 5: 'V', 6: 'VI',
    7: 'VII', 8: 'VIII', 9: 'IX'
}

simbolos_romanos  = {
    'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1, '': 0
}

class RomanNumberError(Exception):
    pass

def entero_a_romano(valor):
    valor = str(valor)
    romano = ""
    ix = 0
    
    for caracter in valor:    
        caracter = caracter + ("0" * int(len(valor) - ix - 1))
        romano += componentes[int(caracter)]
        ix += 1
    
    return romano

def romano_a_entero(romano):
    """numero_romano = 0
    repeticiones = 1
    for pos, caracter in enumerate(romano):
        if pos > 0 and caracter == romano[pos - 1]:
            repeticiones += 1
        else:
            repeticiones = 1
    
        if repeticiones < 4:
            numero_romano += simbolos_romanos[caracter]
        else:
            raise RomanNumberError("No se pueden dar más de tres repeticiones")
    
    return numero_romano"""

    numero_romano = 0
    repeticiones = 1
    caracter_anterior = ""
    
    for caracter in romano:
        if caracter == caracter_anterior:
            repeticiones += 1
    
        else:
            repeticiones = 1
    
        if repeticiones > 3:
            raise RomanNumberError("No se pueden dar más de tres repeticiones")
        

        if simbolos_romanos[caracter] > simbolos_romanos[caracter_anterior]:
            numero_romano -= simbolos_romanos[caracter_anterior] * 2
            
        numero_romano += simbolos_romanos[caracter]
        caracter_anterior = caracter
    
    return numero_romano


        

    
    
    for caracter in romano:
        numero_romano += simbolos_romanos[caracter]
    return numero_romano







