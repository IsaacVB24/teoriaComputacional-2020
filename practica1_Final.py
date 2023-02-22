
# author VICTORIA BENAVIDES ISAAC

s1 = []
s2 = []
# inciso a)
tam = float(input('\nIngrese tamaño de S1: '))
while tam < 3 or tam % 1 != 0:
    tam = float(input("Ingrese tamaño de S1, un entero mayor o igual a 3: "))
for i in range(int(tam)):
    s1.append(str(input("Ingrese el elemento " + str(i + 1) + " de S1: ")))
# inciso b)
tam = float(input("\nIngrese tamaño de S2: "))
while tam < 3 or tam % 1 != 0:
    tam = float(input("Ingrese tamaño de S2, un entero mayor o igual a 3: "))
for i in range(int(tam)):
    s2.append(str(input("Ingrese el elemento " + str(i + 1) + " de S2: ")))
while s1 == s2:
    s2 = []
    print('\n¡Error! El alfabeto S2 debe ser diferente a S1.')
    for i in range(int(tam)):
        s2.append(str(input("Ingrese el elemento " + str(i + 1) + " de S2: ")))


def imprimirAlfabetos(alfabeto):
    print(str(alfabeto[0]), end='')
    for x in range(0, len(alfabeto) - 1):
        print(', ' + str(alfabeto[x + 1]), end='')
    print('}')


print("\nEl alfabeto S1 es: {", end='')
imprimirAlfabetos(s1)
print("El alfabeto S2 es: {", end='')
imprimirAlfabetos(s2)


def validarCadena(cadena):
    lenCadena = len(cadena)
    for x in range(0, len(s1)):
        if s1[x] in cadena:
            lenCadena = lenCadena - len(s1[x])*cadena.count(s1[x])
    return lenCadena


# inciso c)
w1 = str(input("\nIngrese la cadena w1 con elementos de S1: "))
validarCadena(w1)
while validarCadena(w1) != 0:
    w1 = input('Debe ingresar una cadena w1 válida que contenga símbolos de S1: ')
    validarCadena(w1)

w2 = str(input("Ingrese la cadena w2 con elementos de S1: "))
validarCadena(w2)
while validarCadena(w2) != 0:
    w2 = input('Debe ingresar una cadena w2 válida que contenga símbolos de S1: ')
    validarCadena(w2)
# inciso d)
n = input('\nPara realizar la operación (w1w2)^n. Ingrese n: ')
while (float(n) % 1) != 0:
    print('El valor de n debe ser entero positivo o negativo. \nIngrese n: ')
    n = input()


def concatenarCadenas(cadena1, cadena2, potencia):
    concatenacion = cadena1 + cadena2
    print('w1w2 es: ' + concatenacion)
    if int(n) > 0:
        print('(w1w2)^' + n + ' es: ' + concatenacion * int(potencia))
    if int(n) == 0:
        print('(w1w2)^' + n + ' es: \'\'')
    if int(n) < 0:
        print('(w1w2)^-1 es: ' + concatenacion[::-1])
        print('(w1w2)^' + n + ' es: ' + (concatenacion[::-1]) * abs(int(potencia)))


print('La palabra w1 es: ' + w1)
print('La palabra w2 es: ' + w2)
concatenarCadenas(w1, w2, n)


def concurrencia(cadena, target):
    # repeticiones = re.findall(str(target), cadena)
    repeticiones = cadena.count(target)
    return repeticiones


# inciso e)
palabraTarget = input('\nPara realizar la operación |w1|_x escriba x, el cual, pertenece a S1: ')
while palabraTarget not in s1:
    palabraTarget = input(
        'Se introdujo una cadena no válida. \nPara realizar la operación |w1|_x escriba x, el cual, pertenece a S1: ')
print("La concurrencia del símbolo \' " + palabraTarget + ' \' en la palabra \' ' + w1 + ' \' es: ' + str(
    concurrencia(w1, palabraTarget)))


