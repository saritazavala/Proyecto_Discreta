#Universidad del Valle de Guatemala
#Sara Nohemi Zavala Gutierrez
#Carnet: 18893
#Pro

def partitionsOf(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

def mainMenu():
	return '''
	\n\tMenu Principal
	\n1. Calcular particiones
	\n2. Salir
	'''

def calculatePartitions():
	
	n = input("\n\nIngrese un numero N: ")
	particiones = partitionsOf(int(n))
	#print("\nExisten", len(list(particiones)), "particiones del numero", n)

	k = input("\nIngrese longitud de particiones a desplegar: ")
	for i in particiones:
		if int(k) == 0:
			print(i)
		elif len(i) == int(k):
			print(i)






print("-----------------------------------------------")
print("        Particiones de números enteros"         ) 
print("-----------------------------------------------")
print("")
while True:
    print("*******************************")
    print("        Menu de opciones "      )
    print("*******************************")

    print("1. Calular partición de numero n")
    print("2. Mensaje")
    print("3. Salir")
    print('')
    opcion = input("Ingrese opcion deseada")

    if opcion == "1":
        calculatePartitions()
    elif opcion == "2" :
        break
    else:
        print("Inngrese opcion válida")
