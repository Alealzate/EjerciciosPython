#1 crear una lista
lista= [1,2,3,4,5]
print(lista)
#2 imprimir un numero de la lista
print(lista[3])
#3 modificar el numero 1
lista[1]=10
print(lista)
#4 Agrgar un nuevo campo a la lista
lista.append(6)
print(lista)
#5 eliminar un elemento por valor
buscar=10
lista.remove(buscar)
print(lista)
#6 eliminar un elemento por indice
i=0
del lista[0]
print(lista)
#7 longitud de la lista
print(len(lista))
#8 extender la lista
lista.extend([7,8,9])
print(lista)
#9 insertar un elemento
lista.insert(0,0)
print(lista)
#10limpiar la lista
lista.clear()
print(lista)
#11 revertir la lista
lista=[1,2,3,4,5]
lista.reverse()
print(lista)
#12 Ordenar la lista
listaDesordenada=[5,3,1,4,2]
listaDesordenada.sort()
print(listaDesordenada)
#13 indice de un elemnto (en que posicion se encuentra el 4)
indice=listaDesordenada.index(4)
print(indice)
#14 Ultimo elemento con pop()
#muestra y elimina el ultimo elemento de la lista usando pop() y luego muestra la ultima lista modificada
ultimo=listaDesordenada.pop()
print(ultimo)
print(listaDesordenada)
#15 crear listas de listas 
#crear una lista de listas donde cada sublista contiene tres numeros consecutivos y muestre la lista de listas
listaDeLista=[[1,2,3],[4,5,6],[7,8,9]]
print(listaDeLista)
#16 acceder a elementos de sublistas
#accede y muestra el primer elemento de la primera sublista
print("------")
print(listaDeLista[1][2]) #(primer corchete pertenece a la lista, segunto es el numero que hay en la lista )
#17añadir sublista
listaDeLista.append([10,11,12])
print(listaDeLista)



import os 
os.system("clear")

producto =[]
cantidad =[]
precio=[]

opc=0
while opc != 9:
    print("1-Crear un producto\n2--Buscar Un producto\n3--Actualizar Producton\n4--Eliminar producto\n5--Lista de productos\n6--Ordenar producto por nombre\n7--Invertir los productos\n8--Eliminar todos los productos\n9--Salir")
    opc=int(input("Ingrese su opcion: "))

    if opc ==1:
        os.system("clear")
        print("---Crear Producto---")
        nombreP = input("Ingresa el nombre del producto: ").capitalize()
        cantidadP = int(input("Ingrese cantidad del producto: "))
        precioP = float(input("Ingrese el precio del producto: "))

        producto.append(nombreP)
        cantidad.append(cantidadP)
        precio.append  (precioP)

        print("---Producto Agregado con exito---")

    elif opc ==2:
        os.system("clear")
        buscarProducto = input("Que producto deseas buscar?: ").capitalize()
        resultado = buscarProducto in producto

        if resultado == True:
            print("---Producto encontrado---")
            elemento = producto.index(buscarProducto)

            print("Nombre del producto ",producto[elemento])
            print("Cantidad del producto ",cantidad[elemento])
            print("Precio del producto ",precio[elemento])
        else:
                print("----- Producto No encontrado -----")


    elif opc ==3:
        os.system("clear")
        buscarProducto = input("Que producto deseas Actualizar?: ").capitalize()
        resultado = buscarProducto in producto

        if resultado == True:
            print("---Producto encontrado---")
            elemento = producto.index(buscarProducto)
            nuevoNombreP = input("Ingresa elnuevo nombre del producto: ").capitalize()
            nuevaCantidadP = int(input("Ingrese la nueva cantidad del producto: "))
            nuevoPrecioP = float(input("Ingrese el nuevo precio del producto: "))

            producto[elemento]= nuevoNombreP
            cantidad[elemento]= nuevaCantidadP
            precio[elemento]  = nuevoPrecioP
            
            print("----- Producto actualizado correctamente -----")
        else:
            print("----- Producto No encontrado -----") 

    elif opc ==4:
        os.system("clear")
        buscarProducto = input("Que producto deseas Eliminar?: ").capitalize()
        resultado = buscarProducto in producto

        if resultado == True:
            print("---Producto encontrado---")
            elemento = producto.index(buscarProducto)

            producto.pop(elemento)
            cantidad.pop(elemento)
            precio.pop(elemento)
            print("---Elemento eliminado con exito---")
        else:
            print("---El producto no fue encontrado---")    

    elif opc ==5:
        os.system("clear")
        if producto:
            print("---Lista de productos---")
            for p,c,pr in zip(producto,cantidad,precio):
                print(f"producto: {p} Cantidad: {c} Precio: {pr}")
        else:
            print("---No hay productos para mostrar---")
    elif opc ==6:
        os.system("clear")
        if producto:
            
            producto,cantidad,precio = zip(*sorted(zip(producto,cantidad,precio)))

            print("---Lista de productos en orden---")
            for p,c,pr in zip(producto,cantidad,precio):
                print(f"producto: {p} Cantidad: {c} Precio: {pr}")
        else:
            print("---No hay productos para mostrar---")

    elif opc ==7:
        os.system("clear")
        if producto:
            producto,cantidad,precio = zip(*reversed(list(zip(producto,cantidad,precio))))
            for p,c,pr in zip(producto,cantidad,precio):
                print(f"producto: {p} Cantidad: {c} Precio: {pr}")
        else:
            print("---No hay productos para mostrar---")
    elif opc ==8:
        os.system("clear")
        if producto:
            producto.clear()
            cantidad.clear()
            precio.clear()

            

    elif opc ==9:
        os.system("clear")
        print("Vuelva pronto!!")
    else:
        break 


