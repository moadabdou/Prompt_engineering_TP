# Analyse d'Expériences de Prompt Engineering

Ce document analyse les résultats de trois expériences de prompt engineering menées avec un modèle de langage (IA) pour générer une fonction Python. Chaque section détaille le prompt utilisé, le code généré, et une analyse critique.

---

## Prompt 1 : Vague

### Le Prompt
```
"Écris une fonction pour faire des opérations entre deux nombres en Python."
```

### Code Généré
```python
def operation(nombre1, nombre2, operateur):
  """
  Effectue une opération arithmétique de base entre deux nombres.

  Args:
    nombre1 (int | float): Le premier nombre.
    nombre2 (int | float): Le deuxième nombre.
    operateur (str): L'opérateur. Doit être '+', '-', '*', ou '/'.

  Returns:
    int | float | str: Le résultat du calcul, ou un message d'erreur.
  """
  if operateur == '+':
    return nombre1 + nombre2
  elif operateur == '-':
    return nombre1 - nombre2
  elif operateur == '*':
    return nombre1 * nombre2
  elif operateur == '/':
    if nombre2 == 0:
      return "Erreur : La division par zéro n'est pas autorisée."
    return nombre1 / nombre2
  else:
    return "Erreur : Opérateur non valide. Veuillez utiliser '+', '-', '*' ou '/'."
```

### Analyse Initiale
* **Nom de la fonction :** `operation`.
* **Opérations prises en charge :** Addition (`+`), soustraction (`-`), multiplication (`*`), division (`/`).
* **Gestion des erreurs :** Oui, pour la division par zéro et les opérateurs invalides. Les erreurs sont retournées sous forme de chaînes de caractères (`str`).
* **Commentaires :** Oui, un `docstring` et des commentaires en ligne sont présents.

---

## Prompt 2 : Spécifique

### Le Prompt
```
"Écris une fonction Python appelée calculate(a, b, op) qui prend deux entiers a et b, et une chaîne op indiquant '+', '-', '*', ou '/'. La fonction doit retourner le résultat de l’opération, gérer les erreurs (division par zéro, opération invalide) et arrondir le résultat de la division à deux décimales. Ajoute un docstring détaillé et des commentaires."
```

### Code Généré
```python
def calculate(a, b, op):
    """
    Calcule le résultat d'une opération arithmétique entre deux nombres.
    Le résultat de la division est arrondi à deux décimales.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.
        op (str): L'opérateur. Doit être '+', '-', '*', ou '/'.

    Returns:
        float or int or str: Le résultat de l'opération ou un message d'erreur.
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Erreur : La division par zéro n'est pas autorisée."
        else:
            return round(a / b, 2)
    else:
        return "Erreur : Opération invalide. Veuillez utiliser '+', '-', '*', ou '/'."
```

### Analyse Initiale
* **Comparaison :** Par rapport à la V1, cette fonction est plus **robuste** car elle gère le cas spécifique de l'arrondi. Sa **lisibilité** est équivalente et sa **couverture des cas** est meilleure grâce à l'ajout de cette fonctionnalité précise.

---

## Prompt 3 : Avec Persona

### Le Prompt
```
"En tant que développeur Python, écris une fonction calculate(a, b, op) qui prend deux entiers et une chaîne représentant une opération mathématique ('+', '-', '*', '/'). La fonction doit être robuste, bien documentée, gérer les erreurs (division par zéro, opérateur invalide), arrondir les divisions à deux décimales, et respecter les conventions PEP8. Inclue un docstring et des commentaires clairs."
```

### Code Généré
```python
def calculate(a, b, op):
    """
    Effectue une opération arithmétique de base entre deux nombres.

    Args:
        a (int): Le premier nombre.
        b (int): Le deuxième nombre.
        op (str): L'opérateur mathématique ('+', '-', '*', '/').

    Returns:
        float: Le résultat de l'opération.

    Raises:
        ValueError: Si l'opérateur est invalide ou si une division par zéro est tentée.
    """
    if op not in ['+', '-', '*', '/']:
        raise ValueError(f"Opérateur '{op}' non valide.")

    if op == '/':
        if b == 0:
            raise ValueError("La division par zéro n'est pas autorisée.")
        return round(a / b, 2)
    
    # Utilisation d'eval() pour les autres opérations après validation
    # C'est une approche concise mais qui doit être utilisée avec prudence.
    # Ici, c'est sûr car l'opérateur et les nombres sont contrôlés.
    return float(eval(f"{a} {op} {b}"))
```

