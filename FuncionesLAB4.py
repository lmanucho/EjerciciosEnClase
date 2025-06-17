#Funcion que permita obtener el producto de 2 numeros 

def producto (num1, num2):
    return num1 + num2

#Multiplicar 2#

numero1 = int(input("Digite un numero:  "))
numero2 = int(input("Digite otro numero: "))
resp = producto(numero1, numero2)
print(numero1, " * ",  numero2,  "=", resp)


#Obtener la tabla de multiplicar de un numero
num = int(input("escribe un numero:  "))
for i in range(1, 13):
    r = producto(num, i )
    print(num," * ", i , " = ", r)