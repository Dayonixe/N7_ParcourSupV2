from src.ParcourSupV2.School import School


class Student:
    """
    Class student
    """
    def __init__(self) -> None:
        """
        Constructor of student class
        """
        pass

    def __init__(self, preferences: list) -> None:
        """
        Constructor of student class with list of preferences
        :param preferences:
        """
        self.setPreferences(preferences)

    def setPreferences(self, preferences: list) -> None:
        """
        Associate the list of preferences in parameter to the object
        :param preferences:
        :return:
        """
        self.preferences = preferences

    def getFirstChoice(self) -> School:
        """
        Get the student's school first choice
        :return:
        """
        return self.preferences[0]

    def removeFirstChoice(self) -> bool:
        """
        Remove the actual first choice of the student
        :return:
        """
        if len(self.preferences) > 0:
            self.preferences.pop(0)
            return True
        else:
            return False
