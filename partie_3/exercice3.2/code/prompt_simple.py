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