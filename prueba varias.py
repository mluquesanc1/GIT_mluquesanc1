# Solicitar al usuario su peso en kg
peso = float(input("Por favor, ingresa cual  tu peso en kg: "))


# Solicitar al usuario su estatura en metros
estatura = float(input("Por favor, ingresa cual es tu estatura en metros: "))


# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)


# Redondear el IMC a dos decimales
imc_redondeado = round(imc, 2)


# Mostrar los resultados en pantalla
print(f"Tu índice de masa corporal es" {imc_redondeado})