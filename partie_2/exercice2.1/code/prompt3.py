#prompt 3 
"""
 Prompt avec Persona :
"En tant que développeur Python, écris une fonction calculate(a, b, op) qui prend deux entiers et une chaîne représentant une opération mathématique ('+', '-', '*', '/'). La fonction doit être robuste, bien documentée, gérer les erreurs (division par zéro, opérateur invalide), arrondir les divisions à deux décimales, et respecter les conventions PEP8. Inclue un docstring et des commentaires clairs."
Questions : Le code est-il plus professionnel ? Mieux structuré ? Plus sécurisé ?
"""

def calculate(a, b, op):
    """
    Effectue une opération arithmétique de base entre deux nombres.

    Cette fonction prend deux entiers et une chaîne de caractères représentant
    l'opérateur. Elle gère l'addition, la soustraction, la multiplication
    et la division, tout en incluant une gestion des erreurs pour les
    opérateurs invalides et la division par zéro.

    Args:
        a (int): Le premier nombre (dividende pour la division).
        b (int): Le deuxième nombre (diviseur pour la division).
        op (str): L'opérateur mathématique ('+', '-', '*', '/').

    Returns:
        float: Le résultat de l'opération. Pour la division, le résultat
               est arrondi à deux décimales.

    Raises:
        ValueError: Si l'opérateur est invalide ou si une division par
                    zéro est tentée.
    """
    # Liste des opérateurs autorisés pour validation
    allowed_operators = ['+', '-', '*', '/']

    # Vérifie si l'opérateur fourni est valide
    if op not in allowed_operators:
        raise ValueError(
            f"Opérateur '{op}' non valide. "
            f"Utilisez l'un des suivants : {', '.join(allowed_operators)}"
        )

    # Exécute l'opération correspondante
    if op == '+':
        return float(a + b)
    elif op == '-':
        return float(a - b)
    elif op == '*':
        return float(a * b)
    elif op == '/':
        # Gère le cas de la division par zéro avant de faire le calcul
        if b == 0:
            raise ValueError("La division par zéro n'est pas autorisée.")
        # Effectue la division et arrondit le résultat à deux décimales
        return round(a / b, 2)