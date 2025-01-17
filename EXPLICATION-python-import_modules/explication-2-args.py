#!/usr/bin/python3

# Importation de 'argv' depuis le module sys
# 'argv' est une liste qui contient les arguments passés au script depuis la ligne de commande.
from sys import argv

# Vérification si le fichier est exécuté directement (et non importé dans un autre fichier)
if __name__ == "__main__":

    # 'argv[1:]' extrait tous les arguments passés au script, sauf le premier élément (qui est le nom du script lui-même).
    args = argv[1:]

    # 'num_args' est le nombre d'arguments passés après le nom du script.
    num_args = len(args)

    # Affiche le nombre d'arguments. Si num_args est différent de 1, on met un 's' au mot 'argument' pour le rendre pluriel.
    # La fonction 'end=""' permet de ne pas ajouter un saut de ligne automatiquement après le premier print.
    print(f"{num_args} argument{'s' if num_args != 1 else ''}", end="")

    # Si aucun argument n'est passé (num_args == 0), on affiche un point, sinon on affiche un deux-points.
    if num_args == 0:
        print(".")
    else:
        print(":")

    # Boucle pour afficher chaque argument avec son indice.
    # 'enumerate(args, 1)' retourne à la fois l'indice (commençant à 1) et l'argument.
    for i, arg in enumerate(args, 1):
        # Affiche l'indice de l'argument et l'argument lui-même.
        print(f"{i}: {arg}")

