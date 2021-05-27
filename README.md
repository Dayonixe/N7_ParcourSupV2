# ParcourSupV2

Team : Charly Ginevra & Théo Pirouelle

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

- nbEcole <= nbEleve
- sum(ecole.capacité) >= sum(eleve)

### Actors

- Ecole
  - Capacité
  - Préférences sur les elèves
- Elève
  - Préférences sur les écoles

### Algorithm

- Input :
  - Données depuis un fichier `.csv` ou `.json` placé à la racine du projet
  - Demande à l'utilisateur qui fait l'association (lignes/colonnes)
  - Demande à l'utilisateur les capacités de chaque école
- Output :
  - Nombre de round
  - Résultat dans la console (+ dans le `.csv`)
- Arrêt du code :
  - Lorsque tous les élèves ont une école
  - Lorsqu'il n'y a plus de conflit (conflit = capacité d'une école dépassée)

```python
# Vérification de présence du fichier (sinon affichage d'un warning)
# Demande à l'utilisateur qui fait l'association
# Demande à l'utilisateur les capacités de chaque école
# Vérification : sum(ecole.capacité) >= sum(eleve)
# Exécution de l'algorithme
def marriage_algo(etudiants, ecoles):
    return {res, nbRound}
# Output
```
