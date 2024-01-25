
import time

# Función recursiva para calcular el número de Fibonacci
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Función con bucles para calcular el número de Fibonacci
def fibonacci_con_bucles(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# Función para medir el tiempo de ejecución
def medir_tiempo_ejecucion(funcion, n):
    inicio_tiempo = time.time()
    resultado = funcion(n)
    fin_tiempo = time.time()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    return resultado, tiempo_ejecucion

# Valores de n para los cuales calcularemos el tiempo de ejecución
valores_n = [1, 10, 20, 30, 40]

# Calcular y comparar el tiempo de ejecución para ambos enfoques
for n in valores_n:
    resultado_recursivo, tiempo_recursivo = medir_tiempo_ejecucion(fibonacci_recursivo, n)
    resultado_bucles, tiempo_bucles = medir_tiempo_ejecucion(fibonacci_con_bucles, n)

    print(f"n = {n}:")
    print(f"Resultado (Recursivo): {resultado_recursivo}, Tiempo: {tiempo_recursivo:.6f} segundos")
    print(f"Resultado (Bucles): {resultado_bucles}, Tiempo: {tiempo_bucles:.6f} segundos")
    print("---------")