### **Devoir : Ingénierie de Prompts pour le Refactoring de Code**

#### **Question 1 : Analyser le code fourni**

Voici le fragment de code initial pour l'expérience.

```python
a = [5, 3, 8, 6, 7, 2]
for i in range(len(a)):
  for j in range(i+1, len(a)):
    if a[i] > a[j]:
      tmp = a[i]
      a[i] = a[j]
      a[j] = tmp
print(a)
```

**Analyse :**

* **Fonction :** Le script trie une liste d'entiers par ordre croissant en utilisant un algorithme de tri par sélection de base.
* **Défauts :**
    1.  **Non structuré :** La logique n'est pas dans une fonction, ce qui la rend non réutilisable.
    2.  **Noms non explicites :** Les variables comme `a`, `i`, `j` et `tmp` ne décrivent pas clairement leur but.
    3.  **Absence de commentaires :** Aucune explication n'est fournie sur le but ou la logique du code.

---

#### **Question 2 : Première Expérience - Prompt Simple**

Un prompt simple et général a été utilisé pour voir comment l'IA effectuerait une refactorisation de base.

**Prompt 1 (Simple) :**
> "Bonjour, peux-tu refactoriser le code Python ci-dessous pour le rendre plus lisible, structuré et réutilisable ?"

**Résultat de l'IA (Prompt Simple) :**

L'IA a réussi à encapsuler le code dans une fonction et à améliorer les noms de variables. Cependant, il s'agit toujours d'une implémentation de base qui manque de fonctionnalités professionnelles et qui a pour effet de bord de modifier la liste originale.

```python
def trier_liste(nombres_a_trier):
    """
    Trie une liste de nombres par ordre croissant.
    """
    longueur_liste = len(nombres_a_trier)
    for i in range(longueur_liste):
        for j in range(i + 1, longueur_liste):
            if nombres_a_trier[i] > nombres_a_trier[j]:
                # Échange les éléments
                valeur_temp = nombres_a_trier[i]
                nombres_a_trier[i] = nombres_a_trier[j]
                nombres_a_trier[j] = valeur_temp
    return nombres_a_trier

# Exemple d'utilisation :
liste_initiale = [5, 3, 8, 6, 7, 2]
print(f"Liste originale : {liste_initiale}")

liste_triee = trier_liste(liste_initiale)
print(f"Liste triée : {liste_triee}")
# Note : La liste originale est également modifiée car la fonction n'a pas travaillé sur une copie.
print(f"Liste originale après le tri : {liste_initiale}")
```

---

#### **Question 3 : Deuxième Expérience - Prompt Avancé avec Contraintes**

Cette expérience visait à voir comment l'ajout de contraintes techniques spécifiques améliorerait le résultat de l'IA.

**Prompt 2 (Avancé) :**
> "Pour cette refactorisation, merci de respecter **impérativement** toutes les contraintes suivantes :
> 1.  **Convention PEP 8**
> 2.  **Ajouter des Docstrings complètes**
> 3.  **Séparer en fonctions modulaires**
> 4.  **Utiliser des noms explicites**
> 5.  **Ajouter un bloc `if __name__ == "__main__"`**"

**Résultat de l'IA (Prompt Avancé) :**

Le prompt détaillé a guidé l'IA pour produire un module professionnel, robuste et bien documenté. Le code est maintenant modulaire, sûr (il ne modifie pas les données originales) et identifie correctement l'algorithme utilisé.

```python
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
```

---

### **Comparaison et Conclusion de l'Expérience**

La comparaison des résultats des prompts simple et avancé démontre clairement l'efficacité de l'ingénierie de prompts détaillée.

| Caractéristique | Résultat du Prompt Simple | Résultat du Prompt Avancé |
| :--- | :--- | :--- |
| **Structure** | Une seule fonction de base. | Fonctions `main` et `tri_par_selection` séparées. |
| **Modularité** | Faible. Le code n'est pas fait pour être importé. | Élevée, grâce au bloc `if __name__ == "__main__"`. |
| **Documentation** | Une `docstring` très simple. | `Docstrings` complètes pour le module et les fonctions. |
| **Sécurité du code** | **Dangereux :** Modifie la liste originale (effet de bord). | **Sûr :** Travaille sur une copie (`.copy()`), laissant l'original intact. |
| **Clarté** | Noms de variables corrects. | Noms explicites, commentaires et annotations de type (`typing`). |
| **Professionnalisme**| Niveau amateur. | Niveau professionnel, prêt à l'emploi. |

**Conclusion :**

Cette expérience montre que bien qu'une IA puisse comprendre une requête générale, la qualité du résultat est directement proportionnelle au détail et à la spécificité du prompt. Le prompt simple a produit un script fonctionnel mais imparfait. Le **prompt avancé**, avec ses contraintes techniques claires, a guidé l'IA pour produire un code non seulement meilleur, mais qui suit également les normes de développement logiciel professionnel, y compris la modularité, la sécurité et la documentation complète. Cela met en évidence le principe fondamental de l'ingénierie de prompts : **de meilleures instructions mènent à de meilleurs résultats.**