def marriage(students: list, schools: list, verbose: bool) -> int:
    nbRound = 1
    notAssignedStudents = students  # At the beginning, every student have not school

    while not (len(notAssignedStudents) == 0):
        # Morning : Every students without school apply for their preferred
        for student in notAssignedStudents:
            # print("{} is not assigned".format(student.getName()))
            school = student.getFirstChoice()
            school.addCandidate(student)
        notAssignedStudents = list()

        # Afternoon : Schools check if their capacity isn't exceeded, if it is, they remove their less preferred student
        if verbose:
            print("Round {}".format(nbRound))

        for school in schools:
            if verbose:
                print(school.getName())
                print("Before :")
                for i in range(0, len(school.candidate)):
                    print("{}. {}".format(i, school.candidate[i].getName()))

            if school.isCapacityExceeded():
                for refusedStudent in school.declineStudent():
                    notAssignedStudents.append(refusedStudent)

            if verbose:
                print("After :")
                for i in range(0, len(school.candidate)):
                    print("{}. {}".format(i, school.candidate[i].getName()))

        # Evening : Less desired students erase their first choice
        for student in notAssignedStudents:
            student.removeFirstChoice()

        if verbose:
            print()

        nbRound += 1

    return nbRound
