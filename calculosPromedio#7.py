#Calculo promedio desde un archivo 
# Abrimos el archivo de entrada
with open("notas.csv", "r") as archivo_entrada:
    lineas = archivo_entrada.readlines()

# Creamos o abrimos el archivo de salida
with open("promedios.txt", "w") as archivo_salida:
    for linea in lineas:
        partes = linea.strip().split(",")
        nombre = partes[0]
        calificaciones = list(map(float, partes[1:]))
        promedio = sum(calificaciones) / len(calificaciones)
        archivo_salida.write(f"{nombre}: {promedio:.2f}\n")

print("Promedios calculados y guardados en 'promedios.txt'.")