from src.ParcourSupV2.Student import Student


class School:
    """
    Class School
    """

    def __init__(self, capacity: int, preferences: list) -> None:
        """
        Constructor of the class school
        :param capacity: capacity of the school
        :param preferences: preferences of the school
        """
        self.capacity = capacity
        self.setPreferences(preferences)
        self.candidate = list()

    def setPreferences(self, preferences: list) -> None:
        """
        Associate the list of preferences in parameter to the object
        :param preferences:
        :return:
        """
        self.preferences = preferences

    def addCandidate(self, student: Student):
        """
        Add a candidate to the school
        :param student: candidate to add
        :return:
        """
        self.candidate.append(student)

    def isCapacityExceeded(self) -> bool:
        """
        if the capacity of the school is exceeded
        :return:
        """
        if len(self.candidate) > self.capacity:
            return True
        else:
            return False

    def declineStudent(self) -> list:
        """
        The capacity of the school is exceed, removes and returns the less preferred students
        :return: list of student
        """
        declinedStudentList = list()

        def indexOf(student: Student) -> int:
            """
            Get the index of the student in the preferences
            :param student:
            :return: index
            """
            for i in range(0, len(self.preferences)):
                if self.preferences[i] == student:
                    return i
            return -1

        def getLessFavorite() -> Student:
            """
            Get and remove the less preferred student of the candidate list
            :return:
            """
            # Get the place (the index) of the less preferred student
            index = 0
            for student in self.candidate:
                indexStudent = indexOf(student)
                if indexStudent > index:
                    index = indexStudent

            # Remove him from the candidate list
            student = self.candidate[index]
            self.candidate.pop(index)

            # return him
            return student

        # Get all less preferred students
        while len(self.candidate) > self.capacity:
            declinedStudentList.append(getLessFavorite())

        return declinedStudentList
