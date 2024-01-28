import re

# Expresión regular corregida
pattern = re.compile(r'(\+|-)?\d+\.\d+')

# Lista de cadenas de prueba
test_strings = ['-20.43', '0.3216', '329.', '217.92', '+2019', '+.762', '-.4555']

# Prueba las cadenas
for test in test_strings:
    if pattern.fullmatch(test):
        print(f"'{test}' coincide con la expresión regular")
    else:
        print(f"'{test}' no coincide con la expresión regular")
