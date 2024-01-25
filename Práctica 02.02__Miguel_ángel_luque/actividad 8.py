



# Iterar a través de los numeros del 1 al 10
for i in range(1, 11):
    
# Imprimir en el encabezado de la tabla para el número actual
    print(f"Tabla de multiplicar del {i}:")

# Iterar a través de los numeros del 1 al 10 y calcular los productos
    for j in range(1, 11):
        producto = i * j
    
# Imprimir la multiplicación en el formato "numero1 x número2 = producto"
        print(f"{i} x {j} = {producto}")

# Imprimir  límea en blanco para separar las tabas
    print()
