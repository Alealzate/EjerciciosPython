print("suma entre 2 numeros: ")
num1=int (input("digite el numero 1: "));
num2=int (input("digite el numero 2: "));
suma= int (num1+num2);

print ("La suma de los numeros es: ", suma)

#primos
num1 = int (input("ingrese un numero"));
if num1 % 2 == 0:
    print (num1, "es par" )
else:
    print (num1, "no es par" );

#ciclo
i=1
while i <=5:
 num1 = int (input("ingrese un numero"));
 if num1 % 2 == 0:
    print (num1, "es par" )
 else:
    print (num1, "no es par" );
 i=i+1

 #numeros del 1 al 10
 i = 0
while i<10:
    i=i+1
    print(i, end=",")

#pares
    i = 0
while i<6:
    i=i+2
    print(i, end=",")

#ejercicio ciclo para  
    
for i in range (0,50,5):
    print (i)

for i in range (0,50,2):
   print (i)

# segun que
   valor=int(input("digite un numero del 1 al 5:"))
if valor==1: print ("valor 1")
elif valor==2: print ("valor 2")
elif valor==3: print ("valor 3")
elif valor==4: print ("valor 4")
elif valor==5: print ("valor 5")          

#break

i=int(input("digite un numero del < 2: "))
while i!= 10:
    print("dentro del ciclo, i vale:", i)
    i=i+1
    if i==5:
     break
print("fuera del ciclo i vale:", i)

#numSecreto
i=int(input("digite un numero del <101:"))
numSecreto=33
while i !=numSecreto:
    i=int(input("digite un numero del <101:"))
print (("acertaste el numero secreto:"), numSecreto)

#numero mayor 
n1 = int (input("ingrese el primer numero: "))
n2 = int (input("ingrese el primer numero: "))
n3 = int (input("ingrese el primer numero: "))

if n1>=n2 and n1>=n3:
    mayor=n1
elif n2>=n1 and n2>=n3:
    mayor=n2
else:
    mayor = n3
print("el mayor es: ", mayor)

#.............................................................

#ejercicio 1 
v= int (input("ingrese un numero "))
t= int (input("ingrese un numero "))
d=v*t
print ("la distancia es",d)
#.......................................................


#ejercicio 2
nota1=float(input("ingrese nota 1 "))
nota2=float(input("ingrese nota 2 "))
nota3=float(input("ingrese nota 3 "))
promedio=(nota1+nota2+nota3)/3
print("su promedio es", promedio)

#...........................................................
#ejercicio 3
respco=int(input("ingrese el numero de respuestas correctas "))
respinc=int(input("ingrese el numero de respuestas incorrectas "))
respenbla=int(input("ingrese el numero de respuestas en blanco "))
puntajeFinal=(respco*4)+ respinc*(-1)
print ("el puntaje final es ", puntajeFinal)

#........................................................................
#ejercicio 4
partgana=int(input("ingrese el numero de partidos ganados "))
partperd=int(input("ingrese el numero de partidos perdidos "))
partempat=int(input("ingrese el numero de partidos empatados "))
puntajefinal=(partgana*3) + (partempat*1) 
print ("El puntaje final es ", puntajefinal)
#............................................................................
#ejercicio 5
tph=float(input("ingrese la tarifa por hora "))
hl=int(input("ingrese el numero de horas laboradas "))
planilla=tph*hl
print ("el total de su planilla es ", planilla)
#..........................................................................
#ejercicio 6
import math
ladoa=float(input("ingrese lado a "))
ladob=float(input("ingrese lado b "))
ladoc=float(input("ingrese lado c "))
semi=(ladoa+ladob+ladoc)/2
are= math.sqrt (semi*(semi-ladoa)*(semi-ladob)*(semi-ladoc))
print("el area del triangulo es ", are)
print("el semiperimetro del triangulo es ", semi)
#................................................................................
#ejercicio 7
import math
gb=int(input("ingrese la cantidad de gb que quiere almacenar "))
mb=gb*1024
cantc=mb/700
print(("la cantidad de cd que se necesita es "), math.trunc (cantc))
#...............................................................................
#ejercicio 8
abca=int(input("ingrese abcisa de a "))
orda=int(input("ingrese ordenada de a "))
abcb=int(input("ingrese abcisa de b "))
ordb=int(input("ingrese ordenada de b "))
dis=((abcb-abca)**2+(ordb-orda)**2)**0.5
print ("la distancia entre a y b es", dis)
#.................................................................................
#ejercicio 9
aact=int(input("ingrese el año actual "))
anac=int(input("ingrese el año de nacimiento "))
ed=aact-anac
if ed>=17:
    print("debe solicitar su cuil ")
else:
     print("no debe solicitar su cuil ")
     #............................................................................
     #ejercicio 10
ph=int(input("ingrese la edad del primer hermano "))
sh=int(input("ingrese la edad del segundo hermano "))
if ph>sh:
    dih=ph-sh
    print("El primer hermano es mayor", dih, "años")
else:
    dih=sh-ph
    print("El segundo hermano es mayor", dih, "años")
    #.................................................................................
    #ejercicio 11
    import math
pl=int(input("ingrese la produccion del lunes "))
pm=int(input("ingrese la produccion del martes "))
pmi=int(input("ingrese la produccion del miercoles "))
pj=int(input("ingrese la produccion del jueves "))
pv=int(input("ingrese la produccion del viernes "))
ps=int(input("ingrese la produccion del sabado "))
ppromedio=(pl+pm+pmi+pj+pv+ps)/6
print ("promedio produccion total: ",math.trunc (ppromedio))
if ppromedio>=100:
    print("recibiras incentivo")
