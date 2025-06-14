#prompt 2
"""
Prompt Spécifique :
"Écris une fonction Python appelée calculate(a, b, op) qui prend deux entiers a et b, et une chaîne op indiquant '+', '-', '*', ou '/'. La fonction doit retourner le résultat de l’opération, gérer les erreurs (division par zéro, opération invalide) et arrondir le résultat de la division à deux décimales. Ajoute un docstring détaillé et des commentaires."
Questions : Comparer la robustesse, la lisibilité et la couverture des cas
"""

def calculate(a, b, op):
    """
    Calcule le résultat d'une opération arithmétique entre deux nombres.

    Cette fonction prend deux nombres entiers et un opérateur sous forme de chaîne de
    caractères. Elle effectue l'opération spécifiée et retourne le résultat.
    Elle gère les cas d'erreur comme la division par zéro et les
    opérateurs invalides. Le résultat de la division est arrondi à deux
    décimales.

    Args:
        a (int): Le premier nombre (dividende pour la division).
        b (int): Le deuxième nombre (diviseur pour la division).
        op (str): L'opérateur. Doit être '+', '-', '*', ou '/'.

    Returns:
        float or int or str: Le résultat de l'opération.
                             Retourne un message d'erreur (str) si une
                             division par zéro est tentée ou si l'opérateur
                             est invalide.
    """
    # Vérifie si l'opérateur est l'un des opérateurs valides
    if op == '+':
        # Effectue l'addition
        return a + b
    elif op == '-':
        # Effectue la soustraction
        return a - b
    elif op == '*':
        # Effectue la multiplication
        return a * b
    elif op == '/':
        # Gère le cas spécifique de la division
        if b == 0:
            # Retourne un message d'erreur si le diviseur est zéro
            return "Erreur : La division par zéro n'est pas autorisée."
        else:
            # Effectue la division et arrondit le résultat à deux décimales
            return round(a / b, 2)
    else:
        # Gère le cas où l'opérateur n'est pas reconnu
        return "Erreur : Opération invalide. Veuillez utiliser '+', '-', '*', ou '/'."