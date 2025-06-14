#prompt 1

"""
Prompt Vague :
"Écris une fonction pour faire des opérations entre deux nombres en Python."
Questions : La fonction est-elle nommée ? Quelles opérations sont prises en charge ? Y a-t-il une gestion des erreurs ? Des commentaires ?
"""

def operation(nombre1, nombre2, operateur):
  """
  Effectue une opération arithmétique de base entre deux nombres.

  Cette fonction prend deux nombres et un symbole d'opérateur en tant
  qu'arguments et retourne le résultat du calcul.

  Args:
    nombre1 (int | float): Le premier nombre de l'opération.
    nombre2 (int | float): Le deuxième nombre de l'opération.
    operateur (str): L'opérateur à utiliser. Doit être '+', '-', '*', ou '/'.

  Returns:
    int | float | str: Le résultat du calcul, ou un message d'erreur si
                       l'opération est invalide (par exemple, division par zéro)
                       ou si l'opérateur n'est pas reconnu.
  """
  if operateur == '+':
    return nombre1 + nombre2
  elif operateur == '-':
    return nombre1 - nombre2
  elif operateur == '*':
    return nombre1 * nombre2
  elif operateur == '/':
    # Vérifier si le deuxième nombre est zéro pour éviter une erreur de division
    if nombre2 == 0:
      return "Erreur : La division par zéro n'est pas autorisée."
    return nombre1 / nombre2
  else:
    # Retourner une erreur si l'opérateur n'est pas l'un des quatre valides
    return "Erreur : Opérateur non valide. Veuillez utiliser '+', '-', '*' ou '/'."