# ParcourSupV2

Team : Charly Ginevra & Théo Pirouelle

<img src="https://img.shields.io/badge/laguage-python-blue?style=flat-square" alt="laguage-python" />

<img src="https://upload.wikimedia.org/wikipedia/fr/thumb/d/dc/Logo_parcoursup.svg/langfr-250px-Logo_parcoursup.svg.png" alt="parcoursup" style="zoom:40%;" />

---

## Table of contents

- [Project guidelines](#project-guidelines)
- [Implementation of the project](#implementation-of-the-project)
  - [Integrity constraints](#integrity-constraints)
  - [Actors](#actors)
  - [Algorithm](#algorithm)

---

## Project guidelines
Implement a student admission program using the stable marriage algorithm
Teams of 2

- Input
  - Student and school preferences from a file in the format used TD
  - User selects who does the biding
- Output
  - Student to school assignment
  - Number of rounds needed to converge
- Evaluation
  - Demo during last session, June 3
  - Report + code by June 13



## Implementation of the project

### Integrity constraints

- sum(ecole.capacité) >= sum(eleve)

### Acteurs

- École
  - Capacité
  - Préférences sur les élèves
  - Liste des postulants
- Élevé
  - Préférences sur les écoles

### Algorithme

- Input :
  - Données depuis un fichier `.csv` placé à la racine du projet
  - Demande à l'utilisateur qui fait l'association (lignes/colonnes)
  - Demande à l'utilisateur les capacités de chaque école
- Output :
  - Nombre de round
  - Résultat dans la console (+ dans le `.csv`)
- Arrêt du code :
  - Lorsque tous les élèves ont une école
  - Lorsqu'il n'y a plus de conflit (conflit = capacité d'une école dépassée)

#### Description des différents types

##### Etudiant

```python
class student:
  def __init__(self, preferences):
    self.preferences = preferences

  def getFirstChoice(self):
    return self.preferences[0]

  def removeFirstChoice(self):
    self.preferences.pop(0)
```

##### Ecole
```python
class school:
  def __init__(self, capacity, preferences):
    self.capacity = capacity
    self.preferences = prefences
    self.postulants = list()

  def isOverLoaded():
```

##### Etapes d'exécution 

1. Vérification de présence du fichier (sinon affichage d'un warning)
2. Demande à l'utilisateur qui fait l'association
3. Demander à l'utilisateur les capacités de chaque école
4. Vérification : sum(ecole.capacité) >= sum(eleve)
5. Exécution de l'algorithme
6. Output

##### Fonction

```
// nom : marriage_algo
// sémantique: effectue l'algorithme du marriage stable pour parcousupv2
// paramètres:
// écoles : In/Out list<école>; -- Rôle du paramètre
// étudiants : In/Out list<étudiant>; -- liste d'étudiants
// nbRound : Out Envier; -- nombre round pour la résolution du problème
// pré-condition: sum(ecole.capacité) >= sum(eleve)
// post-condition: 
//      -- Tous les étudiants sont répartis dans les "postulants" des différentes écoles
//      -- Tous les étudiants possèdent une école
fonction marriage_algo(étudiants: list<étudiant>; écoles: list<école>) : Integer
début
    nbRound := 0
    etudiants_non_assignés := copy(etudiants)
    tant que (non etudiants_non_assignés.est_vide()) faire
        // Matin : Tous les etudiants sans école postulent à une école
        pour etudiant dans etudiants_non_assignés faire
            prefSchool := etudiant.getFirstChoice()
            prefSchool.addPostulant(etudiant)
        fpour
        etudiants_non_assignés := list() // remise à zéro de la liste

        // Après-midi : Les écoles vérifient si leur capacité n'est pas dépassée, auquel cas elle supprime les étudiants les moins désirés
        pour ecole dans ecoles faire
            si ecole.surchagé alors // conflit
                pour eleve dans ecole.refuseEleves() faire
                    etudiants_non_assignés.append(eleve)
                fpour
            fsi
        fpour

        // Soir : Les étudiants les moins désirés supprime leur premier choix
        pour etudiant dans etudiants_non_assignés faire
            etudiant.supprimerPremierChoix()
        fpour

        nbRound := nbRound + 1
        
    ftant
        
    retourne nbRound
fin
```

*Note: l'ouvrire avec le plugin **algo** de vscode*
