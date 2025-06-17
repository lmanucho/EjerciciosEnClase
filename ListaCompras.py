#Programa de lista de compras 
# 1. Abrir el archivo en modo escritura para iniciar una nueva lista
archivo = open("compras.txt", "w")

# 2. Crear un bucle infinito
while True:
    # 3. Pedir al usuario que ingrese un producto
    producto = input("Ingresa un producto (o escribe 'fin' para terminar): ")
    
    # 4. Si el usuario escribe 'fin', salir del bucle
    if producto.lower() == "fin":
        break
    
    # 5. Escribir el producto en el archivo con un salto de línea
    archivo.write(producto + "\n")

# 6. Cerrar el archivo y notificar al usuario
archivo.close()
print(" Tu lista de compras ha sido guardada en 'compras.txt'.")
