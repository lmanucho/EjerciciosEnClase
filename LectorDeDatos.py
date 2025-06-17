# 1. Abrir el archivo productos.csv en modo lectura
try:
    with open("productos.csv", "r", encoding="utf-8") as archivo:
        # 2. Recorrer línea por línea
        for linea in archivo:
            # 3. Eliminar el salto de línea
            linea = linea.strip()

            # 4. Separar los datos por coma
            datos = linea.split(",")

            # Verificar que hay exactamente 3 elementos
            if len(datos) == 3:
                nombre, precio, cantidad = datos

                # 5. Imprimir la información de forma ordenada
                print(f"Producto: {nombre} | Precio: ${precio} | Stock: {cantidad} unidades")

except FileNotFoundError:
    print(" El archivo 'productos.csv' no fue encontrado.")