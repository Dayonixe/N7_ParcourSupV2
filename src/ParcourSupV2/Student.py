from src.ParcourSupV2.School import School


class Student:
    """
    Class student
    """
    def __init__(self, name: str) -> None:
        """
        Constructor of student class with name
        :param name: name of the student
        """
        self.name = name
        self.preferences = list()

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
        :return: First school on the preferences list
        """
        return self.preferences[0]

    def getName(self) -> str:
        """
        Get the name of the student
        :return: The name
        """
        return self.name

    def removeFirstChoice(self) -> bool:
        """
        Remove the actual first choice of the student
        :return: True if the first choice has been removed, False otherwise (the list is empty)
        """
        if len(self.preferences) > 0:
            self.preferences.pop(0)
            return True
        else:
            return False    # ERROR!