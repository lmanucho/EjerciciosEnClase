from datetime import datetime

# Pedir al usuario el mensaje del evento
mensaje = input("Escribe el mensaje del evento: ")

# Obtener la fecha y hora actual
fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Crear la línea del log
linea_log = f"[{fecha_hora}] Evento: {mensaje}\n"

# Guardar en el archivo log.txt
with open("log.txt", "a") as archivo_log:
    archivo_log.write(linea_log)

print("Evento registrado correctamente.")