import os
os.system('cls' if os.name == 'nt' else 'clear')

palabra = input("Ingresa la palabra a evaluar: ")

palabra_invertida = palabra[::-1]

if palabra == palabra_invertida:
    print("La palabra ingresada es palíndromo.")
else:
    print("La palabra ingresada no es palíndromo.")

          