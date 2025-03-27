n = int(input("Introduce un número entero positivo: "))
if n <= 0:
    print("Por favor, ingresa un número entero positivo.")
else:
    fibonacci = [0, 1] + [0]*(n - 2) 
    
    for i in range(2, n):
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]   
    print(f"Los primeros {n} números de la secuencia Fibonacci son: {fibonacci}")
