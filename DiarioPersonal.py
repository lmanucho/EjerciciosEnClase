#Diario Simple 
from datetime import datetime

entrada = input("Escribe tu entrada de hoy: ")

fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("diario.txt", "a") as archivo:
    archivo.write(f"\n[{fecha_hora}]\n{entrada}\n")

print("Tu entrada ha sido guardada en 'diario.txt'.")