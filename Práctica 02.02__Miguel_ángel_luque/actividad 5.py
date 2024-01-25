#solicitut nombre y sexo
Nombre = input( "cual es tu nombre: ")

sexo = input( "cual es tu sexo ( m para mujer y h para hombre): " )

#determina la casa

casa = "" 

if (sexo == "M" and Nombre < "M") or (sexo == "H" and Nombre > "N"):
    casa = "Gryffindor"

else:casa = "Slytherin"

# Mostrar la casa asignada
print(f"Tu casa en Hogwarts es: {casa}")