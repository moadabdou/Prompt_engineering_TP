# -*- coding: utf-8 -*-

"""
Un module pour trier une liste de nombres en utilisant l'algorithme
du tri par sélection et pour démontrer son utilisation.
"""

from typing import List, Union

# Le type Union[int, float] permet d'accepter des listes d'entiers ou de flottants.
NumericList = List[Union[int, float]]


def tri_par_selection(liste_de_donnees: NumericList) -> NumericList:
    """Trie une liste de nombres en utilisant l'algorithme du tri par sélection.

    Cette implémentation crée une copie de la liste d'entrée pour éviter de la
    modifier (pas d'effet de bord) et retourne une nouvelle liste triée.

    Args:
        liste_de_donnees (List[Union[int, float]]): La liste de nombres à trier.

    Returns:
        List[Union[int, float]]: Une nouvelle liste contenant les nombres triés
                                 par ordre croissant.
    """
    # Crée une copie de la liste pour ne pas modifier l'originale.
    liste_triee = liste_de_donnees.copy()
    longueur_liste = len(liste_triee)

    # Parcours de tous les éléments de la liste.
    for i in range(longueur_liste):
        # Trouve l'index de l'élément minimum dans le reste de la liste
        index_min = i
        for j in range(i + 1, longueur_liste):
            if liste_triee[j] < liste_triee[index_min]:
                index_min = j
        
        # Echange l'élément minimum trouvé avec l'élément courant
        if index_min != i:
            liste_triee[i], liste_triee[index_min] = liste_triee[index_min], liste_triee[i]

    return liste_triee


def main():
    """Fonction principale pour exécuter un exemple de tri."""
    print("Démonstration du tri par sélection (selection sort).")
    nombres_exemple: NumericList = [5, 3, 8, 6, 7, 2]
    
    print(f"Liste originale : {nombres_exemple}")

    # Appel de la fonction de tri modulaire.
    nombres_tries = tri_par_selection(nombres_exemple)

    print(f"Liste triée : {nombres_tries}")
    print(f"La liste originale n'a pas été modifiée : {nombres_exemple}")


# Le bloc ci-dessous s'assure que la fonction main() est appelée uniquement
# lorsque le fichier est exécuté directement comme un script.
if __name__ == "__main__":
    main()