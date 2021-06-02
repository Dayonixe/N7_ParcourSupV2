from parseFile import parseFile as ps
from userInteraction import userInteraction as ui

from ParcourSupV2 import StudentModule
from ParcourSupV2 import SchoolModule
from ParcourSupV2 import StableMarriage

import test

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


def afficheRes(schools: list) -> None:
    print("RESULT")
    print("======")
    for i in range(0, len(schools)):
        print("{}.".format(i))
        print("school : {}".format(schools[i].getName()))
        print("student : ", end="")
        for student in schools[i].getCandidates():
            print("{} ".format(student.getName()), end="")
        print()


def main():
    students = list()
    schools = list()

    # 1. Vérification de présence du fichier (sinon affichage d'un warning)
    fileName = ui.nameFile()
    if not ps.presenceFile(fileName):
        print("Le fichier n'est pas présent")
        exit(-1)

    bind = ui.whoBiding()
    data = ps.parseCSV(fileName)
    #print(data)
    #print(len(data))
    #print(ps.getNameCol(data))
    #print("Le nombre de colonnes est de : " + str(ps.getNbCol(data)))
    #print(ps.getNameRow(data))
    #print("Le nombre de lignes est de : " + str(ps.getNbRow(data)))
    #print(ps.getPrefCol(data))
    #print(ps.getPrefRow(data))

    # 2. Demande à l'utilisateur qui fait l'association
    studentsDict = dict()
    schoolsDict = dict()
    if bind == "R":
        studentsDict = ps.getPrefCol(data)
        schoolsDict = ps.getPrefRow(data)
    else:
        studentsDict = ps.getPrefRow(data)
        schoolsDict = ps.getPrefCol(data)


        # création de tous les étudiants avec leur nom
    for studentName in studentsDict.keys():
        students.append(StudentModule.Student(studentName))

        # creation de toutes les écoles avec leur nom et préférences
    for schoolName in schoolsDict.keys():
        school = SchoolModule.School(schoolName)
        preferences = list()
        for studentName in schoolsDict[schoolName]:
            preferences.append(getElmtByName(students, studentName))
        school.setPreferences(preferences)
        schools.append(school)

        # ajoute des préférences aux étudiants
    for student in students:
        preferences = list()
        for schoolName in studentsDict[student.getName()]:
            preferences.append(getElmtByName(schools, schoolName))
        student.setPreferences(preferences)

    # 3. Demander à l'utilisateur les capacités de chaque école
    for school in schools:
        capa = ui.schoolCapacity(school.getName())
        school.setCapacity(capa)

    # 4. Vérification : sum(ecole.capacité) >= sum(eleves)
    totalCapa = 0
    for school in schools:
        totalCapa += school.getCapacity()

    if totalCapa < len(students):
        raise ValueError("Not enough places for all students : sum(school.capacity) < sum(students)")

    # 5. Exécution de l'algorithme
    nbRound = StableMarriage.marriage(students, schools, False)

    # 6. Output
    afficheRes(schools)
    print("Nombre de round : {}".format(nbRound))

if __name__ == '__main__':
    main()