### Analyse Initiale
* **Professionnalisme et Structure :** Le code est **nettement plus professionnel**. Il utilise `raise ValueError` pour la gestion des erreurs, ce qui est la pratique standard en Python. C'est plus **robuste**, **fiable** et **mieux structuré**.
* **Sécurité :** L'utilisation de `raise` rend l'intégration de la fonction plus sûre dans une application plus large, car elle force la gestion des cas d'erreur.

---

## Analyse Critique

### 1) Différences observées entre les codes générés

Les différences sont progressives et significatives :
* **De Vague à Spécifique :** Le changement principal est l'ajout de fonctionnalités demandées explicitement. Le nom de la fonction est respecté (`calculate`) et une nouvelle logique (l'arrondi de la division) est implémentée. Le contrôle passe d'une IA créative à une IA qui suit des instructions.
* **De Spécifique à Persona :** La différence est **qualitative**. Le code ne se contente plus de "fonctionner", il est écrit en respectant les standards professionnels de Python. Le changement le plus marquant est le passage d'un retour de `str` pour les erreurs à l'utilisation de `raise ValueError`. Cette approche est plus robuste car elle sépare clairement le flux de succès (qui retourne un nombre) du flux d'erreur (qui lève une exception), évitant des bugs silencieux.

### 2) Quel principe de Prompt Engineering a eu le plus grand impact ?

Le principe de la **persona** a eu de loin le plus grand impact.

Alors que la **spécificité** a permis d'ajouter une fonctionnalité (l'arrondi), la **persona** ("En tant que développeur Python...") a fondamentalement modifié la *manière* dont le code est écrit. Elle a poussé l'IA à mobiliser ses connaissances sur les **meilleures pratiques**, les **conventions de style (PEP8)** et les **modèles de conception logicielle** (comme la gestion d'erreurs par exception).

En résumé, la spécificité dit à l'IA *quoi faire*, mais la persona lui dit *comment être*, ce qui aboutit à un résultat de qualité bien supérieure.

### 3) L'IA a-t-elle introduit des erreurs ou des comportements inattendus ?

Non, l'IA n'a introduit **aucune erreur de logique ou bug de calcul**. Toutes les fonctions font ce qu'on leur demande.

Cependant, on peut considérer que le retour d'une chaîne de caractères (`str`) en cas d'erreur dans les versions 1 et 2 est un **comportement inattendu et indésirable** dans un contexte professionnel. Un code qui appelle ces fonctions pourrait s'attendre à toujours recevoir un nombre et échouer de manière imprévisible s'il ne vérifie pas manuellement le type du résultat. La version 3 corrige ce défaut de conception.

### 4) Quel est le coût pour obtenir un code de haute qualité ?

Le coût (en temps et en effort) varie radicalement en fonction de la qualité du prompt.
* **Prompt Vague :** Le coût initial est **très faible**, mais le coût total est **très élevé**. Le code généré n'est qu'une ébauche. Un développeur doit investir un temps considérable pour le tester, le raffiner, corriger les défauts de conception (gestion d'erreurs), et s'assurer qu'il respecte les normes de qualité.
* **Prompt Spécifique/Persona :** Le coût initial est **plus élevé**. Il faut réfléchir et prendre le temps de rédiger une spécification claire et détaillée. Cependant, le coût total est **beaucoup plus faible**. Le code généré est quasiment prêt à l'emploi. L'effort est déplacé de la *rédaction et correction du code* vers la *rédaction du prompt*. C'est un gain d'efficacité spectaculaire, car l'IA se charge de la "sale besogne" de l'écriture du code idiomatique et robuste.