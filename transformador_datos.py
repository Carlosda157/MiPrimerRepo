""""
Diseña una biblioteca de utilidades para validar y dar formato a información ingresada por un usuario.

"""
from datetime import date

"""
VALIDACIONES Y TRANSFORMACIONES
"""


def es_telefono_valido(numero: str) -> bool:
    return numero.isdigit() and len(numero) == 9


def formatear_telefono(numero: str) -> str:
    # Formato estándar: +51-XXX-XXX-XXX
    return f"+51-{numero[0:3]}-{numero[3:6]}-{numero[6:]}"


def es_anio_valido(anio: str) -> bool:
    if not (anio.isdigit() and len(anio) == 4):
        return False

    anio_int = int(anio)
    anio_actual = date.today().year
    # Valida un rango coherente (ej: entre 1900 y el año actual)
    return 1900 <= anio_int <= anio_actual


def calcular_edad(anio_nacimiento: str) -> int:
    return date.today().year - int(anio_nacimiento)


def es_email_valido(correo: str) -> bool:
    correo_limpio = correo.strip().lower()
    return correo_limpio.endswith("@gmail.com") and len(correo_limpio) > len("@gmail.com")


"""
ENTRADAS DE DATOS POR CONSOLA
"""


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
        num = input("Número telefónico (9 dígitos): ").strip()
        if es_telefono_valido(num):
            return num
        print("❌ Ingresa un número celular válido de 9 dígitos.")


def pedir_anio_nacimiento() -> str:
    while True:
        fech = input("Año de nacimiento (AAAA): ").strip()
        if es_anio_valido(fech):
            return fech
        print("❌ Ingrese un año de nacimiento válido.")


def pedir_email() -> str:
    while True:
        corr = input("Correo electrónico: ").strip()
        if es_email_valido(corr):
            return corr.lower()
        print("❌ Correo no válido. Debe terminar en @gmail.com")


def pedir_datos_persona() -> dict:
    """Pide todos los datos de UNA persona, incluido su correo."""
    print("\n--- Ingreso de Datos ---")
    nombre = input("Nombre completo: ").strip().title()
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
    cantidad = pedir_entero_positivo("Digite el número de personas a registrar: ")
    personas = []
    for i in range(cantidad):
        print(f"\n👤 Persona {i + 1} de {cantidad}")
        personas.append(pedir_datos_persona())
    return personas


def mostrar_datos(personas: list[dict]) -> None:
    print(f"\nSe han ingresado {len(personas)} persona(s) a la lista.")
    print("=" * 70)
    print("DATOS DE CLIENTES REGISTRADOS")
    print("=" * 70)
    print(f"{'CLIENTE':<22}{'EDAD':<8}{'TELÉFONO':<18}{'CORREO'}")
    print("-" * 70)
    for p in personas:
        print(f"{p['nombre']:<22}{p['edad']:<8}{p['telefono']:<18}{p['correo']}")
    print("=" * 70)


def main():
    personas = pedir_datos()
    mostrar_datos(personas)


if __name__ == "__main__":
    main()