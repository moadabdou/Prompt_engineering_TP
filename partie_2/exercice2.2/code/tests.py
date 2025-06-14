# test_all_versions.py
import pytest

# ======================================================================================
# VERSION 1: FONCTION GÉNÉRÉE PAR "ZÉRO-SHOT PROMPTING"
# ======================================================================================
def format_product_code_v1(product_id: str) -> str:
  """
  Version 1 : Robuste et suit la règle "après le 3ème et 7ème caractère".
  Format : XXX-XXXX-XXX
  """
  if not isinstance(product_id, str) or not product_id.isalnum() or len(product_id) != 10:
    raise ValueError("L'ID du produit doit être une chaîne de 10 caractères alphanumériques.")
  return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"


# ======================================================================================
# VERSION 2: FONCTION GÉNÉRÉE PAR "ONE-SHOT PROMPTING"
# ======================================================================================
def format_product_code_v2(product_id: str) -> str:
  """
  Version 2 : Robuste et suit le format de l'exemple.
  Format : XXX-XXX-XXXX
  """
  # Le type-hinting a été ajouté pour la cohérence des tests, mais n'était pas dans la sortie originale.
  if not isinstance(product_id, str) or not product_id.isalnum():
    raise ValueError("L'ID produit doit être une chaîne alphanumérique.")
  if len(product_id) != 10:
    raise ValueError("L'ID produit doit contenir exactement 10 caractères.")
  return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"


# ======================================================================================
# VERSION 3: FONCTION GÉNÉRÉE PAR "FEW-SHOT PROMPTING"
# ======================================================================================
def format_product_code_v3(code: str) -> str:
  """
  Version 3 : Non robuste, a "oublié" la validation isalnum.
  Format : XXX-XXX-XXXX
  """
  if len(code) != 10:
    raise ValueError("Le code produit doit contenir exactement 10 caractères.")
  # Cette version est vulnérable à une TypeError si l'entrée n'est pas une chaîne.
  # Et elle ne valide pas les caractères alphanumériques.
  part1 = code[:3]
  part2 = code[3:6]
  part3 = code[6:]
  return f"{part1}-{part2}-{part3}"


# ======================================================================================
# SUITE DE TESTS UNITAIRES PARAMÉTRISÉE
# On liste toutes les fonctions à tester.
# ======================================================================================
all_functions_to_test = [
    format_product_code_v1,
    format_product_code_v2,
    format_product_code_v3
]

# Le "fixture" ci-dessous permet de passer chaque fonction à tour de rôle aux tests.
@pytest.fixture(params=all_functions_to_test)
def format_function(request):
    return request.param

# --- Tests de formatage ---

def test_format_rule1_3_4_3(format_function):
    """Teste le formatage XXX-XXXX-XXX."""
    if format_function.__name__ == 'format_product_code_v1':
        assert format_function("ABC1234XYZ") == "ABC-1234-XYZ"
    else:
        # Les autres versions ne suivent pas cette règle, donc on s'attend à une erreur.
        with pytest.raises(AssertionError):
            assert format_function("ABC1234XYZ") == "ABC-1234-XYZ"

def test_format_rule2_3_3_4(format_function):
    """Teste le formatage XXX-XXX-XXXX."""
    if format_function.__name__ in ['format_product_code_v2', 'format_product_code_v3']:
        assert format_function("ABC123DEF4") == "ABC-123-DEF4"
    else:
        # La v1 ne suit pas cette règle.
        with pytest.raises(AssertionError):
            assert format_function("ABC123DEF4") == "ABC-123-DEF4"

# --- Tests des cas d'erreur ---

def test_raises_error_for_short_input(format_function):
    """Doit lever ValueError pour une chaîne trop courte."""
    with pytest.raises(ValueError):
        format_function("SHORT")

def test_raises_error_for_long_input(format_function):
    """Doit lever ValueError pour une chaîne trop longue."""
    with pytest.raises(ValueError):
        format_function("THISISWAYTOOLONG")

def test_raises_error_for_non_alnum_input(format_function):
    """Doit lever ValueError pour des caractères non alphanumériques."""
    if format_function.__name__ == 'format_product_code_v3':
        # On s'attend à ce que ce test échoue pour la v3, car elle est boguée.
        # Un test comme celui-ci documente la régression.
        with pytest.raises(AssertionError, match="DID NOT RAISE <class 'ValueError'>"):
             with pytest.raises(ValueError):
                format_function("ABC-DEF-G4")
    else:
        # Les versions 1 et 2 doivent passer ce test.
        with pytest.raises(ValueError):
            format_function("ABC-DEF-G4")

def test_raises_error_for_non_string_input(format_function):
    """Doit lever une erreur si l'entrée n'est pas une chaîne (str)."""
    # La v3 lève une TypeError, tandis que v1/v2 lèvent une ValueError.
    # Le test doit donc accepter les deux types d'erreurs.
    with pytest.raises((ValueError, TypeError)):
        format_function(1234567890)