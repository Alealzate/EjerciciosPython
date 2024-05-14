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






