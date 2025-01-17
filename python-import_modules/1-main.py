#!/usr/bin/python3

from calculator_1 import add, subtract, multiply, divide  # Importation des fonctions

if __name__ == "__main__":  # Vérifie que le script est exécuté directement
    a = 10
    b = 5

    # Appel des fonctions et affichage des résultats
    result_add = add(a, b)
    result_subtract = subtract(a, b)
    result_multiply = multiply(a, b)
    result_divide = divide(a, b)

    # Affichage des résultats de manière concise
    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_subtract))
    print("{} * {} = {}".format(a, b, result_multiply))
    print("{} / {} = {}".format(a, b, result_divide))
