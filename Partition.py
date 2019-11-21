


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


wantsToContinue = True

while wantsToContinue:

	print(mainMenu())
	
	op = input("\nIngrese una opcion: ")

	if op == '1':
		calculatePartitions()
	elif op == '2':
		wantsToContinue = False
	else:
		print("\nERROR: La opcion ingresada no es valida.")
