from typing import Union

def multiplicar_por_sumas(a: int, b: int) -> int:
    """
    Multiplica a * b usando sumas repetidas.
    Maneja correctamente los signos.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos valores deben ser números enteros.")

    # Normaliza el signo para evitar bucles negativos
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
    Lanza ValueError si n es negativo y TypeError si no es entero.
    """
    if isinstance(n, bool):
        raise TypeError("El factorial requiere un entero, no un booleano")

    if not isinstance(n, int):
        raise TypeError("El factorial requiere un entero")

    if n < 0:
        raise ValueError("El factorial no está definido para n < 0")

    resultado = 1
    for k in range(2, n + 1):
        resultado *= k
    return resultado


if __name__ == "__main__":
    try:
        # Entradas del usuario
        a = int(input("Ingrese el primer número (a): "))
        b = int(input("Ingrese el segundo número (b): "))

        print(f"{a} x {b} =", multiplicar_por_sumas(a, b))

        n = int(input("Ingrese un número para calcular su factorial: "))
        print(f"{n}! =", factorial(n))

    except ValueError:
        print("⚠️ Error: debe ingresar solo números enteros válidos.")
    except TypeError as e:
        print(f"⚠️ Error de tipo: {e}")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")
