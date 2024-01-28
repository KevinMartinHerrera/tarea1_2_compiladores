""" Realice una expresión regular de todas las cadenas de con símbolos 0 y 1,
que primero tenga lo símbolos 1 ‘S con longitud impar y después aparezcan
los 0 ‘s con longitud par. Ejemplo de estas cadenas son: 100, 10000,
1000000, 11100, 1110000, 111110000, … """


import re


pattern = re.compile(r'^1(11)*(00)*$')


test_strings = ['100', '10000', '1000000', '11100', '1110000', '111110000', '1010', '1111', '000', '1110']


for test in test_strings:
    if pattern.fullmatch(test):
        print(f"'{test}' coincide con la expresión regular")
    else:
        print(f"'{test}' no coincide con la expresión regular")
