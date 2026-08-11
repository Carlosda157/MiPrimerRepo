'''
Un juego interactivo donde la computadora genera un número aleatorio del 1 al 100 y el usuario tiene que adivinarlo con intentos limitados.

'''
#dic = {
#    "carlos":22,
#    "mary": 21
#}




#for i in range(3):
        
 #   nombre = input("nombre:")
  #  edad = int(input("Edad:"))
   # dic[nombre] = edad
    #i+=1

#print(dic)

"""for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")


    #number 2"""

"""for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
"""
"""while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        """

"""def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)"""


"""
Un juego interactivo donde la computadora genera un número aleatorio del 1 al 100
y el usuario tiene que adivinarlo con intentos limitados.

"""
from random import randint

a = randint(1,100)
intentos = 5
list = [a]
while True:
    try:
        numero = int(input(f"Te quedan {intentos} intentos, ingrese un numero cualquiera:"))
    except ValueError:
        print("Ingrese un numero valido.")
        continue
    if not (1<=numero<=100):
        print("Ingrese un numero del 1-100.")
        continue
        
    if (list[0] == numero):
        print("Has ganado, el numero era: ",list[0])
        break
        

    elif(list[0]>numero):
        print("El numero es mayor.")

    else:
        print("El numero es menor.")

    intentos -= 1
    if intentos == 0 :
        print("Se acabaron tus intentos has perdido chaval. El numero era: ", list[0])
        break