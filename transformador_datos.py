""""
Diseña una biblioteca de utilidades para validar y dar formato a información ingresada por un usuario.

"""
from datetime import date
nombres = []
numeros = []
numeros_format = []
correo = []
correo_valid = []
años = []
fecha_nacimiento = []
def pedir_datos():
    i=0
    while True:
        try:
            personas = int(input("Digite el numero de personas a validar:"))
            if((personas<=0)):
                print("Ingrese una cantidad mayor que 0.")
                continue
        except ValueError:
            print("Ingrese una cantidad valida.")
            continue
        while True:
            name = input("Nombre:")
            num = input("Numero:")
            if(len(num)==9):
                numeros.append(num)
                nombres.append(name)
            else:
                print("Ingresa un numero valido de 9 digitos.")
                continue
            
            fech = input("Ingrese la fecha de nacimiento formato (año):")
            if(len(fech)==4):
                fecha_nacimiento.append(fech)
                i += 1
                if i >= personas:
                    break
            else:
                print("Ingrese un año valido.")
                continue
        break
    return personas

def formatear_telefono(numeros):
    for numero in numeros:
        numeros_format.append(f"+51-{numero[0:3]}-{numero[3:]}")

def validar_email(correo, correo_valid):
    while True:
        corr = input("Ingrese su correo: ").strip()

        # Verifica si termina en @gmail.com y tiene texto antes del @
        if corr.endswith("@gmail.com") and len(corr) > 10:
            correo.append(corr)
            correo_valid.append(corr)
            print("Correo válido guardado con éxito.")
            valor = True
            break
        else:
            print("Correo no válido. Debe terminar en @gmail.com")           
    return valor     



def calcular_edad(fecha_nacimiento):
    fecha_actual = date.today()
    formato = fecha_actual.strftime("%Y")
    for fecha in fecha_nacimiento:
        
        años.append(int(formato) - int(fecha))


def mostrar_datos():
    per=pedir_datos()
    varr = validar_email(correo, correo_valid) 
    formatear_telefono(numeros)
    calcular_edad(fecha_nacimiento)
    if(varr == True):
        print(f"se ha ingresado {per} personas a la lista.")
        print("""-------Datos validados.-----
A continuacion estos son los datos de los clientes:\n""")
        print("CLIENTE              EDAD                        TELEFONO")
        for i in range(per):
            print(f"{nombres[i]}       |        {años[i]}            |            {numeros_format[i]}")
        


mostrar_datos()

