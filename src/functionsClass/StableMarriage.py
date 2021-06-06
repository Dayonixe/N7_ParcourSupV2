def marriage(students: list, schools: list, verbose: bool) -> int:
    """
    Main algorithm
    @param students: List of students
    @param schools: List of schools
    @param verbose: If the display is more complete
    @return: Number of rounds
    """

    nbRound = 1
    notAssignedStudents = students  # At the beginning, every student don't have a school

    while not (len(notAssignedStudents) == 0):
        # Morning : Every students without school apply for their preferred
        for student in notAssignedStudents:
            school = student.getFirstChoice()
            school.addCandidate(student)
        notAssignedStudents = list()

        # Afternoon : Schools check if their capacity isn't exceeded. If so, they remove the least preferred student
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

        # Evening : Less desired students delete their first choice
        for student in notAssignedStudents:
            student.removeFirstChoice()

        if verbose:
            print()

        nbRound += 1

    return nbRound
