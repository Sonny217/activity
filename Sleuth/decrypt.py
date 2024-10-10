Num1 = int (input("Ingrese primer valor:"))
Num2 = int (input("Ingrese segundo valor:"))
if Num1 > Num2:
    suma = Num1 + Num2
    resta = Num1 - Num2
    print("Suma del pirmer Valor mas el segundo:" + " " + str(suma) + " " + "y su Resta:" + " " + str(resta))

else:
    producto = Num1 * Num2
    division = Num1 / Num2
    print("Producto del primer Valor por el segudno:"+ " " + str(producto) + " " + "y su division:" + " " + str(division))
####################################################################################
Nota1 = int (input("Ingrese Primera Nota:"))
Nota2 = int (input("Ingrese segunda Nota:"))
Nota3 = int (input("Ingrese tercera Nota:"))
NotasT = {Nota1, Nota2, Nota3}

Promedio = sum(NotasT) / len(NotasT)
if Promedio >= 7:
    print("Promocionado: " +  " " + str (Promedio))
else:
    print("No Promocionado: " + " " + str (Promedio))
#####################################################################################
NUm = int (input("Ingrese un Numero de 1 o 2 digitos:"))
if NUm < 10:
    print("el numero ingresado tiene dos digitos:" + " " + str (NUm))
else:
    print("El numero ingresado es de un solo digito" + " " + str (NUm))
######################################################################################
num1 = int(input("Ingrese primer valor:"))
num2 = int(input("Ingrese segundo valor:"))
num3 = int(input("Ingrese tercer valor:"))
if num1 > num2 and num1 > num3:
    print("El numero mayor es:" + " " + str(num1))
else:
    if num2 > num1 and num2 > num3:
     print("El numero mayor es:" + " " + str(num2))
    if num3 > num2 and num3 > num1:
        print("El numero mayor es:" + " " + str(num3))
########################################################################################
valor = int(input("Ingrese un digito:"))
if valor > 0:
    print("El valor es positivo:" + " " + str(valor))
else:
    if valor < 0:
        print("El valor es negativo:" + " " + str(valor))
    else:
        if valor == 0:
            print("El valor es nulo(es decir 0)" + " " + str(valor))
#########################################################################################
Num = int(input("Ingrese un numero:"))
if Num <=9:
    print("El nuemro es de un digito:" + " " + str(Num))
else:
    if Num < 99 and Num > 10 :
        print("El nuemro es de dos digito:" + " " + str(Num))
    else:
        if Num <=999 and Num >= 100 :
            print("El numero es de tres digitos:" + " " + str(Num))
        else:
            print("Error el digito sobrepasa lo permitido vuelva intentarlo" + " " + str(Num))
############################################################################################
preguntas = int(input("Ingres cantdiad de preguntas realizadas: "))
respuetas = int(input("Igrese cantidad respuestas corectas: "))
if respuetas <= 50:
    print("Esta fuera de nivel:" + " " + str(respuetas))
else :
    if respuetas <75 and respuetas >= 50:
        print("Esta en un nivel regular:" + " " + str(respuetas))
        if respuetas <90 and respuetas >=75:
            print("Esta en un nivel medio:" + " " + str(respuetas))
            if respuetas >=90:
                print("Esta en un nivel maximo:" + " " + str(respuetas))
############################################################################################
X = int(input("Enter X Coordinate:"))
Y = int(input("Enter Y Coordinate:"))
if X > 0 and Y > 0:
    print("Belongs to the First Quadrant:" + "[" + str(X) + "][" + str(Y) + "]")
else:
    if X < 0 and Y > 0:
        print("Belongs to the Second Quadrant:" + "[" + str(X) + "][" + str(Y) + "]")
    else:
        if X < 0 and Y < 0:
            print("Belongs to the Third Quadrant:" + "[" + str(X) + "][" + str(Y) + "]")
        else:
            if X > 0 and Y < 0:
                print("Belogs to the Fourth quadrant:" + "[" + str(X) + "][" + str(Y) +"]")
############################################################################################
operator
salary = int(input("Enter Salary:"))
years = int(input("Enter Year:"))
if salary < 500 and years > 10:
    increase = salary * 0.20
    print("Salary Extra Payment:" + " " + str(increase))
