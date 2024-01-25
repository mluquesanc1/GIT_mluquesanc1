# Inicializar una variable para almacenar la entrada del usuario
entrada = ""

# Repetir el eco hasta que el usuario escriba "salir"
while entrada.lower() != "salir":
    entrada = input( "Introduce algo o escribe 'salir' para terminar): " )
    print(entrada)

print( "¡Hasta luego!" )