def es_primo(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

for numero in range(1, 21):
    print(numero, es_primo(numero))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(1))
print(factorial(5))
print(factorial(10))

def contar_vocales(texto):
    diccionario = {'a': 0, 'e' : 0, 'i' : 0, 'o': 0, 'u' : 0}
    texto_minusculas = texto.lower()
    for letra in texto_minusculas:
        if letra in diccionario:
            diccionario[letra] = diccionario[letra] + 1
    return diccionario

print(contar_vocales("hola mundo"))
print(contar_vocales("Facundo aprende Python"))

a = 0
b = 1
for i in range(50):
    print (a)
    a, b = b, a + b