# inciso f)
def posiblesPreSufSub(palabra):
    print('Posibles prefijos de \' ' + palabra + ' \' = {\' \'', end='')
    for x in range(len(palabra)):
        temporalPal2 = palabra[0:int(x)+1]
        print(', ' + temporalPal2, end='')
    print('}')
    print('Posibles sufijos de \' ' + palabra + ' \' = {\' \'', end='')
    for x in range(len(palabra)):
        temporalPal2 = palabra[len(palabra)-int(x)-1:len(palabra)]
        print(', ' + temporalPal2, end='')
    print('}')
    print('Posibles subcadenas propias de \' ' + palabra + ' \' = {' + palabra[0], end='')
    for x in range(len(palabra)-1):
        temporalPal2 = palabra[1:int(x)+2]
        print(', ' + temporalPal2, end='')
        temporalPal2 = palabra[int(x):len(palabra)-1]
        print(', ' + temporalPal2, end='')
        pass
    print('}')


def preSufSub(palabra1, palabra2):
    if len(palabra2) < len(palabra1):
        print('\nLa palabra \' ' + palabra1 + ' \' es más pequeña que \' ' + palabra2 + ' \'. Por lo que no puede ser ni sufijo, prefijo ni subcadena de \' ' + palabra2 + ' \'.')
        posiblesPreSufSub(palabra2)
    elif palabra1 in palabra2:
        tempPalabra2 = palabra2
        if palabra2.find(palabra1) == 0:
            print('\nLa palabra \' ' + palabra1 + ' \' es prefijo de \' ' + palabra2 + ' \'.')
            tempPalabra2.removeprefix(palabra1)
        if palabra1 == palabra2[len(tempPalabra2) - len(palabra1):len(tempPalabra2)]:
            print('\nLa palabra \' ' + palabra1 + ' \' es sufijo de \' ' + palabra2 + ' \'.')
            tempPalabra2.removesuffix(palabra1)
        if tempPalabra2.find(palabra1) >= 0:
            print('\nUna subcadena \' ' + palabra1 + ' \' se encuentra en \' ' + palabra2 + ' \'.')
    else:
        print('\nLa palabra \' ' + palabra1 + ' \' no se encuentra dentro de \' ' + palabra2 + ' \', por lo que no puede ser ni sufijo, prefijo ni subcadena.')
        posiblesPreSufSub(palabra2)


preSufSub(w1, w2)


def concatenarAlfabetos(alf1, alf2):
    concatenacion = []
    for x in range(len(alf1)):
        for y in range(len(alf2)):
            nuevaPalabra = str(alf1[x] + alf2[y])
            concatenacion.append(nuevaPalabra)
    return concatenacion


# inciso g)
def s1N(numero):
    numero = int(numero)
    sTemporal = s1
    s1Invertido = []
    if numero < -1:
        for x in range(abs(numero)-1):
            sTemporal = concatenarAlfabetos(sTemporal, s1)
        print('S1^' + str(abs(numero)) + ' es: {', end='')
        imprimirAlfabetos(sTemporal)
        for y in range(len(sTemporal)):
            s1Invertido.append(sTemporal[y][::-1])
        print('S1^' + str(numero) + ' es: {', end='')
        imprimirAlfabetos(s1Invertido)
    if numero > 1:
        for x in range(numero-1):
            sTemporal = concatenarAlfabetos(sTemporal, s1)
        print('S1^' + str(numero) + ' es: {', end='')
        imprimirAlfabetos(sTemporal)
        pass
    if numero == -1 or numero == 1:
        print('S1^' + str(numero) + ' es: {', end='')
        imprimirAlfabetos(sTemporal)
    print('La longitud de S1^' + str(numero) + ' es: ' + str(len(sTemporal)))


nSolicitado = input('\nPara realizar la operación S1^n, ingrese n: ')
while float(nSolicitado) % 1 != 0:
    nSolicitado = input('El valor de \'n\' debe ser entero. Para realizar la operación S1^n, ingrese n: ')
s1N(nSolicitado)


# inciso h)
print('\nS1S2 = {', end='')
s1s2 = concatenarAlfabetos(s1, s2)
imprimirAlfabetos(s1s2)
# inciso i)
print('\nS1S2S1 = {', end='')
s1s2s1 = concatenarAlfabetos(s1s2, s1)
imprimirAlfabetos(s1s2s1)
