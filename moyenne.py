"""Ce module fournit une fonction pour calculer une moyenne de valeurs"""

# NB: Ce fichier contient du code à compléter

from rich.console import Console
from rich.markdown import Markdown


def moyenne(valeurs):
    """
    # Calcule la moyenne des valeurs.

    **Paramètres**
    - `valeurs` : valeurs dont on veut calculer la moyenne

    **Retour**
    - la moyenne des valeurs

    **Exceptions**
    - `ValueError` : si la liste est vide

    ---
    """
    # docstrings en markdown
    if valeurs == []:
        raise ValueError("la liste est vide")
    else:
        s = 0
        n = len(valeurs)
        for i in range(n):
            s += valeurs[i]
        return s / n
    print("!! TODO : Compléter la fonction moyenne !!", end=" ")


if __name__ == "__main__":
    Console().print(Markdown(moyenne.__doc__))
    print("moyenne([10, 20, 15]) :", end=" ")
    print(moyenne([10, 20, 15]))
