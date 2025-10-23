from typing import Union


def multiplicar_por_sumas(a: int, b: int) -> int:
    """
    Multiplica a * b usando sumas repetidas.
    Maneja correctamente los signos.
    """
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
    # Evita que bool pase como int (en Python, bool es subclase de int)
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
    # Ejemplos simples de ejecución manual
    print("5 x 3 =", multiplicar_por_sumas(5, 3))     # 15
    print("(-4) x 6 =", multiplicar_por_sumas(-4, 6)) # -24
    print("0! =", factorial(0))                       # 1
    print("5! =", factorial(5))                       # 120
