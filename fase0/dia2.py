nombre = "Facundo"
edad = 19
altura = 1.74
tiene_python = True

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(tiene_python))

a = 10
b = 3

"Operadores"
print(a + b)   # suma → 13
print(a - b)   # resta → 7
print(a * b)   # multiplicación → 30
print(a / b)   # división → 3.333...
print(a // b)  # división entera → 3 (descarta los decimales)
print(a % b)   # módulo → 1 (el resto de dividir 10 entre 3)
print(a ** b)  # potencia → 1000 (10 elevado a la 3)

nombre = "Facundo"
edad = 19

print(f"Hola, me llamo {nombre} y tengo {edad} años.")
print(f"En 10 años voy a tener {edad + 10} años.")
print(f"El doble de mi edad es {edad * 2}.")

edad = 19

if edad >= 18:
    print("Sos mayor de edad.")
elif edad >= 13:
    print("Sos adolescente.")
else:
    print("Sos menor de 13.")

"Operadores de Comparación"
print(10 == 10)   # igual → True
print(10 != 5)    # distinto → True
print(10 > 5)     # mayor → True
print(10 < 5)     # menor → False
print(10 >= 10)   # mayor o igual → True
print(10 <= 9)    # menor o igual → False

edad = 19
tiene_trabajo = True

if edad >= 18 and tiene_trabajo:
    print("Podés alquilar un departamento.")

if edad < 13 or edad > 65:
    print("Tarifa especial.")