import csv


class parseFile:
    def presenceFile(name: str) -> bool:
        """
        Vérification de la présence du fichier csv dans le répertoire courant
        :param name: Nom du fichier à vérifier
        :return: Boolean
        """
        warningColor = '\033[93m'
        resetColor = '\033[0m'
        try:
            with open(name):
                pass
            return True
        except IOError:
            print(warningColor + "Warning: Fichier CSV non trouvé"
                  + resetColor)
            return False

    def parseCSV(name: str) -> list:
        """
        Découpage du fichier CSV passé en paramètre
        :param name: Nom du fichier CSV
        :return: Array
        """
        with open(name, newline='') as csvfile:
            data = list(csv.reader(csvfile, delimiter=';'))
        return data

    def getNameCol(data: list) -> list:
        """
        Revoie la liste des éléments présents dans l'entête de chaque ligne
        :param data: Tableau 2D des données d'un fichier CSV
        :return: Array
        """
        list = []
        for i in range(len(data)):
            list.append(data[i][0])
        list.pop(0)
        return list

    def getNameRow(data: list) -> list:
        """
        Revoie la liste des éléments présents dans l'entête de chaque colonne
        :param data: Tableau 2D des données d'un fichier CSV
        :return: Array
        """
        list = []
        for i in range(len(data[0])):
            list.append(data[0][i])
        list.pop(0)
        return list

    def getNbCol(data: list) -> int:
        """
        Renvoie le nombre de colonnes du fichier CSV
        :return: Integer
        """
        return len(parseFile.getNameCol(data))

    def getNbRow(data: list) -> int:
        """
        Renvoie le nombre de lignes du fichier CSV
        :return: Integer
        """
        return len(parseFile.getNameRow(data))
