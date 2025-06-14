
"""
Prompt basé sur la Règle (zéro-Shot Prompting) :
"Crée une fonction Python format_product_code(product_id). Le product_id doit être une
chaîne de 10 caractères alphanumériques. La fonction doit insérer un tiret après le 3ème et le
7ème caractère. Si la chaîne n'a pas 10 caractères ou contient des caractères non
alphanumériques, elle doit lever une ValueError. Inclue un docstring."
Question : Le code est-il correct ? Est-il robuste face aux erreurs ?

"""

def format_product_code(product_id: str) -> str:
  """Formate un ID de produit en insérant des tirets.

  Cette fonction prend un ID de produit alphanumérique de 10 caractères
  et insère un tiret après le 3ème et le 7ème caractère.

  Args:
    product_id: Une chaîne de 10 caractères alphanumériques.

  Returns:
    La chaîne de l'ID de produit formatée avec des tirets
    (par exemple, 'ABC-1234-XYZ').

  Raises:
    ValueError: Si l'ID de produit n'a pas 10 caractères ou
                contient des caractères non alphanumériques.
  """
  if not isinstance(product_id, str) or not product_id.isalnum() or len(product_id) != 10:
    raise ValueError("L'ID du produit doit être une chaîne de 10 caractères alphanumériques.")
  
  return f"{product_id[:3]}-{product_id[3:7]}-{product_id[7:]}"
