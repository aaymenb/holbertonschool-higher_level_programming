#!/usr/bin/python3

# Importation de la variable 'a' depuis le fichier 'variable_load_5.py'.
# 'a' doit être définie dans ce fichier pour que l'importation fonctionne correctement.
from variable_load_5 import a

# Ce bloc assure que le code suivant sera exécuté uniquement lorsque ce fichier est exécuté directement
# (et non lorsqu'il est importé dans un autre fichier Python).
if __name__ == "__main__":
    # Affichage de la valeur de la variable 'a' qui a été importée depuis 'variable_load_5.py'
    print(a)