else:
    if salary < 500 and years < 10:
        increase1 = salary * 0.05
        print("Salary Extra Payment:" + " " + str(increase1))
    else:
        if salary >= 500 and years == 10:
            print("Salary Extra Payment" + " " + str(salary))
############################################################################################
value1 = int(input("Enter the First value:"))
value2 = int(input("Enter the Second value:"))
value3 = int(input("Enter the Third value:"))
#############################################################################################
Define a function to find the truth by shifting the letter by the specified amount
def lasso_letter(letter, shift_amount):

    # Invoke the ord function to translate the letter to its ASCII code
    # Save the code to the letter_code variable
    letter_code = ord(letter.lower())

      # The ASCII number representation of lowercase letter 'a'
    a_ascii = ord('a')

     # The number of letters in the alphabet
    alphbet_size = 26

    # The formula to calculate the ASCII number for the decoded letter
    # Take into account looping around the alphabet
    true_letter_code = a_ascii + (((letter_code - a_ascii) + shift_amount) % alphbet_size)

     # Convert the ASCII number to the character or letter
    decoded_letter = chr(true_letter_code)

    # Send the decoded letter back
    return decoded_letter

def lasso_word( word, shift_amount ):

    # This variable is updated each time another letter is decoded
    decoded_word = ""

    # This for loop iterates through each letter in the word parameter
    for letter in word:
        # The lasso_letter() function is invoked with each letter and the shift amount
        # The result (the decoded letter) is stored in a variable called decoded_letter
        decoded_letter = lasso_letter(letter, shift_amount)

        # The decoded_letter value is added to the end of the decoded_word value
        decoded_word = decoded_word + decoded_letter

    # The decoded_word is sent back to the line of code that invoked this function
    return decoded_word

print( "Shifting Ncevy by 13 gives: \n" + lasso_word( "Ncevy", 13 ) )
print( "Shifting gpvsui by 25 gives: \n" + lasso_word( "gpvsui", 25 ) )
print( "Shifting ugflgkg by -18 gives: \n" + lasso_word( "ugflgkg", -18 ) )
print( "Shifting wjmmf by -1 gives: \n" + lasso_word( "wjmmf", -1 ) )
#############################################################################################
first_number = int(input('Type the first number: ')) ;\
second_number = int(input('Type the second number: ')) ;\
print("The sum is: ", first_number + second_number)
#############################################################################################

leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)
#############################################################################################
ingresa un valor flotante para la variable a aquí
va = float(input("Ingrese un valor:"))
# ingresa un valor flotante para la variable b aquí
vb = float (input("Ingrese un valor:"))

# mostrar el resultado de la suma aquí
print(" suma de las variables" + " "+ str(va + vb))
# mostrar el resultado de la resta aquí
print(" resta de las variables" + " " + str(va - vb))
# mostrar el resultado de la multiplicación aquí
print(" Multiplicación de las variables" + " " + str(va * vb))

# mostrar el resultado de la división aquí
print("división de las variables" + " " + str(va / vb))


print("\n¡Eso es todo, amigos!")
x = int(input())
y = int(input())

x =x%y
x =x%y
y =y%x
print(y)
class car:

   pass
cull_dot = car()
print(cull_dot)
nums = [0, 1, 2, 3]

try:
   print(sum(nums))

except:
   print('Cannot print the sum! Your variables are not numbers.')
def factorial(num):
   if num == 1:
       return 1
   else:
       return num * factorial(num-1)
########################################################
########################################################
########################################################

En una empresa trabajan n empleados cuyos sueldos oscilan
entre $100 y $500, realizar un programa que lea los sueldos
que cobra cada empleado e informe cuántos empleados cobran
entre $100 y $300 y cuántos cobran más de $300. Además el
programa deberá informar el importe que gasta la empresa en
sueldos al personal.
x= 1
contador= 0
contador1= 0
gastos = 0
n = int(input("Ingrese numeroe de trabajadores: "))
while x <= n:
    sueldos= int(input("Ingrese sueldo de trabajadores:"))
    if sueldos >=100 and sueldos <=300:
        contador = contador+1
    elif sueldos >= 300:
        contador1 = contador1+1
    gastos = gastos + sueldos
    x = x+1
