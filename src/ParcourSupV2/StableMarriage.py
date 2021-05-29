def marriage(students: list, schools: list) -> int:
    nbRound = 0
    notAssignedStudents = students # At the beginning, every student have not school

    while not (len(notAssignedStudents) == 0):
        # Morning : Every students without school apply for their preferred
        for student in students:
            school = student.getFirstChoice()
            school.addCandidate(student)
        notAssignedStudents = list()

        # Afternoon : Schools check if their capacity isn't exceeded, if it is, they remove their less preferred student
        for school in schools:
            if school.isCapacityExceeded():
                for refusedStudent in school.declineStudent():
                    notAssignedStudents.append(refusedStudent)

        # Evening : Less desired students erase their first choice
        for student in notAssignedStudents:
            student.removeFirstChoice()

        nbRound += 1

    return nbRound
