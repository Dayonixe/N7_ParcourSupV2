from parseFile import parseFile as ps

if __name__ == '__main__':
    fileName = "example1.csv"
    if ps.presenceFile(fileName):
        data = ps.parseCSV(fileName)
        print(ps.getNameCol(data))
        print(ps.getNameRow(data))
