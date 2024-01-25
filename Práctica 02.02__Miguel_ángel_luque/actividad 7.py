# pide el nuemro entero

altura = int(input(" introduce un numero entero "))

#verificacion que es numero es entero
if altura <= 0:
    print("La altura no debe de ser unero Zero.")
else:
   
 # Iterar a través de las filas para imprimir el triángulo
    for i in range(1, altura + 1):
        # Imprimir '*' en cada columna de la fila actual
        for j in range(i):
            print('*', end=' ')
        
        # Ir a la siguiente línea para la siguiente fila
        
        print()




