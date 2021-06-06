import csv


class parseFile:
    def presenceFile(name: str) -> bool:
        """
        Check that the CSV file is present in the current directory
        :param name: Name of the file to be checked
        :return: Boolean
        """
        warningColor = '\033[93m'
        resetColor = '\033[0m'
        try:
            with open("csvFiles/" + name):
                pass
            return True
        except IOError:
            print(warningColor + "Warning: CSV file not found"
                  + resetColor)
            return False

    def parseCSV(name: str) -> list:
        """
        Splitting of the CSV file passed in parameter
        :param name: CSV file's name
        :return: Array
        """
        with open("csvFiles/" + name, newline='') as csvfile:
            data = list(csv.reader(csvfile, delimiter=';'))
        return data

    def getNameCol(data: list) -> list:
        """
        Review the list of items in each row header
        :param data: 2D table of data from a CSV file
        :return: Array
        """
        list = []
        for i in range(len(data)):
            list.append(data[i][0])
        list.pop(0)
        return list

    def getNameRow(data: list) -> list:
        """
        Review the list of items in each column header
        :param data: 2D table of data from a CSV file
        :return: Array
        """
        list = []
        for i in range(len(data[0])):
            list.append(data[0][i])
        list.pop(0)
        return list

    def getNbCol(data: list) -> int:
        """
        Returns the number of columns in the CSV file
        :param data: 2D table of data from a CSV file
        :return: Integer
        """
        return len(parseFile.getNameCol(data))

    def getNbRow(data: list) -> int:
        """
        Returns the number of rows in the CSV file
        :param data: 2D table of data from a CSV file
        :return: Integer
        """
        return len(parseFile.getNameRow(data))

    def getPref(data: list, index: int) -> dict:
        """
        Returns a dictionary in the order of its preferences
        :param data: 2D table of data from a CSV file
        :param index: Reading direction
        :return: Dictionary
        """
        preferenceDict = {}
        for row in range(len(data)):
            tempDict = {}
            for col in range(len(data[row])):
                if (row > 0 and col > 0):
                    preferenceIndex = data[row][col].split(",")
                    tempDict[int(preferenceIndex[index])] = data[0][col]
            preferenceDict[data[row][0]] = list(dict(sorted(tempDict.items())).values())
        preferenceDict.pop('')
        return preferenceDict

    def getPrefCol(data: list) -> dict:
        """
        Returns a dictionary with the values of each column as key
        :param data: 2D table of data from a CSV file
        :return: Dictionary
        """
        invertTable = []
        for col in range(len(data[0])):
            list = []
            for row in range(len(data)):
                list.append(data[row][col])
            invertTable.append(list)

        return parseFile.getPref(invertTable, 1)

    def getPrefRow(data: list) -> dict:
        """
        Returns a dictionary with the values of each row as key
        :param data: 2D table of data from a CSV file
        :return: Dictionary
        """
        return parseFile.getPref(data, 0)