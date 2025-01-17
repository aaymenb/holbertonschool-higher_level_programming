#!/usr/bin/python3

# Importation des fonctions nécessaires depuis le fichier calculator_1.py
# Ces fonctions vont nous permettre de faire des opérations de base comme l'addition, la soustraction, la multiplication et la division.
from calculator_1 import add, sub, div, mul

# Cette condition garantit que le code suivant sera exécuté seulement si ce fichier est exécuté directement,
# et non lorsqu'il est importé dans un autre script Python.
if __name__ == "__main__":
    # Définition des variables 'a' et 'b' avec les valeurs 10 et 5 respectivement
    a = 10
    b = 5

    # Affichage du résultat de l'addition de 'a' et 'b'
    # La méthode format() est utilisée pour insérer les valeurs de 'a', 'b' et le résultat de l'addition dans la chaîne de caractères.
    print("{} + {} = {}".format(a, b, add(a, b)))
    
    # Affichage du résultat de la soustraction de 'b' de 'a'
    print("{} - {} = {}".format(a, b, sub(a, b)))
    
    # Affichage du résultat de la multiplication de 'a' et 'b'
    print("{} * {} = {}".format(a, b, mul(a, b)))
    
    # Affichage du résultat de la division de 'a' par 'b'
    # La fonction div() retourne un résultat en type float, même si la division est exacte
    print("{} / {} = {}".format(a, b, div(a, b)))