print("sueldos que oscilan entre 100 a 300 pesos:" +" "+ str(contador))
print("Sueldos mayores a 300 pesos:" + " " + str(contador1))
print("Gastos total de la empresa en sueldos:" + " " + str(gastos))

########################################################
########################################################
########################################################

Se ingresan un conjunto de n alturas de personas por teclado.
Mostrar la altura promedio de las personas.
x = 1
n = int(input("Ingrese  cuantas alturas seran promediadas:"))
suma = 0
while x <= n:
    altura = float(input("Ingrese altura de la persona:"))
    suma = suma + altura
    x = x+1
promedio = suma/n
print("La altura promesio es :"+ " " + str (promedio) )

########################################################
########################################################
########################################################

Realizar un programa que imprima 25 términos de la serie
11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)
x = 1
conttador = 11
while x <= 25:
    print(conttador)
    x = x+1
    conttador = conttador +11

########################################################
########################################################
########################################################

Mostrar los múltiplos de 8 hasta el valor 500.
Debe aparecer en pantalla 8 - 16 - 24, etc.
x = 1
multiplo = 8
while multiplo <=500:
    print(multiplo)
    multiplo = multiplo + 8

########################################################
########################################################
########################################################

Realizar un programa que permita cargar dos listas de 15 valores
cada una. Informar con un mensaje cual de las dos listas tiene
un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas
en un algoritmo.
x = 1
y = 1
suma = 0
suma1 = 0
while x <= 15:
    Lista = int(input("Ingrese valor de la primera lista:"))
    suma = suma + Lista
    x = x + 1

while y <= 15:
    lista1 = int(input("Ingrese valor de la segunda lista:"))
    suma1 = suma1 + lista1
    y = y + 1
print("La suma total de la segunda lista es :"+ " " + str(suma1))
print("La suma total de la primera lista es :"+ " " + str(suma))
if suma >= suma1:
    print("La primera lista es mayor a la segunda lista" +" " + str(suma))
else:
    if suma1 >= suma:
        print("La segunda lista es mayor a la primera lista"+ " "+ str(suma1))

########################################################
########################################################
########################################################

Desarrollar un programa que permita cargar n números enteros
y luego nos informe cuántos valores fueron pares y cuántos
impares.
Emplear el operador “%” en la condición de la estructura
condicional (este operador retorna el resto de la división
de dos valores, por ejemplo 11%2 retorna un 1):
	if valor%2==0:

x = 1
n = int(input("Ingrese  un numero:"))
contador = 0
contador1 = 0
while x <= n:
    valor = int(input("Ingres valor a evalurar:"))
    if valor%2 == 0:
        contador1= contador1 + 1
    else:
        contador=contador+1
    x = x + 1
print("Numero total de pares:" + " " + str(contador))
print("Numero total de impares:" + " " + str(contador1))

########################################################
########################################################
########################################################

lista = [12, 130, 100, 14, 150, 16, 17, 180]
contador = 0
for element in lista:
   if element >= 100:
       contador=contador+1
print("La canditad de numero " + contador)

lista =["arreglo","acumulador","superior", "más", "valor", "suma "]

mars_temperature = "The highest temperature on Mars is about 30 C"
or item in mars_temperature.split():
   if item.isnumeric():
       print(item)

lista =[]
for x in range(5):
   nombre= str(input("Ingresse un nombre a la lista:"))
   lista.append(nombre)

menor = lista[0]
for x in range(1,5):
if lista[x]<menor:
   menor=lista[x]

print("Lista completa:", lista)
print("Nombre menor de la lista:",menor)
###############################
Este codigo  trabaja con lista y me dice cual es el numero,
mayor de la lista y cual numero se repite en la lista.
###############################

lista=[]
for x in range(5):
   nombres= int(input("Ingrese un numero a la lista:"))
   lista.append(nombres)

mayor = lista[0]

for x in range(1,len(lista)):
   if lista[x] > mayor:
       mayor = lista[x]

repedito = lista.count(mayor)

