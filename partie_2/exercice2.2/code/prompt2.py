

"""
Prompt avec un Exemple (One-Shot Prompting) :
"Crée une fonction Python format_product_code(product_id). Le product_id doit être une
chaîne de 10 caractères alphanumériques. Voici un exemple d'entrée-sortie:
format_product_code("ABC123DEF4") devrait retourner "ABC-123-DEF4". La fonction doit
lever une ValueError si l'entrée est invalide. Inclue un docstring."
Question : Comparer avec le résultat précédent. L'exemple a-t-il simplifié la tâche de l'IA ? A-
t-il aidé à éviter des erreurs ?

"""

def format_product_code(product_id):
  """Formate un ID de produit alphanumérique de 10 caractères.

  Cette fonction prend une chaîne de 10 caractères alphanumériques et
  insère des tirets pour la formater en trois parties, comme "ABC-123-DEF4".

  Args:
    product_id: Une chaîne de caractères de 10 caractères alphanumériques
                (A-Z, a-z, 0-9).

  Returns:
    La chaîne de l'ID produit formatée avec des tirets.

  Raises:
    ValueError: Si l'entrée n'est pas une chaîne de caractères, ne fait pas
                exactement 10 caractères ou contient des caractères non
                alphanumériques.
  """
  # Vérifie si l'entrée est une chaîne et si elle est alphanumérique
  if not isinstance(product_id, str) or not product_id.isalnum():
    raise ValueError("L'ID produit doit être une chaîne alphanumérique.")

  # Vérifie si la longueur est exactement de 10 caractères
  if len(product_id) != 10:
    raise ValueError("L'ID produit doit contenir exactement 10 caractères.")

  # Formate la chaîne en utilisant le f-string slicing
  return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"
