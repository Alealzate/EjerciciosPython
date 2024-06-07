
lista=[]
opc=0
while opc != 21:
    print("1-Suma de lista\n 2--Producto de lista\n 3--Count\n 4--Maximo y Minimo\n 5--Duplicado\n 6--Intercambio\n 7--Reverse\n 8--Pares e impares\n 9--Frutas\n 10--Mayor\n 11--Suma Sublista\n 12--Len\n 13--Pares\n 14--Range\n 15--3 en lista\n 16--Negativos\n 17--Suma dos listas\n 18--Pares ordenados\n 19--Lista range\n 20--Palabras\n 21--Salir\n")
    opc=int(input("Ingrese su opcion: "))

    if opc == 1:
    #1
        lista=[1,2,3,4,5]
        print(sum(lista))
        print("::::::::::::::::::::::::::::")

    elif opc == 2:

    #2
        lista=[1,2,3,4,5]
        producto=1
        for numero in lista:
            producto = producto * numero
        print(producto)
        print("::::::::::::::::::::::::::::")

    elif opc == 3:
    #3
        lista = [1, 2, 3, 4, 5, 3, 3]
        print(lista.count(3))
        print(lista)
        print("::::::::::::::::::::::::::::")

    elif opc == 4:
    #4
        lista = [1, 2, 3, 4, 5]
        print (max(lista))
        print(lista) 

        lista = [1, 2, 3, 4, 5]
        print (min(lista))
        print(lista) 
        print("::::::::::::::::::::::::::::")

    elif opc == 5:
    #5
        lista = [1, 2, 3, 4, 5, 3, 3]
        duplicado = list(set(lista))
        print(duplicado)
        print("::::::::::::::::::::::::::::")

    elif opc == 6:
    #6
        lista = [1, 2, 3, 4, 5]
        lista[0], lista[-1] = lista[-1], lista[0]
        print(lista)
        print("::::::::::::::::::::::::::::")

    elif opc == 7:
    #7
        lista[1:4] 
        lista = [1, 2, 3, 4, 5]
        sublista = lista[1:4]
        sublista.reverse()
        lista[1:4] = sublista
        print(lista)
        print("::::::::::::::::::::::::::::")

    elif opc == 8:
    #8
        lista = [1, 2, 3, 4, 5]
        pares = len([num for num in lista if num % 2 == 0])
        print(pares)
        impares = len([num for num in lista if num % 2 != 0])
        print(impares)
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 9:
    #9
        frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]
        print("".join(frutas))
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 10:
    #10
        lista = [1, 2, 3, 4, 5]
        mayor=[num for num in lista if num > 3]
        print(mayor)
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 11:
    #11
        lista[1:4] 
        lista = [1, 2, 3, 4, 5]
        print (sum(lista[1:4]))
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 12:
    #12
        lista = [1, 2, 3, 4, 5]
        print(sum(lista) / len(lista))
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 13:
    #13
        lista = [1, 2, 3, 4, 5]
        pares=[num for num in lista if num % 2 == 0]
        print(pares)
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 14:
    #14
        lista=[num**2 for num in range(1, 6)]
        print(lista)
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 15:
    #15
        lista = [1, 2, 3, 4, 5]
        print (3 in lista)
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 16:
    #16
        negativos=[-num for num in range(1, 11)]
        print(negativos)
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 17:
    #17
        lista1 = [1, 2, 3]  
        lista2 = [4, 5, 6]
        resultado= (lista1 + lista2)
        print(resultado)
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 18:
    #18
        lista1 = [1, 2, 3] 
        lista2 = ['a', 'b', 'c']
        paresordenados=(list(zip(lista1, lista2)))
        print(paresordenados)
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 19:
    #19
        lista=(list(range(1, 6)))
        print(lista)
        print(":::::::::::::::::::::::::::::::::::::::::::::")

    elif opc == 20:
    #20
        palabras = ["HoLa", "MUNDO", "pYThon"]
        palabras = ([palabra.upper() for palabra in palabras])
        print(palabras)

    #21
    elif opc == 21:
        
            print("Gracias vuelva prontos!!")
    else:
        print("No valido")
        