print("Lista completa: ", lista)
print("Numero mayor dentro de la lista: ", mayor)
print("Hay un numero que se repite en la lista: ",repedito)

###############################
Este codigo  trabaja con lista y me dice cual es el numero,
mayor de la lista y si dicho numero se repite en la lista.
###############################

lista=[]
for x in range(5):
   nombres= int(input("Ingrese un numero a la lista:"))
   lista.append(nombres)

mayor = lista[0]

for x in range(1,len(lista)):
   if lista[x] > mayor:
       mayor = lista[x]

repedito = lista.count(mayor)

print("Lista completa: ", lista)
print("Numero mayor dentro de la lista: ", mayor)
print("Hay un numero que se repite en la lista: ",repedito)
if repedito >1:
  print(f"El numero {mayor} de la lista se repite")
else:
     print(f"El numero  {mayor}  de la lista no se repite")


Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

for i in range(1, 101):
   if i % 3 == 0 and i % 5 == 0:
       print("Fizzbuzz")
   elif i % 3 == 0:
       print("Fizz")
   elif i % 5 == 0:
       print("Buzz")
   else:
       print(i)

lista=[[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]
suma=0
for k in range(len(lista)):
   for x in range(len(lista[k])):
       suma=suma+lista[k][x]
print(suma)

lista=[[100,7,85,8], [4,8,56,25], [67,89,23,1], [78,56]]
print(lista)
print("-------------")
for k in range(len(lista)):
   for x in range(len(lista[k])):
       if lista[k][x] > 50:
           print(lista[k][x])

lista=[[4,12,5,66], [14,6,25], [3,4,5,67,89,23,1], [78,56]]
print(lista)
for i in range(len(lista[0])):
   if lista[0][i] > 10:
       lista[0][i]=0
print(lista)

lista = [[5, 8, 9], [7, 3, 4, 5], [1, 4, 8], [2, 3, 4, 1], [2, 4, 5, 8], [3, 5, 4, 2]]
print("Lista original:", lista)
for i in range(len(lista)):
   print(lista[i][-1])

calculo de temperatura por trimestre####
nombres_paises=[]
temperatura=[]
promedio_Temperatura=[]
for i in range(4):
   nom_pais= str(input("Ingrese un nombre de pais: "))
   nombres_paises.append(nom_pais)
   temp1=int(input("Ingrese Primera temperatura:"))
   temp2=int(input("Ingrese Segunda temperatura:"))
   temp3=int(input("Ingrese Tercera temperatura:"))
   temperatura.append([temp1,temp2,temp3])

print("Lista de paises:",[nombres_paises],"\n Temperaturas:",[temperatura])
for x in range(4):
   prom= (temperatura[x][0] + temperatura[x][1] + temperatura[x][2])//3
   promedio_Temperatura.append(prom)
print("paises y temperaturas medias trimestrales:")
for x in range(4):
   print(nombres_paises[x],":", promedio_Temperatura[x])

posmayor=0
for x in range(1,4):
   if promedio_Temperatura[x] > promedio_Temperatura[posmayor]:
       print("Pais con temperatura media trimestral mayor:", nombres_paises[posmayor])
###############################################################
###############################################################
"Gestión de Inasistencias de Empleados
#dias_ausente = []
for x in range(3):
   nomb=str(input("Ingrese nombre del empleado:"))
   nombre_empleado.append([nomb])
print("Lista de empleados:",nombre_empleado)

suma =0
for x in range(len(nombre_empleado)):
   falta= int(input("ingrese el numero de dias que falto:"))
   dias_ausente.append([falta])
suma =([nombre_empleado[0] + dias_ausente[0]], [nombre_empleado[1] + dias_ausente[1]], [nombre_empleado[2]] + dias_ausente[2])
print("Lista de empleados con sus asusencias:", suma, sep=":")

menor=dias_ausente[0][0]
ind_menor=0
for i in range(1, len(dias_ausente)):
   if dias_ausente[i][0] < menor:
       menor = dias_ausente[i][0]
       ind_menor=i
print(f"Empelados que menos faltron en el mes:{nombre_empleado[ind_menor][0]} con {menor} dias de ausencia")

lista=[]
contador = 1
for x in range(50):
   lista.append([])
   cont = 1
   for i in range (contador):
     lista[x].append(cont)
       cont= cont+1
   contador= contador+1
print(lista)

def mostrar_perimetro(lado):
   per=lado*4
   print("El perimetro es",per)


def mostrar_superficie(lado):
  sup=lado*lado
  print("La superficie es",sup)


def cargar_dato():
  la=int(input("Ingrese el valor del lado de un cuadrado:"))
  respuesta=input("Quiere calcular el perimetro o la superficie[ingresar texto: perimetro/superficie]?")
  if respuesta=="perimetro":
      mostrar_perimetro(la)
 if respuesta=="superficie":
    mostrar_superficie(la)


programa principal

cargar_dato()

def contador_vocales(vocales):
    contador=0
    for x in range(len(vocales)):
         if vocales[x]=="a" or vocales[x]=="e" or  vocales[x]=="i" or  vocales[x]=="o" or  vocales[x]=="u":
              contador+=1
    print(f"Caantidad de vocales de la palabra {vocales}: es> {contador} ")


contador_vocales("Saludos")
contador_vocales("Como estan")
contador_vocales("Feliz noche")

def ordenar_imprimir(v1,v2,v3):
#    if v1<v2 and v1<v3:
     if (v2<v3):
         print(v1,v2,v3)
     else:
         print(v1,v3,v2)
 else:
    if (v2<v3):
        if (v1<v3):
           print(v2,v1,v3)
      else:
          print(v2,v3,v1)
  else:
      if (v1<v2):
         print(v3,v1,v2)
    else:
       print(v3,v2,v1)


def cargar():
  num1=int(input("Ingrese primer valor:"))
 num2=int(input("Ingrese segundo valor:"))
 num3=int(input("Ingrese tercer valor:"))
ordenar_imprimir(num1,num2,num3)


bloque principal

cargar()

def recibir_enteros(n1,n2,n3):
   sum = n1 + n2 + n3 /3
   return sum


Bloque principal
numero1=int(input("Ingrese primer valor:"))
numero2=int(input("Ingrese segundo valor:"))
numero3=int(input("Ingrese tecer valor:"))
print(recibir_enteros(numero1,numero2,numero3))


def recibir_perimetro(lado):
 perim=lado*4
 return perim

bloque principal
la = int(input("Ingrese el lado del perimetro:"))
print(f"El perimero es {recibir_perimetro(la)}")

ef retornar_superficie(lado1, lado2):
   super = lado1*lado2
   return super

Bloque principal
lado1 = int(input("Ingrese la altura del perimetro:"))
lado2 = int(input("Ingrese la base del perimetro:"))
print(f"La superfidel perimetro es {retornar_superficie(lado1, lado2)}")

def retornar_superficie(lado1,lado2):
  superficie=lado1*lado2
   return superficie


bloque principal

print("Primer rectangulo")
lado1=int(input("Ingrese lado menor del rectangulo:"))
lado2=int(input("Ingrese lado mayor del rectangulo:"))
print("Segundo rectangulo")
lado3=int(input("Ingrese lado menor del rectangulo:"))
lado4=int(input("Ingrese lado mayor del rectangulo:"))
if retornar_superficie(lado1,lado2)==retornar_superficie(lado3,lado4):
   print("Los dos rectangulos tiene la misma superficie")
else:
   if retornar_superficie(lado1,lado2)>retornar_superficie(lado3,lado4):
       print("El primer rectangulo tiene una superficie mayor")
   else:
       print("El segundo rectangulo tiene una superficie mayor")

def cantidad_vocales(cadena):
  cantidad=0
for x in range(len(cadena)):
      if cadena[x]=="a" or cadena[x]=="A":
          cantidad= cantidad + 1
 return cantidad
Bloque principal
cadena = str(input("Ingrese una palbra:"))
print(f"La palabra{cadena} tiene {cantidad_vocales(cadena)} a")


def lista_enteros(lista,va):
   for x in range(len(lista)):
       multi=lista[x]*va
       print(multi)


bloque principal

lista=[3, 7, 8, 10, 2]
print("Lista original:",lista)
print("Lista multiplicando cada elemento por 3")
lista_enteros(lista,3)

def  mas_caracteres(palabras):
  conta=0
  for x in range(len(palabras)):
     if len(palabras[x]) > len(palabras[conta]):
         conta=x
 return conta

Bloque principal
palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print(f"Palabra con mas caracteres:{mas_caracteres(palabras)}")

def lista_producto(lista):
 product =1
 for x in range(len(lista)):
   product = product * lista[x]
 return product

bloque princial
lista=[2,1,3,5,6,8,12]
print(f"Lista completa :{lista}")
print(f"el producto de la lista:{lista_producto(lista)}")

def  enteros():
valor1=int(input("Ingrese primer valor:"))
valor2=int(input("Ingrese segundo valor:"))
valor3=int(input("Ingrese tercer valor:"))
promedio = (valor1 + valor2 + valor3)//3
print(f"El promedio del valor es:{promedio}")

enteros()

def cuadrados():
  lados = input("Ingrese las longitudes de los cuatro lados del cuadrado separadas por comas (ejemplo: 5,5,5,5): ")
  la1, la2, la3, la4 = map(int, lados.split(','))
  perimetro = la1 + la2 + la3 + la4 * 4
  return perimetro
cuadrados()

def retornar_superficie(lado1, lado2):
   superficie = lado1*lado2
   return superficie

blouqe principal
valor1 =int(input("Ingrese base del rectangulo:"))
valor2 =int(input("Ingrese la altura del rectangulo:"))
print(f"la superficie del rectanculo es:{retornar_superficie(valor1, valor2)}")

def reci_entero(v1,v2,v3=0,v4=0,v5=0):
   su= v1+v2+v3+v4+v5
   return su

bloque principal
print(f"Suma de 5 + 6 = {reci_entero(5,6)}")
print(f"Suma de 1+2+3 = {reci_entero(1,2,3)}")
print(f"Suma de 1+2+3+4+5 = {reci_entero(1,2,3,4,5)}")


def multipixel(numero, elementos=11):
   for x in range(elementos):
       multi = x * numero
       print(multi, "-" ,sep="", end="")
   return multi

multipixel(2)

def edades(*list):
   cont=0
   for x in range(len(list)):
       if list[x]>=18:
           print(f"mayor de edade son:{list[x]}")
       else:
           print(f"menor de edade son:{list[x]}")
   cont=cont+1

list=[18,16,17,34,14,20]
eda = edades(*list)
print(eda)

#Codigo Base####
def cargar_lista():
   lista = []
   for x in range(5):
       val=int(input("Ingrenes valor entero:"))
       lista.append(val)
   return lista

def entero_mayo_menor(lista):
   cont1=0
   for x in range(lista):
       if lista[x] > lista[x+1]:
           print(F"enteros mayore:{cont1}")
   cont1+=1

lista=cargar_lista()
entero_mayo_menor()
###############################################################
def cargar_lista():
##   for x in range(5):
     val = int(input("Ingrese un valor entero: "))
     lista.append(val)
 return lista

def entero_mayo_menor(lista):
  cont1 = 0
  for x in range(len(lista) - 1):  # Iterar hasta el penúltimo índice
      if lista[x] > lista[x + 1]:  # Comparar elementos adyacentes
          cont1 += 1
          print(f"Enteros mayores que el siguiente: {lista[x]}")
  print(f"Total de enteros mayores que el siguiente: {cont1}")

Cargar la lista y usarla como argumento para la segunda función
lista = cargar_lista()
entero_mayo_menor(lista)


###############################################################
def empleado1():
sueldo1= [va1, va2]
va1 =str(input("Ingrese nombre del empleado:"))
va2 =int(input(f"Ingrese sueldo del empleado {va1}:"))

def empleado2():
sueldo2=[va3,va4]
# va3 =str(input("Ingrese nombre del empleado:"))
va4 =int(input(f"Ingrese sueldo del empleado {va3}:"))
sueldo2.append(va3,va4)


def cargar_empleados(empleado1, empleado2):
   print(empleado1)
   print(empleado2)

def mayor_sueldo(sueldo1, sueldo2):
   if sueldo1[1]>=sueldo2[1]:
       print(f"El empleado con mayor sueldo es:{empleado1}")
  else:
     print(f"El empledaod con el sueldo mayor es:{empleado2}")

cargar_empleados()
mayor_sueldo()
empleado1()
empleado2()
###############################################################
def cargar_empleado():
#   nombre=input("Ingrese el nombre del empleado:")
  sueldo=float(input("Ingrese su sueldo:"))
  return (nombre,sueldo)


def mayor_sueldo(empleado1,empleado2):
#    if empleado1[1]>empleado2[1]:
      print(empleado1[0],"tiene mayor sueldo")
  else:
      print(empleado2[0],"tiene mayor sueldo")


bloque principal

empleado1=cargar_empleado()
empleado2=cargar_empleado()
mayor_sueldo(empleado1,empleado2)

def edad(lista, *lista1):
   cont=0
   if lista >=18:
      cont+=1
   for x in range(len(lista1)):
       if lista1[x] >= 18:
         cont+=1
   return cont
print("Edades mayores o igual a 18:",edad(14,19,23,18,15,29,38))


def word():
    cant = 0
    x = 0
    palabr = str(input("Ingrese una oracion:"))
    while x < len(palabr):
        if palabr[x] == " ":
            cant += 1
        x += 1
    return cant   

space = word()
print(f"La cantidad de espacios que contiene la oracion es:{space}")

def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
    return li


def imprimir_mayor10(li):
    print("Elementos de la lista mayores a 10")
    for x in range(len(li)):
        if li[x]>10:
            print(li[x])


# bloque principal del programa

lista=carga_lista()
imprimir_mayor10(lista)

def carga_sueldos():
    sul=[]
    for x in range(10):
        money= int(input("Ingrese sueldo:"))
        sul.append(money)
    return sul

def superios_suledo(sul):
    print("Lista de sueldos mayores o igual a $4000:")
    for sueldo in sul:
        if sueldo >= 4000:
            print(sueldo)

def promedio_sueldos(sul):
    suma = sum(sul)
    promedio = suma//len(sul)
    print(f"El promedio de los sueldos es >>${promedio}<<")

sueldos = carga_sueldos()
superios_suledo(sueldos)
promedio_sueldos(sueldos)

mejora adicional:
def promedio_sueldos(sul):
    if len(sul) == 0:
        print("No se ingresaron sueldos.")
        return
    suma = sum(sul)
    promedio = suma // len(sul)
    print(f"El promedio de los sueldos es >> ${promedio} <<")

def articles():
    nom=[]
    pre=[]
    for x in range(2):
      val1=str(input("Ingrese nombre del articulo:"))
      nom.append(val1)
      val2=int(input("Ingrese precio del articulo:"))
      pre.append(val2)
    return [nom,pre]
def lista_articles(nom,pre):
    print("Lista de articulos:")
    for x in range(len(nom)):
     print(nom[x] + ":" ,"$"+ str(pre[x]) )

def article_mayor(nom,pre):
   mayor= pre[0]
   poo =0
   for x in range(1,len(pre)):
      if pre[x] > mayor:
         mayor= pre[x]
         poo=x
   print("Articulo de mayor precio es :", nom[poo], "$",mayor )

def importt(nom, pre):
   val = int(input("Ingrese un impote para los articulos de menor precio:"))
   for x in range(len(pre)):
      if pre[x]< val:
         print(nom[x], "$",pre[x])
   

nombres,precios=articles()
lista_articles(nombres,precios)
article_mayor(nombres,precios)
importt(nombres,precios)

def carga_datos():
    list = []
    for x in range(5):
     num = int(input("Ingrese un numero:"))
     list.append(num)
    return list
    
def generate_list(list):
   positive=[]
   negative=[]
   for number in list:
      if number >=0:
         positive.append(number)
      elif number <= 0:
         negative.append(number)
   print(f"numeros positivos: {positive} \n numeros negativos:{negative}")
   return[positive, negative]

numerot=carga_datos()
generate_list(numerot)

def cargar_numero(multiplicador,termino=11):
    for x in range(termino):
        multiplo = x * multiplicador 
        print(multiplo, "," ,sep="", end=" ")
    print()
cargar_numero()