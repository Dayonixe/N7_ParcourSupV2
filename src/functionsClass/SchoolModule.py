class School:

    def __init__(self, name: str) -> None:
        """
        Constructor of the School Class with name
        """
        self.name = name
        self.capacity = 0
        self.preferences = list()
        self.candidate = list()

    def setCapacity(self, capacity: int) -> None:
        """
        Set the capacity of the school
        :param capacity:
        """
        self.capacity = capacity

    def setPreferences(self, preferences: list) -> None:
        """
        Associate the list of preferences as a parameter to the object
        :param preferences:
        """
        self.preferences = preferences

    def addCandidate(self, student):
        """
        Add a candidate to the school
        :param student: candidate to add
        """
        self.candidate.append(student)

    def isCapacityExceeded(self) -> bool:
        """
        If the capacity of the school is exceeded
        :return: Boolean
        """
        if len(self.candidate) > self.capacity:
            return True
        else:
            return False

    def getCapacity(self) -> int:
        """
        Get the capacity of the school
        :return: The capacity
        """
        return self.capacity

    def getName(self) -> str:
        """
        Get the name of the school
        :return: The name
        """
        return self.name

    def getCandidates(self) -> list:
        """
        Get candidates
        :return:
        """
        return self.candidate

    def declineStudent(self) -> list:
        """
        The capacity of the school is exceeded, the least preferred students are withdrawn and expelled.
        :return: list of student
        """
        declinedStudentList = list()

        def getPreferenceOf(student) -> int:
            """
            Get the index of the student in the preferences
            :param student:
            :return: Index
            """
            for i in range(0, len(self.preferences)):
                if self.preferences[i] == student:
                    return i

        def getLessFavorite():
            """
            Get and remove the less preferred student of the candidate list
            :return:
            """
            # Get the place (the index) of the less preferred student
            index = 0
            higherPreference = 0
            for y in range(0, len(self.candidate)):
                preferenceStudent = getPreferenceOf(self.candidate[y])
                if preferenceStudent > higherPreference:
                    higherPreference = preferenceStudent
                    index = y

            # Remove him from the candidate list
            student = self.candidate[index]
            self.candidate.pop(index)

            # return him
            return student

        # Get all less preferred students
        while len(self.candidate) > self.capacity:
            declinedStudentList.append(getLessFavorite())

        return declinedStudentList
