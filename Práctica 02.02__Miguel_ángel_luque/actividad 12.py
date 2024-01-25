# Solicitar una frase y una letra
frase = input( " ingresa una frase: " )
letra = input( " ingresa una letra para contar: " )

# Inicializar una variable para contar la cantidad de veces que aparece la letra
contador = 0

# Iterar a trabes de la frase para contar la letra
for caracter in frase:
    if caracter == letra:
        contador += 1

# Mostrar el resultado
print(f"La letra '{letra}' aparece {contador} veces en la frase." )