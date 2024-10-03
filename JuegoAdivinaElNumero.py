from random import randint

intentos = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un numero ntre 1 y 100\nTienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cual es el numero?: "))
    intentos += 1

    if estimado < numero_secreto:
        print("mi numero es mas alto")

    if estimado > numero_secreto:
        print("mi numero es mas bajo")

    if estimado == numero_secreto:
        print(f"Felicitaciones {nombre} ! has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"lo siento, se han agotado los intentos, el numero secreto era {numero_secreto}")

