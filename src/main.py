from functionsClass.parseFile import parseFile as ps
from functionsClass.userInteraction import userInteraction as ui

from functionsClass import StudentModule
from functionsClass import SchoolModule
from functionsClass import StableMarriage


# Main program
def getElmtByName(list: list, name: str):
    """
    Items retrieval by name
    :param list: List of students or schools
    :param name: Searched name
    :return: Element
    """
    for elmt in list:
        if elmt.getName() == name:
            return elmt

def displayResult(schools: list) -> None:
    """
    Display of the result
    :param schools: List of students or schools
    """
    print("\n" + "=============================="
          + "\n|           RESULT           |"
          + "\n==============================\n")
    for i in range(0, len(schools)):
        print("{}. ===========================".format(i+1))
        print("| School : {}".format(schools[i].getName()))
        print("| Student(s) : ", end="")
        for student in schools[i].getCandidates():
            print("{} ".format(student.getName()), end="")
        print("\n==============================\n")


def main():
    students = list()
    schools = list()

    # 1. Check for the presence of the file (otherwise a warning is displayed)
    fileName = ui.nameFile()
    if not ps.presenceFile(fileName):
        exit(-1)

    bind = ui.whoBiding()
    data = ps.parseCSV(fileName)

    # 2. Ask the user who makes the binding
    studentsDict = dict()
    schoolsDict = dict()
    if bind == "R":
        studentsDict = ps.getPrefCol(data)
        schoolsDict = ps.getPrefRow(data)
    else:
        studentsDict = ps.getPrefRow(data)
        schoolsDict = ps.getPrefCol(data)

        # Creation of all students with their names
    for studentName in studentsDict.keys():
        students.append(StudentModule.Student(studentName))

        # Creation of all schools with their names and preferences
    for schoolName in schoolsDict.keys():
        school = SchoolModule.School(schoolName)
        preferences = list()
        for studentName in schoolsDict[schoolName]:
            preferences.append(getElmtByName(students, studentName))
        school.setPreferences(preferences)
        schools.append(school)

        # Adding preferences to students
    for student in students:
        preferences = list()
        for schoolName in studentsDict[student.getName()]:
            preferences.append(getElmtByName(schools, schoolName))
        student.setPreferences(preferences)

    # 3. Ask the user about the capacities of each school
    for school in schools:
        capa = ui.schoolCapacity(school.getName())
        school.setCapacity(capa)

    # 4. Check: sum(school.capacity) < sum(students)
    totalCapa = 0
    for school in schools:
        totalCapa += school.getCapacity()

    if totalCapa < len(students):
        raise ValueError("Not enough places for all students : sum(school.capacity) < sum(students)")

    # 5. Running the algorithm
    nbRound = StableMarriage.marriage(students, schools, False)

    # 6. Output
    displayResult(schools)
    print("> Number of rounds : \033[92m{}\033[0m".format(nbRound))

if __name__ == '__main__':
    main()