else:
    print("no aplicas para el incentivo")
#..............................................................................
    #ejercicio 12
n1 = int (input("ingrese el primer numero: "))
n2 = int (input("ingrese el primer numero: "))
n3 = int (input("ingrese el primer numero: "))

if n1>=n2 and n1>=n3:
    mayor=n1
elif n2>=n1 and n2>=n3:
    mayor=n2
else:
    mayor = n3
print("el mayor es: ", mayor)
#............................................................................
#ejercicio 13
l1 = int (input("ingrese lado 1 "))
l2 = int (input("ingrese lado 2 "))
l3 = int (input("ingrese lado 3 "))
if l1==l2 and l2==l3 and l3==l1:
    print("el triangulo es equilatero")
elif l1!=l2 and l2!=l3 and l3!=l1:
    print("el triangulo es escaleno")
else: print("el triangilo es isosceles")
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#ejercicio 13
l1 = int (input("ingrese lado 1 "))
l2 = int (input("ingrese lado 2 "))
l3 = int (input("ingrese lado 3 "))
if l1==l2  == l3:
    print("el triangulo es equilatero")
elif l1!=l2 and l1!=l3 :
    print("el triangulo es escaleno")
else: print("el triangilo es isosceles")
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
##un estudiante de fisica realiza un experimento del movimiento rectilineo uniforme, donde un movil se desplaza con velocidad constante. 
##para evaluar su desempaño en este experimento el estudiante debera hacer 3 calculos y montrar un mensaje por cada experimento y su promedio final.


v= int (input("ingrese un numero "))
t= int (input("ingrese un numero "))
d1=v*t
print ("la distancia1 es",d1)

v= int (input("ingrese un numero "))
t= int (input("ingrese un numero "))
d2=v*t
print ("la distancia2 es",d2)

v= int (input("ingrese un numero "))
t= int (input("ingrese un numero "))
d3=v*t
print ("la distancia3 es",d3)

promedio=(d1+d2+d3)/3
print("su promedio es", promedio)
##::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
menu=int(input("ingrese\nnumeros_romanos--1\nvocales--2 "))

if menu==1:

    def romanos(x):
        numeros_romanos={
            1:"I",
            2:"II",
            3:"III",
            4:"IV",
            5:"V",
            6:"VI",
            7:"VII",
            8:"VIII",
            9:"IX",
            10:"X"

        }
        numeros= numeros_romanos.get(x)

        return  numeros
    
    datos=int(input("ingrese un numero entre el 1 y el 10 "))

    #Validacion del dato de entrada
    if datos>=1 and datos<=10:

        validar=romanos(datos)

        print("el numero es", validar)
    else:
        print("numero no existe")

elif menu==2:

    def vocales(y):

        letras={
            1:"a",
            2:"e",
            3:"i",
            4:"o",
            5:"u",
        }
        vocales=letras.get(y)

        return vocales
    
    datos_vocales=int(input("ingrese un numero entre el 1 y el 5"))

    if datos_vocales>=1 and datos_vocales<=5:

        ejecutar= vocales(datos_vocales)

        print("la vocal es",ejecutar)

    else:
        print("numero no existe")




::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.

           ##ejercicio1
try:
    numEntero=int (input("ingrese un numero del 1 al 10 "))
    if numEntero == 1:
        print ("I")
    elif numEntero == 2:
        print ("II")
    elif numEntero == 3:
        print ("III")
    elif numEntero == 4:
        print ("IV")
    elif numEntero == 5:
        print ("V")
    elif numEntero == 6:
        print ("VI")
    elif numEntero == 7:
        print ("VII")
    elif numEntero == 8:
        print ("VIII")
    elif numEntero == 9:
        print ("IX")
    elif numEntero == 10:
        print ("X")
except:
    print("numero no valido")
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#Ejercicio2
try:
    salario=float(input("digite el salario: "))
    bonificacion=float(input("digite la bonificacion: "))
    print(f"el salario {salario} + bonificacion {bonificacion}% es:{salario*(bonificacion+1)} " )
except ValueError:
    print("digite numeros y no letras")
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#ejercicio3

def vocales(y):

        letras={
            1:"a",
            2:"e",
            3:"i",
            4:"o",
            5:"u",
        }
        vocales=letras.get(y)

        return vocales
datos_vocales=int(input("ingrese un numero entre el 1 y el 5"))

if datos_vocales>=1 and datos_vocales<=5:

        ejecutar= vocales(datos_vocales)

        print("la vocal es",ejecutar)

else:
        print("numero no existe")

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
##Ejercicio4
#Escribe un programa que reciba una edad como entrada y clasifique a la persona en las siguientes categorías: niño 
#(menos de 11 años), 
#adolescente (12-17 años), adulto (18-64 años) o mayor (65 años o más).
#Opcional: preadolescente: 11 a 13 y adolescente de 14 a 17
try:
    edad=int(input("ingrese su edad "))
    if edad <=11:
        print("Es niño")
    elif edad >12 and edad <=17:
        print("es adolecente")
    elif edad >18 and edad <=64:
        print("Es adulto")
    else:
       print("la persona es mayor")
except:("no valido")
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#ejercicio5
#Escribe un programa que reciba una nota (0-100) y la clasifique en: 
#deficiente (menos de 50), aprobado (50-64), notable (65-84), sobresaliente (85-100
try:
    nota=float(input("ingrese su nota "))
    if nota < 50:
     print("deficiente")
    elif nota >=50 and nota <=64:
     print("Aprobado")
    elif nota >=64 and nota <=84:
     print("Notable")
    elif nota >=85 and nota <=100:
     print("Sobresaliente")
except:("No valido") 
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#ejercicio6
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
        