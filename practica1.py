import random

# author VICTORIA BENAVIDES ISAAC

s = []
# inciso a)
tam = float(input('\nIngrese tamaño de S1: '))
while tam < 3 or tam % 1 != 0:
    tam = float(input("Ingrese tamaño de S1, un entero mayor o igual a 3: "))
for i in range(int(tam)):
    s.append(str(input("Ingrese el elemento " + str(i + 1) + " de S1: ")))

# inciso b)
np = float(input("\nIngrese el número de elementos a generar para L1 y L2: "))
while np <= 0 or np % 1 != 0:
    np = float(input("El número a ingresar debe ser entero positivo mayor a 0. \nIngrese el número de elementos a generar para L1 y L2: "))
l = float(input("Ingrese la longitud que tendrá cada palabra de ambos lenguajes: "))
while l <= 0 or l % 1 != 0:
    l = float(input("El número a ingresar debe ser entero positivo mayor a 0. \nIngrese el número de elementos a generar para L1 y L2: "))
L1 = []
L2 = []


def imprimirAlfabetos(alfabeto):
    print(str(alfabeto[0]), end='')
    for x in range(0, len(alfabeto) - 1):
        print(' , ' + str(alfabeto[x + 1]), end='')
    print('}')


def generarLenguaje(lenguaje, alfabeto):
    for x in range(int(np)):
        palabra = ''
        for y in range(int(l)):
            palabra = palabra + random.choice(alfabeto)
        lenguaje.append(palabra)


print("El lenguaje L1 generado es: {", end='')
generarLenguaje(L1, s)
imprimirAlfabetos(L1)
print("El lenguaje L2 generado es: {", end='')
generarLenguaje(L2, s)
imprimirAlfabetos(L2)

# inciso c)
LU = L1 + L2
print("\nGenerando la unión de L1 y L2 ...")
print("LU = {", end='')
imprimirAlfabetos(LU)
print("La longitud de LU es: " + str(len(LU)))

# inciso d)


def LC(lenguaje1, lenguaje2):
    concatenacion = []
    for x in range(len(lenguaje1)):
        for y in range(len(lenguaje2)):
            nuevaPalabra = str(lenguaje1[x] + lenguaje2[y])
            concatenacion.append(nuevaPalabra)
    return concatenacion


print('\nGenerando la concatenación de L1 y L2...')
print('LC = {', end='')
imprimirAlfabetos(LC(L1, L2))

# inciso e)


def diferencia(lenguaje1, lenguaje2):
    repeticiones = []
    lenguajeTemporal = []
    for d in range(len(lenguaje1)):
        lenguajeTemporal.append(lenguaje1[d])
    for x in range(len(lenguaje2)-1):
        if lenguaje2[x] in lenguajeTemporal:
            lenguajeTemporal.remove(str(lenguaje2[x]))
            repeticiones.append(lenguaje2[x])
    print('LD = {', end='')
    imprimirAlfabetos(lenguajeTemporal)
    print('Las palabras que están en ambos lenguajes son: {', end='')
    if len(repeticiones) == 0:
        print(' }')
    else:
        imprimirAlfabetos(repeticiones)


print('\nGenerando la diferencia entre L1 y L2...')
print('L1 = {', end='')
imprimirAlfabetos(L1)
print('L2 = {', end='')
imprimirAlfabetos(L2)
diferencia(L1, L2)
print('\nGenerando la diferencia entre L2 y L1...')
print('L2 = {', end='')
imprimirAlfabetos(L2)
print('L1 = {', end='')
imprimirAlfabetos(L1)
diferencia(L2, L1)

# inciso f)
selLen = float(input('\nIngrese \'1\' para hacer la operación LP con el lenguaje 1, o cualquier otro número para el lenguaje 2: '))
while selLen % 1 != 0:
    selLen = float(input('El número ingresado debe ser entero.\nIngrese \'1\' para hacer la operación LP con el lenguaje 1, o cualquier otro número para el lenguaje 2: '))
pot = float(input('Ingrese la potencia a la cuál se elevará el lenguaje (debe ser en rango de enteros de [-5, 5]: '))
while pot % 1 != 0 or pot < -5 or pot > 5:
    pot = float(input('No válido.\nIngrese la potencia a la cuál se elevará el lenguaje (debe ser en rango de enteros de [-5, 5]: '))


def concatenar(lenguaje1, lenguaje2):
    concatenacion = []
    for x in range(len(lenguaje1)):
        for y in range(len(lenguaje2)):
            nuevaPalabra = str(lenguaje1[x] + lenguaje2[y])
            concatenacion.append(nuevaPalabra)
    return concatenacion


