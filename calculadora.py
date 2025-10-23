from typing import Union


def multiplicar_por_sumas(a: int, b: int) -> int:
    """
    Multiplica a * b usando sumas repetidas.
    Maneja correctamente los signos y valida tipos.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos valores deben ser números enteros.")

    if b < 0:
        a, b = -a, -b

    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado


def factorial(n: Union[int, bool]) -> int:
    """
    Calcula el factorial de n (n!).
    Reglas:
      - n debe ser entero >= 0
      - 0! = 1
    Excepciones:
      - TypeError si n no es entero o es booleano.
      - ValueError si n es negativo.
    """
    if isinstance(n, bool):
        raise TypeError("El factorial requiere un entero, no un booleano.")

    if not isinstance(n, int):
        raise TypeError("El factorial requiere un entero.")

    if n < 0:
        raise ValueError("El factorial no está definido para n < 0.")

    resultado = 1
    for k in range(2, n + 1):
        resultado *= k
    return resultado


def pedir_entero(mensaje: str) -> int:
    """
    Solicita un número entero al usuario.
    Si ingresa una letra u otro valor inválido, vuelve a pedirlo.
    """
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("⚠️ Entrada inválida. Por favor ingrese un número entero.")


if __name__ == "__main__":
    print("=== Programa de Prueba ===")

    # Pedir valores con validación
    a = pedir_entero("Ingrese el primer número (a): ")
    b = pedir_entero("Ingrese el segundo número (b): ")

    try:
        print(f"\nResultado de {a} x {b} =", multiplicar_por_sumas(a, b))
    except Exception as e:
        print(f"⚠️ Error en multiplicación: {e}")

    n = pedir_entero("\nIngrese un número para calcular su factorial: ")

    try:
        print(f"\nEl factorial de {n} es {factorial(n)}")
    except Exception as e:
        print(f"⚠️ Error al calcular factorial: {e}")

    print("\n✅ Programa finalizado correctamente.")
