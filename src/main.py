from parseFile import parseFile as ps
from userInteraction import userInteraction as ui


# Programme principal
def main():
    fileName = ui.nameFile()
    if ps.presenceFile(fileName):
        bind = ui.whoBiding()
        data = ps.parseCSV(fileName)
        print(data)
        print(len(data))
        print(ps.getNameCol(data))
        print("Le nombre de colonnes est de : " + str(ps.getNbCol(data)))
        print(ps.getNameRow(data))
        print("Le nombre de lignes est de : " + str(ps.getNbRow(data)))


if __name__ == '__main__':
    main()