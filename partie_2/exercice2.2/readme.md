
# Analyse d'Expériences de Prompt Engineering avec Gemini

Ce document analyse les résultats d'une série d'expériences de "prompt engineering" menées avec le modèle de langage Gemini. L'objectif est d'observer comment différentes techniques de prompt (Zéro-Shot, One-Shot, Few-Shot) influencent la qualité, la correction et la robustesse du code Python généré.

## Expérience 1 : Prompt Zéro-Shot (Basé sur la Règle)

#### **Prompt**

```
"Crée une fonction Python format_product_code(product_id). Le product_id doit être une
chaîne de 10 caractères alphanumériques. La fonction doit insérer un tiret après le 3ème et le
7ème caractère. Si la chaîne n'a pas 10 caractères ou contient des caractères non
alphanumériques, elle doit lever une ValueError. Inclue un docstring."
```

#### **Code Généré (Version 1)**

```python
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
```

#### **Analyse**

* **Le code est-il correct ?**
    Oui, le code est **parfaitement correct**. Il respecte toutes les instructions : le nom, la logique de formatage (`XXX-XXXX-XXX`), la gestion des erreurs et le docstring sont implémentés comme demandé.

* **Est-il robuste face aux erreurs ?**
    Oui, le code est **très robuste**. Il inclut même une validation de type (`isinstance`) qui n'était pas explicitement demandée, en plus de vérifier la longueur et la nature alphanumérique des caractères.

---

## Expérience 2 : Prompt One-Shot (Avec un Exemple)

#### **Prompt**

```
"Crée une fonction Python format_product_code(product_id). ... Voici un exemple d'entrée-sortie:
format_product_code("ABC123DEF4") devrait retourner "ABC-123-DEF4". La fonction doit
lever une ValueError si l'entrée est invalide. Inclue un docstring."
```

#### **Code Généré (Version 2)**

```python
def format_product_code(product_id):
  """Formate un ID de produit alphanumérique de 10 caractères."""
  # ... (vérifications des erreurs) ...
  if not isinstance(product_id, str) or not product_id.isalnum():
    raise ValueError("L'ID produit doit être une chaîne alphanumérique.")
  if len(product_id) != 10:
    raise ValueError("L'ID produit doit contenir exactement 10 caractères.")

  # Formate la chaîne en utilisant le f-string slicing
  return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"
```

#### **Analyse**

* **Comparer avec le résultat précédent. L'exemple a-t-il simplifié la tâche de l'IA ? A-t-il aidé à éviter des erreurs ?**
    L'exemple a clarifié l'intention sur le format de sortie, mais il a aussi **introduit une incohérence**. La règle initiale ("après le 3ème et 7ème caractère") impliquait un format `XXX-XXXX-XXX`. L'exemple (`ABC-123-DEF4`) montre un format `XXX-XXX-XXXX`. L'IA a **privilégié l'exemple sur la règle implicite**, modifiant la logique de formatage. Loin d'éviter une erreur, il a changé le comportement pour correspondre à un exemple qui contredisait la première demande. La robustesse de la gestion des erreurs reste cependant excellente.

---

## Expérience 3 : Prompt Few-Shot (Avec Plusieurs Exemples)

#### **Prompt**

```
"Reprenez le prompt précédent et ajoutez un deuxième exemple d'entrée-sortie:
format_product_code("XYZ987GHIJ") devrait retourner "XYZ-987-GHIJ", incluant un cas
d'erreur : format_product_code("SHORT") devrait lever une ValueError."
```

#### **Code Généré (Version 3)**

```python
def format_product_code(code: str) -> str:
  """Met en forme un code produit de 10 caractères au format XXX-XXX-XXXX."""
  if len(code) != 10:
    raise ValueError("Le code produit doit contenir exactement 10 caractères.")

  # Sépare le code en trois parties et les joint avec des tirets
  part1 = code[:3]
  part2 = code[3:6]
  part3 = code[6:]

  return f"{part1}-{part2}-{part3}"
```

#### **Analyse**

