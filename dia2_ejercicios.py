"Ejercicio 1"

nombre = input("¿Cuál es tu nombre?")
edad = int(input("¿Cuántos años tenés?"))

años_para_100 = 100 - edad

if edad <= 100:
    print(f"Te faltan {años_para_100} años para llegar a 100")

"Ejercicio 2"

numero1 = float(input("¿Cual será el primer número? "))
numero2 = float(input("¿Cuál será el segundo? "))
operador = input("Operador (+, -, *, /): ")

if operador == "+":
    print(numero1 + numero2)
elif operador == "-":
    print(numero1 - numero2)
elif operador == "*":
    print(numero1 * numero2)
elif operador == "/":
    print(numero1 / numero2)

"Ejercicio 3"

import random
numero_secreto = random.randint(1, 10)
intento = int(input("Adiviná el número (1 al 10): "))

if intento > numero_secreto:
        print("¿Quizá un poco más abajo?")
elif intento < numero_secreto:
        print("¿Quizá un poco más arriba?")
else:
        print("¡Felicitaciones, lo lograste!")