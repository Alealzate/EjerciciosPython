#1crear una lista
lista= [1,2,3,4,5]
print(lista)
#2imprimir un numero de la lista
print(lista[3])
#3modificar el numero 1
lista[1]=10
print(lista)
#4Agrgar un nuevo campo a la lista
lista.append(6)
print(lista)
#5eliminar un elemento por valor
buscar=10
lista.remove(buscar)
print(lista)
#6eliminar un elemento por indice
i=0
del lista[0]
print(lista)
#7longitud de la lista
print(len(lista))
#extender la lista
lista.extend([7,8,9])
print(lista)
#insertar un elemento
lista.insert(0,0)
print(lista)
#limpiar la lista
lista.clear()
print(lista)
#revertir la lista
lista=[1,2,3,4,5]
lista.reverse()
print(lista)
#Ordenar la lista
listaDesordenada=[5,3,1,4,2]
listaDesordenada.sort()
print(listaDesordenada)