* **L'IA gère-t-elle mieux les cas d'erreur maintenant ? La robustesse a-t-elle été améliorée ?**
    Non, c'est tout le contraire. La gestion des erreurs s'est **considérablement dégradée**. En fournissant un exemple d'erreur portant uniquement sur la longueur (`"SHORT"`), l'IA a "sur-appris" de cet exemple et a **totalement omis la vérification des caractères alphanumériques (`.isalnum()`)**. La robustesse a donc été **nettement réduite**, rendant la fonction vulnérable à des entrées invalides comme `"ABC-!@#XYZ"`.

---

## Analyse Critique

#### **1) Comment l'ajout d'exemples a-t-il influencé la capacité de l'IA à générer le code ?**

L'ajout d'exemples a eu une influence à double tranchant :

* **Clarification du format** : L'exemple du prompt "One-Shot" a permis de définir sans ambiguïté un format de sortie (`XXX-XXX-XXXX`), ce qui peut être plus simple que de le décrire textuellement. L'IA a parfaitement suivi cet exemple concret.

* **Introduction de biais et "sur-apprentissage"** : L'influence des exemples peut devenir négative si ceux-ci ne sont pas exhaustifs. Dans le prompt "Few-Shot", l'exemple d'erreur ne portait que sur la longueur. L'IA a interprété cela comme la *seule* condition d'erreur pertinente et a abandonné la contrainte `alphanumérique` pourtant présente dans la demande initiale. **L'IA a donc tendance à donner plus de poids aux exemples concrets qu'aux règles abstraites**, ce qui peut simplifier la tâche mais aussi la rendre moins complète si les exemples ne couvrent pas tous les cas.

#### **2) Quand le "Few-Shot Prompting" est-il particulièrement utile en développement ?**

Le "Few-Shot Prompting" est particulièrement utile dans les scénarios suivants :

* **Pour des formats de sortie complexes** : Quand on souhaite générer du code qui produit une sortie dans un format très spécifique (ex: JSON structuré, XML, une classe avec un `__repr__` particulier), fournir quelques exemples est souvent plus efficace que de décrire le format en prose.
* **Pour des tâches de style et de ton** : Pour générer des commentaires de code, de la documentation ou des messages d'erreur avec un style particulier (formel, informel, technique), les exemples guident l'IA bien mieux que des adjectifs.
* **Pour des logiques difficiles à décrire** : Si une transformation de données est complexe à expliquer mais simple à montrer (ex: `transform("Jean Dupont") -> "J. DUPONT"`), quelques exemples permettent à l'IA d'inférer le pattern.
* **Pour "amorcer" un comportement** : En montrant un exemple d'une fonction et de son test unitaire, on peut demander à l'IA de générer des fonctions et des tests pour d'autres cas en suivant le même modèle.

#### **3) Y a-t-il des limites aux exemples (nombre, qualité) ?**

Oui, il y a des limites fondamentales, et cette expérience les illustre parfaitement.

* **Qualité > Quantité** : Mieux vaut quelques exemples de haute qualité qui couvrent une large gamme de cas que de nombreux exemples répétitifs. Un bon jeu d'exemples doit inclure :
    * Un ou deux cas de succès standards.
    * Des cas limites (ex: un code produit avec uniquement des chiffres ou des lettres).
    * **Des exemples pour chaque type d'erreur attendu**. Si nous avions inclus un exemple d'erreur pour un caractère non-alphanumérique dans le prompt 3, l'IA aurait probablement conservé la validation `isalnum`.

* **Risque de "sur-apprentissage"** : Comme démontré, le modèle peut se focaliser excessivement sur les détails des exemples fournis et ignorer des règles plus générales. Si les exemples ne sont pas représentatifs de l'ensemble du problème, le résultat sera biaisé et potentiellement incorrect pour les cas non illustrés.

* **Incohérence** : Si un exemple contredit une règle textuelle, le comportement de l'IA devient imprévisible. Dans notre cas, elle a privilégié l'exemple, mais ce n'est pas toujours garanti. Il est crucial d'assurer la cohérence entre les règles et les exemples.