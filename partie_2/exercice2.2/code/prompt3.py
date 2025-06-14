
"""
Prompt avec Multiple Exemples (Few-Shot prompting) :
Reprenez le prompt précédent et ajoutez un deuxième exemple d'entrée-sortie:
format_product_code("XYZ987GHIJ") devrait retourner "XYZ-987-GHIJ", incluant un cas
d'erreur : format_product_code("SHORT") devrait lever une ValueError.
Question : L'IA gère-t-elle mieux les cas d'erreur maintenant ? La robustesse a-t-elle été
améliorée ?
"""

def format_product_code(code: str) -> str:
  """
  Met en forme un code produit de 10 caractères au format XXX-XXX-XXXX.

  Args:
    code: La chaîne de caractères du code produit à formater.

  Returns:
    Le code produit formaté avec des tirets.

  Raises:
    ValueError: Si le code produit n'a pas une longueur de 10 caractères.
  """
  if len(code) != 10:
    raise ValueError("Le code produit doit contenir exactement 10 caractères.")
  
  # Sépare le code en trois parties et les joint avec des tirets
  part1 = code[:3]
  part2 = code[3:6]
  part3 = code[6:]
  
  return f"{part1}-{part2}-{part3}"