#!/usr/bin/python3

# Cette condition garantit que le code sera exécuté uniquement lorsqu'il est lancé directement
# et non lorsqu'il est importé dans un autre fichier Python.
if __name__ == "__main__":

    # Importation de 'argv' depuis le module sys. 
    # 'argv' contient les arguments passés au script via la ligne de commande.
    from sys import argv

    # Initialisation de la variable 'int_sum' à 0. Elle servira à stocker la somme des arguments.
    int_sum = 0

    # Boucle qui parcourt les arguments passés au script, en ignorant le premier (argv[0] qui est le nom du script)
    # On commence la boucle à partir de l'indice 1 pour commencer à traiter les vrais arguments (argv[1], argv[2], etc.).
    for i in range(1, len(argv)):
        # On convertit chaque argument en entier avec int(argv[i]) et on l'ajoute à 'int_sum'.
        int_sum += int(argv[i])

    # Affichage de la somme de tous les arguments passés.
    print("{}".format(int_sum))

