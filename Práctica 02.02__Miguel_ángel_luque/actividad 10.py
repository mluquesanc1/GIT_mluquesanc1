# Definir la contraseña
contrasena_correcta = ( "palotes" )

# Pedir al usuario que ingrese la contraseña
while True:
    contrasena_ingresada = input( "Por favor, ingresa contraseña: " )

# Verificar si la contraseña ingresada es correcta
    if contrasena_ingresada == contrasena_correcta:
        print( "¡Contraseña correcta! Acceso concedido." )
        break  
   
    else:
        print( "Contraseña incorrecta. Inténtalo de nuevo." )