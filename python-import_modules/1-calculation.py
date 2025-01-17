#!/usr/bin/python3

# Le shebang ci-dessus permet au script d'être exécuté avec l'interpréteur Python 3 si ce fichier est exécuté sur un système Unix/Linux.

# Importation des fonctions nécessaires depuis le fichier calculator_1.
# On importe spécifiquement les fonctions add (addition), sub (soustraction), div (division) et mul (multiplication).
# Cela permet d'utiliser ces fonctions dans le code sans avoir à les redéfinir.
from calculator_1 import add, sub, div, mul

# La condition suivante vérifie si le fichier est exécuté directement et non importé en tant que module dans un autre script.
# Si le fichier est exécuté directement, __name__ est égal à "__main__".
if __name__ == "__main__":
    # Définition de la variable 'a' avec la valeur 10.
    a = 10
    # Définition de la variable 'b' avec la valeur 5.
    b = 5

    # La première ligne de print affiche le résultat de l'addition entre a et b.
    # La fonction 'add(a, b)' calcule la somme de a et b, qui donne ici 10 + 5 = 15.
    # La méthode format() remplace les accolades {} dans la chaîne par les valeurs correspondantes : a, b et le résultat de l'addition.
    print("{} + {} = {}".format(a, b, add(a, b)))

    # La deuxième ligne de print affiche le résultat de la soustraction entre a et b.
    # La fonction 'sub(a, b)' calcule la différence entre a et b, ici 10 - 5 = 5.
    # La méthode format() insère les valeurs de a, b et le résultat de la soustraction dans la chaîne de caractères.
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # La troisième ligne de print affiche le résultat de la multiplication entre a et b.
    # La fonction 'mul(a, b)' calcule le produit de a et b, soit 10 * 5 = 50.
    # La méthode format() insère a, b et le résultat de la multiplication dans la chaîne.
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # La quatrième ligne de print affiche le résultat de la division entre a et b.
    # La fonction 'div(a, b)' calcule le quotient de a divisé par b, ici 10 / 5 = 2.0.
    # La méthode format() insère a, b et le résultat de la division dans la chaîne.
    # Si b était égal à zéro, la fonction div gérerait l'erreur en renvoyant un message d'erreur.
    print("{} / {} = {}".format(a, b, div(a, b)))