def LP(lenguaje, numero):
    numero = int(numero)
    lTemporal = lenguaje
    lInvertido = []
    if numero < -1:
        for x in range(abs(numero)-1):
            lTemporal = concatenar(lTemporal, lenguaje)
        print('L^' + str(abs(numero)) + ' es: {', end='')
        imprimirAlfabetos(lTemporal)
        for y in range(len(lTemporal)):
            lInvertido.append(lTemporal[y][::-1])
        print('L^' + str(numero) + ' es: {', end='')
        imprimirAlfabetos(lInvertido)
    if numero > 1:
        for x in range(numero-1):
            lTemporal = concatenar(lTemporal, lenguaje)
        print('L^' + str(numero) + ' es: {', end='')
        imprimirAlfabetos(lTemporal)
    if numero == 1:
        print('L^' + str(numero) + ' es: {', end='')
        imprimirAlfabetos(lTemporal)
    if numero == -1:
        print('L^1 es: {', end='')
        imprimirAlfabetos(lTemporal)
        for y in range(len(lTemporal)):
            lInvertido.append(lTemporal[y][::-1])
        print('L^' + str(numero) + ' es: {', end='')
        imprimirAlfabetos(lInvertido)
    if numero == 0:
        print('L^0 es : {}')
        lTemporal = ''
    print('La longitud de L^' + str(numero) + ' es: ' + str(len(lTemporal)))


if selLen == 1:
    print('Generando la potencia ' + str(int(pot)) + ' del lenguaje 1 ...')
    print('L1 = {', end='')
    imprimirAlfabetos(L1)
    LP(L1, pot)
    pass
else:
    print('Generando la potencia ' + str(int(pot)) + ' del lenguaje 2 ...')
    print('L2 = {', end='')
    imprimirAlfabetos(L2)
    LP(L2, pot)

# inciso g)
posibilidad = 'ABCDEFGHIJKLMNOPQRSTUVXYZ0123456789'
estados = [
    "Aguascalientes",
    "Baja California Norte",
    "Baja california Sur",
    'Campeche',
    'Chiapas',
    'Chihuahua',
    'Ciudad de México',
    'Coahuila',
    'Colima',
    'Durango',
    'Estado de México',
    'Guanajuato',
    'Guerrero',
    'Hidalgo',
    'Jalisco',
    'Michoacán',
    'Morelos',
    'Nayarit',
    'Nuevo León',
    'Oaxaca',
    'Puebla',
    'Querétaro',
    'Quintana Roo',
    'San Luis Potosí',
    'Sinaloa',
    'Sonora',
    'Tabasco',
    'Tamaulipas',
    'Tlaxcala',
    'Veracruz',
    'Yucatán',
    'Zacatecas'
]


def crearPlacas():
    apartado = ''
    placaFinal = ''
    for a in range(3):
        apartado = apartado + random.choice(posibilidad)
        placaFinal = apartado + '-'
    for a in range(2):
        apartado = ''
        apartado = apartado + random.choice(posibilidad)
        placaFinal = placaFinal + apartado
    placaFinal += '-'
    for a in range(3):
        apartado = ''
        apartado = apartado + random.choice(posibilidad)
        placaFinal = placaFinal + apartado
    return placaFinal


totalPlacas = []
print('\n\nPara lo siguiente, se generará una placa de cualquier estado de la república con el siguiente formato: AAA-AA-AA')
print('Donde cada A puede ser cualquier dígito aleatorio o letra del abecedario aleatoria.\nA continuación se muestran los estados:\n')
for num in range(len(estados)):
    print(str(num+1) + '.- ' + estados[num])
nPlacas = float(input('\n¿Cuántas placas desea tramitar? '))
while nPlacas % 1 != 0 or nPlacas < 0:
    nPlacas = float(input('Debe ingresar un número entero positivo: '))
if nPlacas == 0:
    print('\nHasta luego!')
else:
    edo = float(input('Ingrese el número del Estado al que corresponderán las ' + str(int(nPlacas)) + ' placas: '))
    while edo % 1 != 0 or edo not in range(1, 33):
        edo = float(input('Error! Debe ser un número entero del 1 al 32.\nIngrese el número del Estado al que corresponderán las ' + str(int(nPlacas)) + ' placas: '))
    print('\nGenerando ' + str(int(nPlacas)) + ' placas para ' + estados[int(edo)-1] + ' ...\n')
    for g in range(int(nPlacas)):
        nuevaPlaca = crearPlacas()
        totalPlacas.append(nuevaPlaca)
        if nuevaPlaca in totalPlacas:
            totalPlacas.remove(nuevaPlaca)
            totalPlacas.append(nuevaPlaca)
    print('Las placas generadas para ' + estados[int(edo)-1] + ' son:')
    for imp in range(int(nPlacas)):
        print(str(imp+1) + '.- ' + totalPlacas[imp])
