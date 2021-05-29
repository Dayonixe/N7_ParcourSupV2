import sys


class userInteraction:
    @staticmethod
    def nameFile() -> str:
        """
        Demande à l'utilisateur le nom du fichier CSV qui contient les données
        :return: String
        """
        warningColor = '\033[93m'
        resetColor = '\033[0m'

        name = input("Entrer le nom du fichier csv : ")
        checkName = name.split(".")

        if (len(checkName) < 2 or len(checkName) > 2 or checkName[1] != "csv"):
            print(warningColor + "Warning: Nom de fichier incorrect"
                  + resetColor)
            sys.exit()

        return name

    @staticmethod
    def whoBiding() -> str:
        """
        Demande à l'utilisateur qui fait l'association (lignes/colonnes)
        :return: String
        """
        isValid = False
        while not isValid:
            bind = input("Entrer qui fait l'association [Row/Col] : ")
            if (bind.lower() in ['r', 'row', 'rows', 'l', 'ligne', 'lignes']):
                return 'R'
            elif (bind.lower() in ['c', 'col', 'column', 'columns', 'colonne', 'colonnes']):
                return 'C'
