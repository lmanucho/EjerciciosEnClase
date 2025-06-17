# Programa que lee un archivo "Poema.txt" y lo imprime línea a línea

with open("Poema.txt", "r") as poema:
    for linea in poema:
        print(linea, end='')  # 'end' evita el doble salto de línea
