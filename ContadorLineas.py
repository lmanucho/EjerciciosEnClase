#Contador de lineas 
# 1. Solicitar al usuario el nombre del archivo
nombre = input("Ingresa el nombre del archivo : ")

# 2. Usar try...except para manejar FileNotFoundError
try:
    # 3. Abrir el archivo en modo lectura
    with open(nombre, "r", encoding="utf-8") as archivo:
        # 4. Leer todas las líneas en una lista
        lineas = archivo.readlines()
        
        # 5. Calcular y mostrar el número de líneas
        total = len(lineas)
        print(f"El archivo tiene {total} líneas.")

# 6. Si el archivo no se encuentra, mostrar mensaje de error amigable
except FileNotFoundError:
    print(" El archivo no fue encontrado. Asegúrate de que el nombre sea correcto.")