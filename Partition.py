#Universidad del Valle de Guatemala
#Matemática Discreta 
#Sara Nohemi Zavala Gutierrez 18893
#André Rodríguez 18332
#Ricardo Valenzuela 18762
#Proyecto: Particiones de un entero

#Algoritmo de Jerome Kelleher
def create_partition(number):
    a = [0 for i in range(number + 1)]
    k = 1
    y = number - 1
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

################################################################################

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
    opcion = input("Ingrese opcion deseada ")   

#Basicamente, se pide el numero y la longitud de las particiones
#Luego se hace un ciclo for
#Dentro del ciclo, para cada particion, se verifica si k (longitud) es 0 o no
#Si no es igual a 0, la lungitud de la particion va a ser la longitud final
    try:
        if opcion == "1":
            number_parameter = input("Ingrese un número ")
            particiones = create_partition(int(number_parameter))
            k_longitud = input("Ingrese longitud a la que desea realizar la partición: ")
            for elemnt in particiones:
                if int(k_longitud) == 0:
                    print(elemnt)
                elif len(elemnt) == int(k_longitud):
                    print(elemnt)
    #Extra para salvar el semestre
        elif opcion == "2":
            print("-----------------------------------")
            print("Salvemos el semestre juntos")
            print("-----------------------------------")
    # Salir del programa        
        elif opcion == "3" :
            break
        else:
            print("Inngrese opcion válida")
    except:
        print("An exception occurred")
