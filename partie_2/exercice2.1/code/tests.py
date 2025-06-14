import pytest

# --- Importation des fonctions depuis leurs fichiers respectifs ---
# Pour que cela fonctionne, les fonctions doivent être dans ces fichiers
# ou vous pouvez copier leurs définitions directement ici.

# Version 1 (Prompt Vague)
from prompt1 import operation as operation_v1

# Version 2 (Prompt Spécifique)
from prompt2 import calculate as calculate_v2

# Version 3 (Prompt avec Persona)
from prompt3 import calculate as calculate_v3


# === Tests pour la Fonction 1 (Prompt Vague) ===

def test_v1_addition():
    """V1: Teste une addition simple."""
    assert operation_v1(10, 5, '+') == 15

def test_v1_division_par_zero():
    """V1: Teste que la division par zéro retourne le message d'erreur attendu."""
    assert operation_v1(10, 0, '/') == "Erreur : La division par zéro n'est pas autorisée."

def test_v1_operateur_invalide():
    """V1: Teste qu'un opérateur invalide retourne le message d'erreur attendu."""
    assert operation_v1(10, 5, '%') == "Erreur : Opérateur non valide. Veuillez utiliser '+', '-', '*' ou '/'."

def test_v1_division_normale():
    """V1: Teste une division standard sans arrondi."""
    assert operation_v1(10, 4, '/') == 2.5


# === Tests pour la Fonction 2 (Prompt Spécifique) ===

def test_v2_soustraction():
    """V2: Teste une soustraction simple."""
    assert calculate_v2(10, 5, '-') == 5

def test_v2_division_avec_arrondi():
    """V2: Teste que le résultat de la division est bien arrondi à deux décimales."""
    assert calculate_v2(10, 3, '/') == 3.33

def test_v2_division_par_zero():
    """V2: Teste la gestion de l'erreur de division par zéro."""
    assert calculate_v2(5, 0, '/') == "Erreur : La division par zéro n'est pas autorisée."

def test_v2_operateur_invalide():
    """V2: Teste la gestion d'un opérateur non reconnu."""
    assert calculate_v2(10, 2, 'x') == "Erreur : Opération invalide. Veuillez utiliser '+', '-', '*', ou '/'."


# === Tests pour la Fonction 3 (Prompt avec Persona) ===

def test_v3_multiplication():
    """V3: Teste une multiplication simple."""
    assert calculate_v3(10, 5, '*') == 50.0

def test_v3_division_par_zero_leve_une_erreur():
    """V3: Vérifie qu'une ValueError est levée lors d'une division par zéro."""
    with pytest.raises(ValueError) as excinfo:
        calculate_v3(10, 0, '/')
    # Vérifie que le message d'erreur est correct
    assert "La division par zéro n'est pas autorisée" in str(excinfo.value)

def test_v3_operateur_invalide_leve_une_erreur():
    """V3: Vérifie qu'une ValueError est levée pour un opérateur invalide."""
    with pytest.raises(ValueError) as excinfo:
        calculate_v3(10, 5, '#')
    assert "Opérateur '#' non valide" in str(excinfo.value)

def test_v3_type_de_retour_flottant():
    """V3: Vérifie que le type de retour est bien un flottant."""
    assert isinstance(calculate_v3(5, 5, '+'), float)
    assert calculate_v3(5, 2, '+') == 7.0


"""
Pour exécuter tous ces tests, il vous suffit de lancer la commande suivante dans votre terminal, en vous assurant d'être dans le bon dossier :

$ pytest test.py

"""