import sys


class userInteraction:
    @staticmethod
    def nameFile() -> str:
        """
        Asks the user for the name of the CSV file that contains the data
        :return: String
        """
        warningColor = '\033[93m'
        resetColor = '\033[0m'

        name = input("> Enter the CSV file name : ")
        checkName = name.split(".")

        if (len(checkName) < 2 or len(checkName) > 2 or checkName[1] != "csv"):
            print(warningColor + "Warning: Incorrect file name !"
                  + resetColor)
            sys.exit()

        return name

    @staticmethod
    def whoBiding() -> str:
        """
        Ask the user who makes the binding (rows/columns)
        :return: String
        """
        isValid = False
        while not isValid:
            bind = input("> Enter who makes the binding [Row/Col] : ")
            if (bind.lower() in ['r', 'row', 'rows', 'l', 'ligne', 'lignes']):
                return 'R'
            elif (bind.lower() in ['c', 'col', 'column', 'columns', 'colonne', 'colonnes']):
                return 'C'

    @staticmethod
    def schoolCapacity(name: str) -> int:
        """
        Asks the user what is the capacity of the school passed in parameter
        :param name: School's name
        :return: Integer
        """
        warningColor = '\033[93m'
        resetColor = '\033[0m'

        isValid = False
        while not isValid:
            capacity = input("> Enter the school's capacity '" + name + "' : ")
            try:
                intCapacity = int(capacity)
                if (intCapacity >= 0):
                    return intCapacity
                else:
                    print(warningColor + "Warning: The capacity must be higher than 0 !"
                          + resetColor)
            except:
                print(warningColor + "Warning: You must enter an integer !"
                      + resetColor)