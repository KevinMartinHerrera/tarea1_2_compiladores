"""
Realice una expresión regular de todas las cadenas con símbolos a y b, que
terminan con el sufijo abb. Ejemplo de estas cadenas son: abb, aabb, babb,
aaabb, ababb, baabb, bbabb, … 
"""
import re


pattern = re.compile(r'[ab]*abb')


test_strings = ['abb', 'aabb', 'babb', 'aaabb', 'ababb', 'baabb', 'bbabb', 'abc', 'aabbc', 'bba']

for test in test_strings:
    if pattern.fullmatch(test):
        print(f"'{test}' coincide con la expresión regular")
    else:
        print(f"'{test}' no coincide con la expresión regular")
