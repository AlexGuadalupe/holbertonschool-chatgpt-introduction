#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcula el factorial de un número dado.

    Args:
        n (int): El número del cual calcular el factorial.

    Returns:
        int: El factorial de n.

    Raises:
        ValueError: Si n es negativo.
    """
    if n < 0:  # Comprueba si n es negativo
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0:  # Si n es 0, el factorial es 1
        return 1
    else:
        return n * factorial(n-1)  # Calcula el factorial recursivamente

if __name__ == "__main__":
    if len(sys.argv) != 2:  # Verifica que se proporcione exactamente un argumento (además del nombre del script)
        print("Uso: python3 nombre_script.py numero")  # Imprime un mensaje de uso
        sys.exit(1)  # Sale del programa con un código de error

    try:
        n = int(sys.argv[1])  # Convierte el argumento en un entero
        f = factorial(n)  # Calcula el factorial de n
        print(f)  # Imprime el resultado
    except ValueError as e:
        print(e)  # Imprime un mensaje de error si no se proporciona un número válido
        sys.exit(1)  # Sale del programa con un código de error si hay un error
