n1 = int (input("ingrese el primer numero: "))
n2 = int (input("ingrese el segundo numero: "))
n3 = int (input("ingrese el tercer numero: "))

try:
    if n1>n2 and n1>n3 and n2>n3:
        print("n1 es mayor, n3 es menor y n2 es el del medio")
    elif n2>n3 and n2>n1 and n1>n3:
        print("n2 es mayor, n3 es menor, y n2 es el del medio")
    elif n3>n1 and n3>n2 and n2>n1:
        print("n3 es mayor, n1 es menor y n2 el del medio ")
    elif n1>n2 and n1>n3 and n3>n2:
        print("n1 es mayor, n2 es menor y n3 el del medio")
    elif n2>n1 and n2>n3 and n3>n1:
        print("n2 es mayor, n1 es menor y n3 el del medio ")
    elif n3>n2 and n3>n1 and n1>n2:
        print("n3 es mayor, n2 es menor y n1 el del medio")
    elif n1== n2 and n2==n3 and n1==n3:
        print("todos los numeros son iguales")
    elif n1==n2 and n2==n1:
        print("hay dos numeros iguales")
    elif n3==n2 and n1==n3:
        print("hay dos numeros iguales")
    elif n2==n3 and n3==n1:
        print("hay dos numeros iguales")
except:
    print("solicitud no valida" )
        