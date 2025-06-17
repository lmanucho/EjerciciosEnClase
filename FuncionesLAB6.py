def calpago(precio, cant):
    return precio * cant


def main():
    producto = input("Nombre del producto: ")
    precio = float(input("Precio c$: "))
    cantidad = float(input("cantidad:  "))
    total = calpago (precio, cantidad)
    print("producto: ", producto)
    
    print(f'\n{"Factura":30}')
    print(f'\n{"Precio":>10}', F'{"cantidad":>10}', f'{"Total":>10}')
    print(f"{precio:10} {cantidad:10} {total:10}")
main()