""""
Diseña una biblioteca de utilidades para validar y dar formato a información ingresada por un usuario.

"""
from datetime import date

"""
validaciones y transformaciones

"""

def es_telefono_valido(numero: str) -> bool:
    return numero.isdigit() and len(numero) == 9

def formatear_telefono(numero: str) -> str:
    return f"+51-{numero[0:3]}-{numero[3:]}"


def es_anio_valido(anio: str) -> bool:
    return anio.isdigit() and len(anio) == 4

def calcular_edad(anio_nacimiento: str) -> int:
    return date.today().year - int(anio_nacimiento)

def es_email_valido(correo: str) -> bool:
    return correo.strip().endswith("@gmail.com") and len(correo.strip()) > len("@gmail.com")


"""ENTRADAS"""


def pedir_entero_positivo(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("Ingrese una cantidad mayor que 0.")
                continue
            return valor
        except ValueError:
            print("Ingrese una cantidad válida.")


def pedir_telefono() -> str:
    while True:
        num = input("Número: ").strip()
        if es_telefono_valido(num):
            return num
        print("Ingresa un número válido de 9 dígitos.")


def pedir_anio_nacimiento() -> str:
    while True:
        fech = input("Ingrese el año de nacimiento (formato AAAA): ").strip()
        if es_anio_valido(fech):
            return fech
        print("Ingrese un año válido.")


def pedir_email() -> str:
    while True:
        corr = input("Ingrese su correo: ").strip()
        if es_email_valido(corr):
            print("Correo válido guardado con éxito.")
            return corr
        print("Correo no válido. Debe terminar en @gmail.com")

def pedir_datos_persona() -> dict:
    """Pide todos los datos de UNA persona, incluido su correo."""
    nombre = input("Nombre: ").strip()
    numero = pedir_telefono()
    anio = pedir_anio_nacimiento()
    correo = pedir_email()
    return {
        "nombre": nombre,
        "telefono": formatear_telefono(numero),
        "edad": calcular_edad(anio),
        "correo": correo,
    }

def pedir_datos() -> list[dict]:
    cantidad = pedir_entero_positivo("Digite el número de personas a validar: ")
    personas = []
    for _ in range(cantidad):
        personas.append(pedir_datos_persona())
    return personas


def mostrar_datos(personas: list[dict]) -> None:
    print(f"\nSe han ingresado {len(personas)} personas a la lista.")
    print("-------Datos validados.-----")
    print("A continuación estos son los datos de los clientes:\n")
    print(f"{'CLIENTE':<20}{'EDAD':<10}{'TELÉFONO':<15}{'CORREO'}")
    for p in personas:
        print(f"{p['nombre']:<20}{p['edad']:<10}{p['telefono']:<15}{p['correo']}")



def main():
    personas = pedir_datos()
    mostrar_datos(personas)
 

if __name__ == "__main__":
    main()