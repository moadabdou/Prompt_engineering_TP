# **Expérimentation : Prompt Vague vs. Prompt Détaillé**

Ce document résume une expérience visant à comparer les résultats d'un modèle d'IA lors de la génération d'une mini-application de calculatrice en HTML/CSS/JS à partir de deux prompts de qualité différente.

**Objectif :** Démontrer comment la précision des instructions influence la qualité, la robustesse et la sécurité du code généré.

## **Étape 1 : Le Prompt Vague**

Le point de départ est une instruction simple et non spécifique. L'IA doit combler les lacunes en faisant ses propres suppositions.

#### **Prompt Fourni :**

Crée une simple calculatrice avec HTML, CSS et JavaScript.

#### **Résultat Attendu :**

Un prototype fonctionnel mais minimaliste, probablement sans style avancé ni gestion robuste des erreurs, et potentiellement utilisant des raccourcis peu sécurisés comme la fonction eval().

## **Étape 2 : Le Prompt Détaillé et Technique**

La deuxième approche consiste à fournir un cahier des charges précis, incluant des contraintes techniques, stylistiques et fonctionnelles.

#### **Prompt Fourni :**

Crée une mini-application web de calculatrice en utilisant HTML, CSS et JavaScript.

**Structure HTML :**

* Utilise un conteneur principal avec la classe calculator.  
* À l'intérieur, crée un écran d'affichage non modifiable avec la classe display.  
* En dessous de l'écran, ajoute une grille de boutons avec la classe buttons-grid.

**Style CSS :**

* Centre la calculatrice au milieu de la page.  
* Applique un thème sombre (\#222 pour le fond du corps, \#333 pour la calculatrice).  
* L'écran (display) doit avoir une police de grande taille, du padding, et une couleur de texte blanche.  
* Les boutons doivent avoir des coins arrondis et un léger effet de hover.  
* Utilise une grille CSS (display: grid) pour aligner les boutons parfaitement.  
* Donne une couleur de fond différente aux boutons d'opérateurs (+, \-, \*, /) (par exemple, orange) et au bouton \= (par exemple, vert). Le bouton C (Clear) doit être rouge.

**Logique JavaScript :**

* Les boutons numériques (0-9) et le point décimal doivent ajouter leur valeur à l'écran.  
* Le bouton \= doit évaluer l'expression affichée et montrer le résultat.  
* Le bouton C doit effacer complètement l'affichage.  
* **Gestion des erreurs :**  
  * Gère la division par zéro en affichant "Erreur".  
  * Empêche l'ajout de plusieurs points décimaux dans le même nombre.  
  * Gère les saisies invalides (par exemple, 5 \* \* 5).  
* N'utilise pas la fonction eval().

## **Étape 3 : Évaluation Finale des Différences**

L'analyse comparative des deux codes produits révèle des écarts significatifs.

### **Analyse comparative des résultats**

En examinant le code des deux calculatrices, on observe des différences majeures sur trois axes principaux : la qualité visuelle (Style & UX), la robustesse du code (Logique & Gestion des erreurs) et le respect des bonnes pratiques (Sécurité).

#### **1\. Qualité Visuelle et Expérience Utilisateur (UX)**

* **Thème et Cohérence :**  
  * **Prompt 1 :** A un design clair et fonctionnel, mais générique.  
  * **Prompt 2 :** Applique parfaitement le **thème sombre** demandé, avec une hiérarchie visuelle claire grâce aux couleurs des boutons.  
* **Mise en Page et Finitions :**  
  * **Prompt 1 :** Utilise une grille CSS basique qui, en plus de manquer d'espacement, est **incorrectement implémentée**. L'IA a appliqué une largeur de deux colonnes (grid-column: span 2\) à la fois au bouton \= et au bouton 0, ce qui brise la symétrie de la grille et résulte en une disposition des boutons **illogique et non-standard**.  
  * **Prompt 2 :** Implémente une grille CSS parfaite avec gap pour l'espacement et une disposition logique des boutons, en plus d'ajouter des micro-interactions (transform au survol) pour une expérience plus moderne.  
* **Structure HTML :**  
  * **Prompt 1 :** Utilise un div pour l'affichage.  
  * **Prompt 2 :** Utilise un \<input type="text" readonly\>, sémantiquement plus correct, et des classes CSS plus spécifiques.

#### **2\. Robustesse et Gestion des Erreurs**

* **Gestion des Erreurs de Saisie :**  
  * **Prompt 1 :** N'a **aucune protection** contre les saisies incorrectes (5..++--//.3).  
  * **Prompt 2 :** Implémente une **logique de validation proactive** qui empêche les points décimaux multiples et les opérateurs consécutifs.  
* **Gestion des Erreurs de Calcul :**  
  * **Prompt 1 :** Ne gère pas spécifiquement la division par zéro (renverrait Infinity).  
  * **Prompt 2 :** Gère explicitement la division par zéro en vérifiant \!isFinite(result) et en affichant "Erreur".

#### **3\. Sécurité et Bonnes Pratiques**

* **Méthode de Calcul :**  
  * **Prompt 1 :** Utilise eval(), une pratique dangereuse qui présente des failles de sécurité (XSS).  
  * **Prompt 2 :** Respecte l'interdiction d'utiliser eval() et opte pour une alternative plus sécurisée (new Function()), démontrant de meilleures pratiques de développement.

### **Conclusion de l'Expérience**

Cette comparaison démontre que **la qualité d'un prompt est un investissement direct dans la qualité du résultat.**

* Le **prompt vague** a produit un **prototype fonctionnel**, une ébauche qui nécessite une révision significative.  
* Le **prompt détaillé** a agi comme un véritable **cahier des charges**, guidant l'IA pour produire une mini-application quasi complète, robuste, sécurisée et avec une expérience utilisateur réfléchie.