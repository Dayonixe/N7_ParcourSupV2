from parseFile import parseFile as ps
from userInteraction import userInteraction as ui

from ParcourSupV2 import *

# Programme principal
def getElmtByName(list, name):
    """
    :param list: list of student or school
    :param name: name searched
    :return:
    """
    for elmt in list:
        if elmt.getName() == name:
            return elmt


def main():
    students = list()
    schools = list()

    # 1. Vérification de présence du fichier (sinon affichage d'un warning)
    fileName = ui.nameFile()
    if ps.presenceFile(fileName):
        bind = ui.whoBiding()
        data = ps.parseCSV(fileName)
        print(data)
        print(len(data))
        print(ps.getNameCol(data))
        print("Le nombre de colonnes est de : " + str(ps.getNbCol(data)))
        print(ps.getNameRow(data))
        print("Le nombre de lignes est de : " + str(ps.getNbRow(data)))

    # 2. Demande à l'utilisateur qui fait l'association
        # création de tous les étudiants avec leur nom
    for studentName in dict.keys():
        students.append(Student(studentName))

        # creation de toutes les écoles avec leur nom et préférences
    for schoolName in dict.keys():
        school = School(schoolName)
        preferences = list()
        for studentName in dict[schoolName]:
            preferences.append(getElmtByName(students, studentName))
        school.setPreferences(preferences)
        schools.append(school)

        # ajoute des préférences aux étudiants
    for student in students:
        preferences = list()
        for schoolName in dict[student.getName()]:
            preferences.append(getElmtByName(school, schoolName))
        student.setPreferences(preferences)

    # 3. Demander à l'utilisateur les capacités de chaque école


    # 4. Vérification : sum(ecole.capacité) >= sum(eleves)
    totalCapa = 0
    for school in schools:
        totalCapa += school.getCapacity()

    if totalCapa < len(students):
        raise ValueError("Not enough places for all students : sum(school.capacity) < sum(students)")

    # 5. Exécution de l'algorithme
    nbRound = StableMarriage.marriage(students, schools)

    # 6. Output

if __name__ == '__main__':
    main()