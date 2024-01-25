
# Solicitar al usuario un nmero entero
altura = int(input( "Por favor, ingresa un número entero: " ))


# Verificar que la altura sea mayor que cero
if altura <= 0:
    print( "La altura debe ser un número entero positivo." )
else:
   
# Iterar a través de las filas para imprimir el triángulo
    for i in range(1, altura + 1):
        # Imprimir '*' en cada columna de la fila actual
        for j in range(i):
            print('*', end=' ')

# Ir a la siguiente línea para la siguiente fila
        print()